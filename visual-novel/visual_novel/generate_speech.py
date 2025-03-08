import boto3
import os

# AWS Polly client
polly_client = boto3.Session(
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),  # Replace with your AWS access key
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),  # Replace with your AWS secret key
    region_name='us-west-2'  # Replace with your preferred region
).client('polly')

# Correct directory path for transcript files
transcripts_dir = '/mnt/f/Programming/gen-ai-bootcamp/free-genai-bootcamp-2025/visual-novel/visual_novel/game/transcripts'

# Mapping of speaker to AWS Polly voice
voice_mapping = {
    'alex': 'Takumi',  # Use Japanese voice for Japanese text
    'hana': 'Mizuki',  # Female Japanese voice
    'kaito': 'Takumi', # Male Japanese voice
    'yuki': 'Mizuki'   # Female Japanese voice
}

# Iterate over each transcript file
for filename in os.listdir(transcripts_dir):
    if filename.endswith('.txt'):
        # Determine the speaker from the filename
        speaker = filename.split('_')[0]
        voice_id = voice_mapping.get(speaker.lower())

        if voice_id:
            # Define the path for the audio file
            audio_file_path = os.path.join(transcripts_dir, f"{os.path.splitext(filename)[0]}.mp3")

            # Check if the audio file already exists
            if os.path.exists(audio_file_path):
                print(f"Audio file already exists for {filename}, skipping generation.")
                continue

            # Read the transcript
            with open(os.path.join(transcripts_dir, filename), 'r', encoding='utf-8') as file:
                text = file.read()

            # Escape special characters in text
            text = text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

            # Adjust speech characteristics for non-native accent simulation or character distinction
            if speaker.lower() == 'alex':
                text = f'<speak><prosody rate="slow" pitch="low">{text}</prosody></speak>'
            elif speaker.lower() == 'hana':
                text = f'<speak><prosody rate="medium" pitch="high">{text}</prosody></speak>'
            elif speaker.lower() == 'yuki':
                text = f'<speak><prosody rate="medium" pitch="low">{text}</prosody></speak>'
            elif speaker.lower() == 'kaito':
                text = f'<speak><prosody rate="medium" pitch="medium">{text}</prosody></speak>'

            # Debugging output
            print(f"SSML for {filename}: {text}")

            try:
                # Generate speech using AWS Polly
                response = polly_client.synthesize_speech(
                    Text=text,
                    OutputFormat='mp3',
                    VoiceId=voice_id,
                    TextType='ssml'  # Use SSML to apply prosody changes
                )

                # Save the audio stream to a file with the same base name as the text file
                with open(audio_file_path, 'wb') as audio_file:
                    audio_file.write(response['AudioStream'].read())

                print(f"Generated speech for {filename} as {audio_file_path}")
            except polly_client.exceptions.InvalidSsmlException as e:
                print(f"SSML error for {filename}: {e}")
        else:
            print(f"No voice mapping found for speaker: {speaker}") 