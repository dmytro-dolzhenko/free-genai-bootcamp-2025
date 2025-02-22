import boto3
import os
from typing import Dict, List, Optional
from uuid import uuid4
from io import BytesIO
import time

class AudioGenerator:
    def __init__(self, region_name: str = "eu-west-1"):
        """
        Initialize AudioGenerator with AWS Polly client.
        
        Args:
            region_name (str): AWS region name for Polly
        """
        self.polly = boto3.client('polly', region_name=region_name)
        self.audio_dir = os.path.join(os.path.dirname(__file__), 'audio_cache')
        os.makedirs(self.audio_dir, exist_ok=True)
        
        # Using only standard engine voices
        self.voices = {
            'male': [
                {'id': 'Takumi', 'engine': 'standard'}
            ],
            'female': [
                {'id': 'Mizuki', 'engine': 'standard'},
                {'id': 'Tomoko', 'engine': 'standard'}
            ]
        }
        
        # Cache for speaker-voice mapping to maintain consistency
        self.speaker_voice_map = {}

    def _get_voice_for_speaker(self, speaker_name: str) -> Dict[str, str]:
        """
        Get or assign a consistent voice for a speaker based on their name.
        Handles names in format '田中太郎 (Tanaka Taro)' or '山本さくら (Yamamoto Sakura)'.
        
        Args:
            speaker_name (str): Name of speaker in Japanese (English) format
            
        Returns:
            Dict[str, str]: Dictionary containing voice ID and engine type
        """
        if speaker_name in self.speaker_voice_map:
            return self.speaker_voice_map[speaker_name]
        
        # Split Japanese and English names
        japanese_name = speaker_name.split(' (')[0] if ' (' in speaker_name else speaker_name
        english_name = speaker_name.split('(')[1].rstrip(')') if '(' in speaker_name else ''
        
        # Male name indicators
        male_ja_indicators = ['太郎', '一郎', '健', '翔太', '勇気', '雄', '男']
        male_en_indicators = ['Taro', 'Ichiro', 'Ken', 'Shota', 'Yuki', 'ro']  # 'ro' for names ending in -taro
        
        # Female name indicators
        female_ja_indicators = ['さくら', '美咲', '花子', '愛', '優子', 'さん', '子']
        female_en_indicators = ['Sakura', 'Misaki', 'Hanako', 'Ai', 'Yuko', 'ko']  # 'ko' for names ending in -ko
        
        # Check if male
        is_male = (
            any(ind in japanese_name for ind in male_ja_indicators) or
            any(ind in english_name for ind in male_en_indicators) or
            english_name.endswith('ro')
        )
        
        # Check if female
        is_female = (
            any(ind in japanese_name for ind in female_ja_indicators) or
            any(ind in english_name for ind in female_en_indicators) or
            english_name.endswith('ko')
        )
        
        # Default to male if neither is detected (you might want to adjust this logic)
        voice_list = self.voices['male'] if is_male or not is_female else self.voices['female']
        
        # Try to use a voice that hasn't been used yet
        used_voices = set(v['id'] for v in self.speaker_voice_map.values())
        available_voices = [v for v in voice_list if v['id'] not in used_voices]
        
        # If all voices are used, cycle through them
        if not available_voices:
            available_voices = voice_list
        
        voice = available_voices[0]
        self.speaker_voice_map[speaker_name] = voice
        
        print(f"Assigned voice {voice['id']} to speaker {speaker_name}")  # Debug print
        return voice

    def _generate_audio(self, text: str, voice_config: Dict[str, str]) -> bytes:
        """
        Generate audio using AWS Polly with specified voice.
        
        Args:
            text (str): Text to synthesize
            voice_config (Dict[str, str]): Voice configuration
            
        Returns:
            bytes: Audio data
        """
        try:
            # Add a small pause after each line
            text_with_pause = text + "。。。"  # Add Japanese periods for natural pause
            
            response = self.polly.synthesize_speech(
                Engine=voice_config['engine'],
                LanguageCode='ja-JP',
                Text=text_with_pause,
                TextType='text',
                OutputFormat='mp3',
                VoiceId=voice_config['id']
            )
            
            if "AudioStream" in response:
                return response["AudioStream"].read()
            else:
                raise Exception("No AudioStream in response")
                
        except Exception as e:
            raise Exception(f"Error generating audio: {str(e)}")

    def _concatenate_audio(self, audio_parts: List[bytes]) -> bytes:
        """Concatenate multiple MP3 audio parts into a single file."""
        try:
            from pydub import AudioSegment
            
            # Convert each part to AudioSegment
            segments = []
            for audio_data in audio_parts:
                segment = AudioSegment.from_mp3(BytesIO(audio_data))
                segments.append(segment)
                
                # Add 1 second silence between segments
                silence = AudioSegment.silent(duration=1000)
                segments.append(silence)
            
            # Combine all segments
            combined = segments[0]
            for segment in segments[1:]:
                combined = combined + segment
            
            # Export to mp3
            output = BytesIO()
            combined.export(output, format="mp3")
            return output.getvalue()
            
        except Exception as e:
            raise Exception(f"Error concatenating audio: {str(e)}")

    def generate_conversation_audio(self, conversation_data: Dict) -> str:
        """
        Generate single audio file for entire conversation/monologue with different voices.
        
        Args:
            conversation_data (Dict): Contains either 'conversation' list or 'monologue' dict
            
        Returns:
            str: Path to the generated audio file
        """
        try:
            audio_parts = []
            
            if "monologue" in conversation_data:
                # Handle monologue
                speaker = conversation_data['monologue']['speaker']
                voice = self._get_voice_for_speaker(speaker)
                audio_data = self._generate_audio(conversation_data['monologue']['text'], voice)
                audio_parts.append(audio_data)
            else:
                # Handle conversation
                for line in conversation_data['conversation']:
                    speaker = line['speaker']
                    voice = self._get_voice_for_speaker(speaker)
                    print(f"Generating audio for {speaker} using voice {voice['id']}")
                    
                    audio_data = self._generate_audio(line['text'], voice)
                    audio_parts.append(audio_data)
            
            # Combine all audio parts
            print(f"Combining {len(audio_parts)} audio segments")
            combined_audio = self._concatenate_audio(audio_parts)
            
            # Save combined audio
            audio_id = f"conversation_{uuid4().hex[:8]}"
            audio_path = os.path.join(self.audio_dir, f"{audio_id}.mp3")
            
            with open(audio_path, 'wb') as f:
                f.write(combined_audio)
            
            print(f"Saved combined audio to {audio_path}")
            return audio_path
            
        except Exception as e:
            raise Exception(f"Error generating conversation audio: {str(e)}")

    def cleanup_old_audio(self, max_age_hours: int = 24):
        """
        Clean up audio files older than specified hours.
        
        Args:
            max_age_hours (int): Maximum age of files in hours
        """
        try:
            current_time = os.time()
            for filename in os.listdir(self.audio_dir):
                file_path = os.path.join(self.audio_dir, filename)
                if os.path.isfile(file_path):
                    file_age = (current_time - os.path.getmtime(file_path)) / 3600
                    if file_age > max_age_hours:
                        os.remove(file_path)
                        
        except Exception as e:
            print(f"Error cleaning up audio files: {str(e)}") 