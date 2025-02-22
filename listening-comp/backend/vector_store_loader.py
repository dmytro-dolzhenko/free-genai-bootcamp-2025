import chromadb
import os
import json
import logging
from typing import List, Dict, Any
from uuid import uuid4

class VectorStoreLoader:
    def __init__(self, persist_directory: str = "chroma_db"):
        """
        Initialize the VectorStoreLoader with a persistence directory for ChromaDB.
        
        Args:
            persist_directory (str): Directory where ChromaDB will persist its data
        """
        self.persist_directory = persist_directory
        
        # Create persist directory if it doesn't exist
        os.makedirs(persist_directory, exist_ok=True)
        
        try:
            self.client = chromadb.PersistentClient(path=persist_directory)
            logging.info(f"ChromaDB client initialized with persist directory: {persist_directory}")
        except Exception as e:
            logging.error(f"Failed to initialize ChromaDB client: {str(e)}")
            raise

    def load_vectorized_data(self, 
                           vectorized_data_path: str,
                           collection_name: str = "documents",
                           batch_size: int = 100) -> chromadb.Collection:
        """
        Load vectorized data from the specified directory into ChromaDB.
        
        Args:
            vectorized_data_path (str): Path to the directory containing vectorized data
            collection_name (str): Name of the collection to create/use in ChromaDB
            batch_size (int): Number of documents to add in each batch
            
        Returns:
            chromadb.Collection: The ChromaDB collection containing the loaded vectors
        """
        try:
            # Get or create collection
            collection = self.client.get_or_create_collection(name=collection_name)
            logging.info(f"Using collection: {collection_name}")
            
            # Group related files by video_id
            file_groups = {}
            for filename in os.listdir(vectorized_data_path):
                if filename.endswith('.json'):
                    video_id = filename.split('_')[0]
                    if video_id not in file_groups:
                        file_groups[video_id] = []
                    file_groups[video_id].append(filename)

            total_documents = 0
            
            # Process each group of files
            for video_id, filenames in file_groups.items():
                logging.info(f"Processing files for video_id: {video_id}")
                
                metadata = {}
                patterns = []
                questions = []
                
                # Load data from each file
                for filename in filenames:
                    file_path = os.path.join(vectorized_data_path, filename)
                    try:
                        with open(file_path, 'r') as f:
                            data = json.load(f)
                            
                        if filename.endswith('_metadata.json'):
                            metadata = data
                        elif filename.endswith('_patterns.json'):
                            patterns = data
                        elif filename.endswith('_questions.json'):
                            questions = data
                    except json.JSONDecodeError as e:
                        logging.error(f"Failed to parse JSON from {file_path}: {str(e)}")
                        continue
                    except Exception as e:
                        logging.error(f"Error processing file {file_path}: {str(e)}")
                        continue

                # Process questions and patterns into documents
                documents, metadatas, ids = self._format_document_text(video_id, metadata)

                # Add patterns
                for pattern in patterns:
                    doc_text = f"Video: {video_id}\nTopic: {pattern['topic']}\n"
                    doc_text += f"Section: {pattern['section_name']}\n"
                    doc_text += f"Question Type: {pattern['question_type']}\n"
                    doc_text += "Patterns:\n" + "\n".join(pattern['patterns'])
                    
                    documents.append(doc_text)
                    metadatas.append({
                        "video_id": video_id,
                        "content_type": "pattern",
                        "topic": pattern["topic"],
                        "section_name": pattern["section_name"]
                    })
                    ids.append(f"pattern_{video_id}_{str(uuid4())}")

                # Add questions
                for question in questions:
                    doc_text = f"Video: {video_id}\nTopic: {question['topic']}\n"
                    doc_text += f"Question: {question['question_text']}\n"
                    doc_text += f"Context: {question['context']}\n"
                    doc_text += f"Pattern: {question['pattern']}\n"
                    doc_text += "Options:\n" + "\n".join(question['answer_options'])
                    doc_text += f"\nCorrect Answer: {question['correct_answer']}"
                    
                    documents.append(doc_text)
                    metadatas.append({
                        "video_id": video_id,
                        "content_type": "question",
                        "topic": question["topic"],
                        "section_name": question["section_name"],
                        "question_type": question["question_type"]
                    })
                    ids.append(f"question_{video_id}_{str(uuid4())}")

                # Add to collection in batches
                for i in range(0, len(documents), batch_size):
                    batch_docs = documents[i:i + batch_size]
                    batch_meta = metadatas[i:i + batch_size]
                    batch_ids = ids[i:i + batch_size]
                    
                    try:
                        collection.add(
                            documents=batch_docs,
                            metadatas=batch_meta,
                            ids=batch_ids
                        )
                        total_documents += len(batch_docs)
                        logging.info(f"Added batch of {len(batch_docs)} documents to collection")
                    except Exception as e:
                        logging.error(f"Failed to add batch to collection: {str(e)}")
                        continue

            logging.info(f"Successfully loaded {total_documents} documents into collection {collection_name}")
            return collection
            
        except Exception as e:
            logging.error(f"Error in load_vectorized_data: {str(e)}")
            raise

    def get_collection(self, collection_name: str = "documents") -> chromadb.Collection:
        """
        Get an existing collection from ChromaDB.
        
        Args:
            collection_name (str): Name of the collection to retrieve
            
        Returns:
            chromadb.Collection: The requested ChromaDB collection
        """
        try:
            collection = self.client.get_collection(name=collection_name)
            logging.info(f"Retrieved collection: {collection_name}")
            return collection
        except Exception as e:
            logging.error(f"Failed to get collection {collection_name}: {str(e)}")
            raise

    def delete_collection(self, collection_name: str = "documents") -> None:
        """
        Delete a collection from ChromaDB.
        
        Args:
            collection_name (str): Name of the collection to delete
        """
        try:
            self.client.delete_collection(name=collection_name)
            logging.info(f"Deleted collection: {collection_name}")
        except Exception as e:
            logging.error(f"Failed to delete collection {collection_name}: {str(e)}")
            raise 

    def _format_document_text(self, video_id: str, metadata: Dict) -> List[Dict]:
        """
        Format metadata into documents for vector storage.
        """
        documents = []
        metadatas = []
        ids = []

        # Add introduction document
        intro_text = f"Video: {video_id}\nTopic: {metadata['topic']}\n"
        intro_text += f"Greeting: {metadata['introduction']['greeting']}\n"
        intro_text += f"Lesson Overview: {metadata['introduction']['lesson_overview']}\n"
        intro_text += f"Target Audience: {metadata['introduction']['target_audience']}"
        
        documents.append(intro_text)
        metadatas.append({
            "video_id": video_id,
            "content_type": "introduction",
            "topic": metadata["topic"]
        })
        ids.append(f"intro_{video_id}")

        # Add conversation segments
        if 'full_conversation' in metadata:
            # Opening segment
            if metadata['full_conversation'].get('opening_segment'):
                conv_text = f"Video: {video_id}\nTopic: {metadata['topic']}\n"
                conv_text += f"Segment: Opening\n"
                conv_text += f"Content: {metadata['full_conversation']['opening_segment']}"
                
                documents.append(conv_text)
                metadatas.append({
                    "video_id": video_id,
                    "content_type": "conversation",
                    "topic": metadata["topic"],
                    "segment_type": "opening"
                })
                ids.append(f"conv_{video_id}_opening")

            # Example segment
            if metadata['full_conversation'].get('example_segment'):
                conv_text = f"Video: {video_id}\nTopic: {metadata['topic']}\n"
                conv_text += f"Segment: Example\n"
                conv_text += f"Content: {metadata['full_conversation']['example_segment']}"
                
                documents.append(conv_text)
                metadatas.append({
                    "video_id": video_id,
                    "content_type": "conversation",
                    "topic": metadata["topic"],
                    "segment_type": "example"
                })
                ids.append(f"conv_{video_id}_example")

            # Main segment
            if metadata['full_conversation'].get('main_segment'):
                conv_text = f"Video: {video_id}\nTopic: {metadata['topic']}\n"
                conv_text += f"Segment: Main\n"
                conv_text += f"Content: {metadata['full_conversation']['main_segment']}"
                
                documents.append(conv_text)
                metadatas.append({
                    "video_id": video_id,
                    "content_type": "conversation",
                    "topic": metadata["topic"],
                    "segment_type": "main"
                })
                ids.append(f"conv_{video_id}_main")

        return documents, metadatas, ids 