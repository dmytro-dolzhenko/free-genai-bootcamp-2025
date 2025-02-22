import random
import requests
import json
from typing import Optional, Dict
import openai
from PIL import Image
import numpy as np
from functools import lru_cache
from pathlib import Path
import yaml
from utils.logging_config import setup_logger
from drawing_comparison import compare_kanji                                            

# Initialize logger
logger = setup_logger('sentence_generator')

# Lazy load all heavy imports
@lru_cache(maxsize=1)
def get_mocr():
    """Lazy loading of MangaOCR"""
    import torch  # Import torch first
    torch.set_grad_enabled(False)  # Disable gradients since we don't need them
    from manga_ocr import MangaOcr
    return MangaOcr()

@lru_cache(maxsize=1)
def load_prompts() -> str:
    """Load prompt template from YAML file and clean it"""
    prompt_path = Path(__file__).parent / "prompts" / "sentence_generation.yaml"
    with open(prompt_path, 'r', encoding='utf-8') as f:
        prompts = yaml.safe_load(f)
    
    # Get the template and normalize whitespace
    template = prompts['sentence_generation']['template']
    result = ' '.join(template.replace('\n', ' ').split())
    logger.info(f"Loaded prompt: {result}")
    return result

def fetch_random_word(group_id: int, api_base_url: str = "http://localhost:5000") -> Optional[Dict]:
    """Fetch a random word from the specified group"""
    try:
        logger.info(f"Fetching random word from group {group_id}")
        # Fetch all words from the group
        response = requests.get(
            f"{api_base_url}/groups/{group_id}/words/raw",
            headers={'Accept': 'application/json; charset=utf-8'}
        )
        response.raise_for_status()
        response.encoding = 'utf-8'  # Force UTF-8 encoding
        
        data = response.json()
        if not data.get("words"):
            logger.warning(f"No words found in group {group_id}")
            return None
            
        # Select a random word from the list
        word = random.choice(data["words"])
        logger.info(f"Selected word: {word['romaji']} ({word['english']})")
        return word
        
    except requests.RequestException as e:
        logger.error(f"Error fetching word: {e}")
        return None

def extract_json_from_response(response_text: str) -> Optional[Dict]:
    """Extract and parse JSON from Ollama response"""
    try:
        # Look for JSON block after ```json marker
        if '```json' in response_text:
            json_start = response_text.find('```json') + 7
            json_end = response_text.find('```', json_start)
            if json_end != -1:
                json_text = response_text[json_start:json_end].strip()
            else:
                json_text = response_text[json_start:].strip()
        else:
            # Fallback to finding JSON between curly braces
            start_idx = response_text.find('{')
            end_idx = response_text.rfind('}')
            if start_idx == -1 or end_idx == -1:
                logger.error("No JSON found in response")
                return None
            json_text = response_text[start_idx:end_idx + 1]

        logger.debug(f"Extracted JSON text: {json_text}")
        return json.loads(json_text)
    except Exception as e:
        logger.error(f"Failed to extract JSON: {e}")
        return None

def generate_sentence_with_ollama(word: Dict, api_key: str = None) -> Optional[Dict]:
    """Generate a Japanese sentence using local LLM (Ollama) that includes the given word"""
    try:
        romaji = word['romaji']
        english = word['english']
        
        logger.info(f"Generating sentence for word: {romaji} ({english})")
        
        prompt = load_prompts().format(
            romaji=romaji,
            english=english
        )
        
        logger.info(f"Sending prompt to Ollama API: {prompt}")
        response = requests.post(
            "http://localhost:8008/api/generate",
            json={
                "model": "llama3.2:3b",
                "prompt": prompt,
                "stream": False
            },
            headers={
                'Content-Type': 'application/json; charset=utf-8',
                'Accept': 'application/json'
            }
        )        
        response.raise_for_status()
        
        # Parse the response
        result = response.json()
        logger.info(f"Ollama response: {result}")
        response_text = result['response'].strip()
        
        # Extract JSON from response
        sentence_data = extract_json_from_response(response_text)
        if not sentence_data:
            return None
            
        # Fix common issues
        if 'japanesee' in sentence_data:
            sentence_data['japanese'] = sentence_data.pop('japanesee')
            
        if 'japanese' not in sentence_data or 'english' not in sentence_data:
            logger.error("Missing required fields in JSON response")
            return None
            
        # Clean up the values
        sentence_data['japanese'] = sentence_data['japanese'].strip()
        sentence_data['english'] = sentence_data['english'].strip()
                
        logger.info(f"Generated sentence: {sentence_data['japanese']}")
        logger.debug(f"Full parsed response: {sentence_data}")
        
        return sentence_data
        
    except (requests.RequestException, KeyError) as e:
        logger.error(f"Error generating sentence with local LLM: {e}")
        return None

def generate_random_sentence(group_id: int, api_key: str = None) -> Optional[Dict]:
    """Generate a random sentence using a Japanese word"""
    logger.info(f"Starting random sentence generation for group {group_id}")
    
    word = fetch_random_word(group_id)
    if not word:
        logger.warning("Failed to fetch random word")
        return None
        
    sentence = generate_sentence_with_ollama(word)
    if not sentence:
        logger.warning("Failed to generate sentence")
        return None
        
    logger.info("Successfully generated random sentence")
    return {
        'word': word,
        'sentence': sentence
    } 