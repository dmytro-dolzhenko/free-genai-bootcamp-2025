from youtube_transcriber import YouTubeTranscriber
from transcript_analyzer import TranscriptAnalyzer
from vector_store_loader import VectorStoreLoader
import re
import os



def main():
    # Initialize components
    yt = YouTubeTranscriber()
    transcript_analyzer = TranscriptAnalyzer(
        region_name="eu-west-1", 
        model_id="mistral.mistral-large-2402-v1:0"
    )
    vector_store = VectorStoreLoader(persist_directory="./chroma_db")

    # Transcribe videos
    yt.transcribe("https://www.youtube.com/watch?v=0e0duD8_LFE&list=PLkGU7DnOLgRMl-h4NxxrGbK-UdZHIXzKQ", "ja")

    # Process transcripts and save to files
    print("Analyzing transcripts...")
    transcript_dir = "transcripts"
    results = []

    # Process each transcript file
    for filename in os.listdir(transcript_dir):
        if filename.endswith(".txt"):
            print(f"\nProcessing transcript: {filename}")
            try:
                result = transcript_analyzer.analyze_transcript(filename)
                if result:
                    results.append(result)
                    print(f"Successfully analyzed {filename}")
                else:
                    print(f"Failed to analyze {filename}")
            except Exception as e:
                print(f"Error processing {filename}: {str(e)}")
                continue

    print(f"\nAnalyzed {len(results)} transcripts successfully")

    # Load the vectorized data into ChromaDB
    try:
        collection = vector_store.load_vectorized_data(
            vectorized_data_path="vectorized_data",
            collection_name="japanese_lessons"
        )
        print(f"\nSuccessfully loaded data into ChromaDB collection: {collection.name}")
        
        # Print some stats about the loaded data
        collection_stats = collection.count()
        print(f"Total documents in collection: {collection_stats}")
    except Exception as e:
        print(f"Error loading data into vector store: {str(e)}")

if __name__ == "__main__":
    main()
