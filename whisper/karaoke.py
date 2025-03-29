from moviepy import CompositeVideoClip, AudioFileClip, ImageClip
from PIL import Image, ImageDraw, ImageFont
import json
import numpy as np
import textwrap

# Load the audio file
audio = AudioFileClip("output/song/accompaniment.wav")

# Create a list to hold the text clips
text_clips = []

def create_text_frame(before_text, word_text, after_text):
    # Create a new image with black background
    img = Image.new('RGB', (1200, 200), color='black')
    draw = ImageDraw.Draw(img)
    
    # Load a font
    try:
        font = ImageFont.truetype("Arial", 50)
    except:
        font = ImageFont.load_default()
    
    # Combine text to check total length
    total_text = before_text + word_text + after_text
    
    # Calculate maximum width for text
    max_width = 1100  # Leave some margin
    
    # Get initial text size
    total_bbox = draw.textbbox((0, 0), total_text, font=font)
    total_width = total_bbox[2] - total_bbox[0]
    
    # If text is too wide, reduce font size
    current_font_size = 50
    while total_width > max_width and current_font_size > 20:
        current_font_size -= 2
        try:
            font = ImageFont.truetype("Arial", current_font_size)
        except:
            font = ImageFont.load_default()
        total_bbox = draw.textbbox((0, 0), total_text, font=font)
        total_width = total_bbox[2] - total_bbox[0]
    
    # If still too wide, wrap the text
    if total_width > max_width:
        # Split text into lines
        words = total_text.split()
        lines = []
        current_line = []
        current_width = 0
        
        for w in words:
            w_bbox = draw.textbbox((0, 0), w + " ", font=font)
            w_width = w_bbox[2] - w_bbox[0]
            if current_width + w_width <= max_width:
                current_line.append(w)
                current_width += w_width
            else:
                lines.append(" ".join(current_line))
                current_line = [w]
                current_width = w_width
        if current_line:
            lines.append(" ".join(current_line))
        
        # Draw each line
        y = 10  # Start from top with some margin
        for line in lines:
            # Find word position in this line
            if word_text in line:
                # Split line into parts around the word
                word_pos = line.find(word_text)
                line_before = line[:word_pos]
                line_after = line[word_pos + len(word_text):]
                
                # Get text sizes for this line
                before_bbox = draw.textbbox((0, 0), line_before, font=font)
                word_bbox = draw.textbbox((0, 0), word_text, font=font)
                total_bbox = draw.textbbox((0, 0), line, font=font)
                
                # Center this line
                start_x = (1200 - (total_bbox[2] - total_bbox[0])) // 2
                current_x = start_x
                
                # Draw the parts
                draw.text((current_x, y), line_before, font=font, fill='white')
                current_x += before_bbox[2] - before_bbox[0]
                draw.text((current_x, y), word_text, font=font, fill='red')
                current_x += word_bbox[2] - word_bbox[0]
                draw.text((current_x, y), line_after, font=font, fill='white')
            else:
                # Center and draw the whole line in white
                bbox = draw.textbbox((0, 0), line, font=font)
                x = (1200 - (bbox[2] - bbox[0])) // 2
                draw.text((x, y), line, font=font, fill='white')
            
            y += int(current_font_size * 1.5)  # Move to next line with spacing
    else:
        # Text fits on one line, draw normally
        # Calculate positions to center the text
        start_x = (1200 - total_width) // 2
        y = (200 - (total_bbox[3] - total_bbox[1])) // 2
        
        # Get individual text sizes
        before_bbox = draw.textbbox((0, 0), before_text, font=font)
        word_bbox = draw.textbbox((0, 0), word_text, font=font)
        
        # Draw the text parts
        current_x = start_x
        
        # Draw before text in white
        draw.text((current_x, y), before_text, font=font, fill='white')
        current_x += before_bbox[2] - before_bbox[0]
        
        # Draw the word in red
        draw.text((current_x, y), word_text, font=font, fill='red')
        current_x += word_bbox[2] - word_bbox[0]
        
        # Draw after text in white
        draw.text((current_x, y), after_text, font=font, fill='white')
    
    # Convert PIL image to numpy array for MoviePy
    return np.array(img)

# Load the word timings
with open('lyrics.txt', 'r') as file:
    lyrics_data = json.load(file)

# Process each segment
current_segment = None
segment_start = 0
segment_end = 0

for segment in lyrics_data:
    segment_text = segment['text']
    first_word = segment['words'][0]
    last_word = segment['words'][-1]
    segment_start = first_word['start']
    segment_end = last_word['end']
    
    # Create a base clip for the entire segment with all white text
    base_frame = create_text_frame(segment_text, "", "")
    base_clip = ImageClip(base_frame).with_duration(segment_end - segment_start)
    base_clip = base_clip.with_start(segment_start).with_position(('center', 300))
    text_clips.append(base_clip)
    
    # For each word in the segment
    for word in segment['words']:
        word_text = word['word']
        word_start = word['start']
        word_end = word['end']
        
        # Find the position of the word in the segment text
        word_pos = segment_text.find(word_text)
        
        if word_pos >= 0:
            # Split the text into parts
            before_text = segment_text[:word_pos]
            after_text = segment_text[word_pos + len(word_text):]
            
            # Create frame with the highlighted word
            frame = create_text_frame(before_text, word_text, after_text)
            
            # Create clip from the frame
            clip = ImageClip(frame).with_duration(word_end - word_start)
            clip = clip.with_start(word_start).with_position(('center', 300))
            
            text_clips.append(clip)

# Create a composite video clip
video = CompositeVideoClip(text_clips, size=(1280, 720)).with_duration(audio.duration)

# Set the audio
video = video.with_audio(audio)

# Write the video to a file
video.write_videofile("karaoke.mp4", fps=24)
