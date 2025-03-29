# Whisper Karaoke Project

This project uses OpenAI's Whisper model and other tools to create a karaoke video with synchronized lyrics. It processes audio files to extract vocals, transcribe lyrics, and generate a karaoke-style video with highlighted words.

## Features
- Extract vocals and accompaniment from audio files using Spleeter.
- Transcribe lyrics with word-level timestamps using Whisper.
- Generate a karaoke video with synchronized lyrics and highlighted words.

## Prerequisites
- Python 3.8 or higher
- ffmpeg installed on your system
- Fonts installed (e.g., Arial)

## Installation
1. Update your system:
   ```bash
   sudo apt update
   sudo apt install ffmpeg
   ```

2. Install fonts:
   ```bash
   sudo apt install ttf-mscorefonts-installer
   ```

3. Install required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

## How to Run
1. **Split the song into vocals and accompaniment:**
   Run `split-song.py` to separate the input audio file into vocals and accompaniment.
   ```bash
   python split-song.py
   ```

2. **Transcribe lyrics:**
   Run `whisper-extract.py` to transcribe the vocals and generate a `lyrics.txt` file with word-level timestamps.
   ```bash
   python whisper-extract.py
   ```

3. **Generate karaoke video:**
   Run `karaoke.py` to create a karaoke video with synchronized lyrics.
   ```bash
   python karaoke.py
   ```

4. The output video will be saved as `karaoke.mp4`.

## Tools Summary

### 1. **Whisper**
- Whisper is an automatic speech recognition (ASR) model by OpenAI.
- Used in `whisper-extract.py` to transcribe audio and generate word-level timestamps for lyrics.

### 2. **Spleeter**
- Spleeter is a pre-trained source separation library by Deezer.
- Used in `split-song.py` to separate vocals and accompaniment from an audio file.

### 3. **MoviePy**
- MoviePy is a Python library for video editing.
- Used in `karaoke.py` to create a karaoke video by combining audio and synchronized lyrics.

### 4. **Pillow**
- Pillow is a Python Imaging Library for image processing.
- Used in `karaoke.py` to create text frames with highlighted words for the karaoke video.

### 5. **FFmpeg**
- FFmpeg is a multimedia framework for handling audio and video.
- Required for processing audio and video files in the project.