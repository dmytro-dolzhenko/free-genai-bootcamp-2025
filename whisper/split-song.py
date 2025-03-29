from spleeter.separator import Separator

# Load Spleeter model (2 stems: Vocals + Instrumental)
separator = Separator('spleeter:2stems')

# Input audio file (Replace with your file)
input_audio = "audio/song.mp3"

# Output directory
output_dir = "output/"

# Process and separate the audio
separator.separate_to_file(input_audio, output_dir)

print("Separation complete! Check the 'output/' folder.")
