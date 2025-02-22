from typing import Dict
import numpy as np
from PIL import Image, ImageEnhance, ImageOps
from functools import lru_cache
from utils.logging_config import setup_logger

# Initialize logger
logger = setup_logger('drawing_comparison')

@lru_cache(maxsize=1)
def get_mocr():
    """Lazy loading of MangaOCR"""
    import torch  # Import torch first
    torch.set_grad_enabled(False)  # Disable gradients since we don't need them
    from manga_ocr import MangaOcr
    return MangaOcr()

def preprocess_image(img: Image.Image) -> Image.Image:
    """Preprocess image for better OCR recognition"""
    # 1. Increase contrast
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(2.0)
    
    # 2. Resize image to be larger
    width, height = img.size
    scale_factor = 2
    img = img.resize((width * scale_factor, height * scale_factor), Image.Resampling.LANCZOS)
    
    # 3. Threshold to make lines clearer
    img = ImageOps.invert(img)  # Invert colors (black on white)
    
    return img

def compare_kanji(drawn_image: np.ndarray, target_text: str) -> Dict:
    """Compare drawn text with target Japanese text using MangaOCR"""
    try:
        logger.info(f"Starting OCR comparison for target text: {target_text}")
        
        # Convert numpy array to PIL Image
        img = Image.fromarray(drawn_image.astype('uint8'), 'RGBA')
        
        # Convert to RGB if image has alpha channel
        if img.mode == 'RGBA':
            img = img.convert('RGB')
        
        # Preprocess image
        img = preprocess_image(img)
        
        # Get MangaOCR instance
        mocr = get_mocr()
        
        # Try multiple orientations
        orientations = [img, img.transpose(Image.Transpose.ROTATE_90)]
        detected_texts = []
        
        for oriented_img in orientations:
            detected_text = mocr(oriented_img)
            detected_texts.append(detected_text)
            logger.debug(f"Detected text in orientation: {detected_text}")
        
        # Choose the best match
        best_match = None
        best_similarity = 0
        
        for detected_text in detected_texts:
            # Remove spaces, numbers, and normalize for comparison
            detected_clean = ''.join(c for c in detected_text if not c.isspace() and not c.isnumeric())
            target_clean = ''.join(c for c in target_text if not c.isspace() and not c.isnumeric())
            
            # Calculate similarity
            from difflib import SequenceMatcher
            similarity = SequenceMatcher(None, detected_clean, target_clean).ratio()
            
            if similarity > best_similarity:
                best_similarity = similarity
                best_match = detected_text
        
        logger.info(f"Best detected text: {best_match} (similarity: {best_similarity})")
        
        # Consider it a match if similarity is above threshold
        is_match = best_similarity > 0.7
        
        return {
            'detected_text': best_match,
            'similarity': best_similarity,
            'is_match': is_match
        }
        
    except Exception as e:
        logger.error(f"Error in OCR comparison: {e}")
        return {
            'detected_text': '',
            'is_match': False,
            'error': str(e)
        } 