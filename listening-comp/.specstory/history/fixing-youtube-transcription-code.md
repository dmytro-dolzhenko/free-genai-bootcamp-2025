## SpecStory

## Fixing YouTube Transcription Code (2/21/2025, 9:23:48 PM)

_**User**_

Could you please fix it?

---

_**Assistant**_

I see the issue. The `transcribe` method in `YouTubeTranscriber` is expecting a single URL string, but we're passing a list of URLs. Let's modify the code to handle each URL individually.

Here's the fix for `app.py`:

```python:backend/app.py
from youtube_transcriber import YouTubeTranscriber

yt = YouTubeTranscriber()
video_url_list = []

def transcribe_all_videos():
    # Build list of video URLs
    for i in range(1, 55):
        url = f"https://www.youtube.com/watch?v=0e0duD8_LFE&list=PLkGU7DnOLgRMl-h4NxxrGbK-UdZHIXzKQ&index={i}"
        video_url_list.append(url)
    print("Starting transcription of all videos...")
    
    # Process each video URL individually
    for url in video_url_list:
        try:
            print(f"Transcribing video: {url}")
            yt.transcribe(url, "ja")
        except Exception as e:
            print(f"Error processing {url}: {str(e)}")
            continue
    
    print("Finished transcription process")
    
transcribe_all_videos()
```

The main changes are:
1. Instead of passing the entire list to `transcribe()`, we now loop through each URL
2. Added try-except block to handle errors for individual videos
3. Added some print statements to track progress
4. If one video fails, the script will continue with the next video instead of stopping completely

This should resolve the `decode` error and provide better error handling for the transcription process.

---

_**User**_

Make sure that each video with different index is stored within separate file

---

_**Assistant**_

I'll modify the code to save each video's transcription in a separate file based on its index.

```python:backend/app.py
from youtube_transcriber import YouTubeTranscriber
import re

yt = YouTubeTranscriber()
video_url_list = []

def extract_index_from_url(url):
    # Extract index parameter from URL
    match = re.search(r'index=(\d+)', url)
    return match.group(1) if match else 'unknown'

def transcribe_all_videos():
    # Build list of video URLs
    for i in range(1, 55):
        url = f"https://www.youtube.com/watch?v=0e0duD8_LFE&list=PLkGU7DnOLgRMl-h4NxxrGbK-UdZHIXzKQ&index={i}"
        video_url_list.append(url)
    print("Starting transcription of all videos...")
    
    # Process each video URL individually
    for url in video_url_list:
        try:
            index = extract_index_from_url(url)
            output_file = f"transcription_{index}.txt"
            print(f"Transcribing video {index}: {url}")
            yt.transcribe(url, "ja", output_file)
        except Exception as e:
            print(f"Error processing {url}: {str(e)}")
            continue
    
    print("Finished transcription process")
    
transcribe_all_videos()
```

You'll also need to modify the `transcribe` method in your `YouTubeTranscriber` class to accept an output filename parameter. Here's how you should modify that class:

```python:backend/youtube_transcriber.py
# ... existing imports and code ...

class YouTubeTranscriber:
    # ... existing methods ...

    def transcribe(self, video_url, lang="ja", output_file=None):
        try:
            video_id = self._extract_video_id(video_url)
            transcript_list = self._get_transcript(video_id, lang)
            
            # Combine all transcript text
            transcript_text = "\n".join([entry['text'] for entry in transcript_list])
            
            # If output_file is specified, write to that file
            if output_file:
                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write(transcript_text)
                print(f"Transcription saved to {output_file}")
            
            return transcript_text
            
        except Exception as e:
            raise Exception(f"Error transcribing video: {str(e)}")
```

The changes include:
1. Added a function to extract the index from the URL
2. Modified the code to create unique filenames based on the video index
3. Updated the `transcribe` method to accept an output filename parameter
4. Each transcription will now be saved in a separate file named `transcription_X.txt` where X is the video index

This will create separate files for each video's transcription, making it easier to manage and process the transcriptions individually.

---

_**User**_

I am getting errors



---

_**Assistant**_

Ah, I see the issue. We need to add the `_get_transcript` method to the `YouTubeTranscriber` class. Let's fix that:

```python:backend/youtube_transcriber.py
def _get_transcript(self, video_id: str, lang: str):
    """
    Get transcript for a video in specified language.
    
    Args:
        video_id (str): YouTube video ID
        lang (str): Language code (e.g., 'ja' for Japanese)
        
    Returns:
        list: List of transcript entries
    """
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=[lang])
        return transcript
    except Exception as e:
        raise Exception(f"Could not get transcript: {str(e)}")
```

Add this method to your `YouTubeTranscriber` class, right after the `_extract_video_id` method. The complete class should look like this:

