import whisper
import json

model = whisper.load_model("medium")
result = model.transcribe("output/song/vocals.wav", word_timestamps=True)

lyrics = []
for segment in result["segments"]:
    words = segment["words"]
    line_text = " ".join(word["word"] for word in words)
    start_time = words[0]["start"]
    end_time = words[-1]["end"]
    lyrics.append({"text": line_text, "start": start_time, "end": end_time, "words": words})        

# Save word timings to a file
with open("lyrics.txt", "w") as file:
    file.write(json.dumps(lyrics, indent=4))
