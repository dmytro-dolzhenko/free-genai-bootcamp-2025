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
    
    def transcribe_multiple(self, video_urls: List[str], languages: Union[str, List[str]] = ['en']) -> List[str]:
        """
        Transcribe multiple YouTube videos.
        
        Args:
            video_urls (List[str]): List of YouTube video URLs or video IDs
            languages (Union[str, List[str]]): Preferred language(s) for transcription
            
        Returns:
            List[str]: List of paths to the saved transcript files
        """
        transcript_files = []
        for url in video_urls:
            try:
                transcript_file = self.transcribe(url, languages)
                transcript_files.append(transcript_file)
            except Exception as e:
                print(f"Error transcribing {url}: {str(e)}")
        
        return transcript_files 