```python:backend/youtube_transcriber.py
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter
import os
from typing import Union, List
from urllib.parse import urlparse, parse_qs

class YouTubeTranscriber:
    def __init__(self, output_dir: str = "transcripts"):
        """
        Initialize the YouTubeTranscriber with an output directory.
        
        Args:
            output_dir (str): Directory where transcripts will be saved
        """
        self.output_dir = output_dir
        self._create_output_dir()
    
    def _create_output_dir(self):
        """Create the output directory if it doesn't exist."""
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
    
    def _extract_video_id(self, url: str) -> str:
        """
        Extract video ID from YouTube URL.
        
        Args:
            url (str): YouTube video URL
            
        Returns:
            str: Video ID
        """
        parsed_url = urlparse(url)
        
        if parsed_url.hostname in ['www.youtube.com', 'youtube.com']:
            if parsed_url.path == '/watch':
                return parse_qs(parsed_url.query)['v'][0]
            elif parsed_url.path.startswith('/v/'):
                return parsed_url.path.split('/')[2]
        elif parsed_url.hostname == 'youtu.be':
            return parsed_url.path[1:]
        
        return url  # Return as-is if it's already a video ID

    def _get_transcript(self, video_id: str, lang: str):
        """
        Get transcript for a video in specified language.
        
        Args:
            video_id (str): YouTube video ID
            lang (str): Language code (e.g., 'ja' for Japanese)
            
        Returns:
            list: List of transcript entries
        """
        try:
            transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=[lang])
            return transcript
        except Exception as e:
            raise Exception(f"Could not get transcript: {str(e)}")
    
    def transcribe(self, video_url, lang, output_file=None):
        try:
            video_id = self._extract_video_id(video_url)
            transcript_list = self._get_transcript(video_id, lang)
            
            # Combine all transcript text
            transcript_text = "\n".join([entry['text'] for entry in transcript_list])
            
            # If output_file is specified, write to that file
            if output_file:
                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write(transcript_text)
                print(f"Transcription saved to {output_file}")
            
            return transcript_text
            
        except Exception as e:
            raise Exception(f"Error transcribing video: {str(e)}")
```

The changes include:
1. Added the missing `_get_transcript` method
2. The method uses `YouTubeTranscriptApi.get_transcript()` to fetch the transcript
3. It handles errors appropriately and returns the transcript list

This should resolve the "'YouTubeTranscriber' object has no attribute '_get_transcript'" error. Try running the script again with these changes.

---

_**User**_

@youtube_transcriber.py 
transcripts should be generated in transcripts folder and have videid as a name of the file

---

_**Assistant**_

I'll modify the `transcribe` method to save files in the transcripts folder with the video ID as the filename.

```python:backend/youtube_transcriber.py
def transcribe(self, video_url, lang, output_file=None):
    try:
        video_id = self._extract_video_id(video_url)
        transcript_list = self._get_transcript(video_id, lang)
        
        # Combine all transcript text
        transcript_text = "\n".join([entry['text'] for entry in transcript_list])
        
        # If output_file is specified, use that, otherwise use video_id in transcripts folder
        if output_file:
            file_path = output_file
        else:
            file_path = os.path.join(self.output_dir, f"{video_id}.txt")
        
        # Save the transcript
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(transcript_text)
        print(f"Transcription saved to {file_path}")
        
        return transcript_text
        
    except Exception as e:
        raise Exception(f"Error transcribing video: {str(e)}")
```

And in your `app.py`, you can now call `transcribe` without specifying the output file:

```python:backend/app.py
def transcribe_all_videos():
    # Build list of video URLs
    for i in range(1, 55):
        url = f"https://www.youtube.com/watch?v=0e0duD8_LFE&list=PLkGU7DnOLgRMl-h4NxxrGbK-UdZHIXzKQ&index={i}"
        video_url_list.append(url)
    print("Starting transcription of all videos...")
    
    # Process each video URL individually
    for url in video_url_list:
        try:
            index = extract_index_from_url(url)
            print(f"Transcribing video {index}: {url}")
            yt.transcribe(url, "ja")  # Removed output_file parameter
        except Exception as e:
            print(f"Error processing {url}: {str(e)}")
            continue
    
    print("Finished transcription process")
```

The changes include:
1. Modified `transcribe` method to use the video ID as filename when no output_file is specified
2. Files will be saved in the `transcripts` directory that was set up in `__init__`
3. Removed the output_file parameter from the `transcribe` call in `app.py`
4. Each transcript will now be saved as `transcripts/VIDEO_ID.txt`

This will ensure all transcripts are organized in the transcripts folder with their video IDs as filenames.

---



---

