## SpecStory

## Loading Vectorized Data into ChromaDB (2/21/2025, 11:07:31 PM)

_**User**_

I now have vectorized data stored in vectorized_data folder. Can you create a separate class to load this data into ChromaDB vector store? 

---

_**Assistant**_

I'll help you create a new class to handle loading vectorized data into ChromaDB. I'll create a new file called `vector_store_loader.py` that will contain this functionality.

```python:vector_store_loader.py
import chromadb
import os
import json
from typing import List, Dict, Any

class VectorStoreLoader:
    def __init__(self, persist_directory: str = "chroma_db"):
        """
        Initialize the VectorStoreLoader with a persistence directory for ChromaDB.
        
        Args:
            persist_directory (str): Directory where ChromaDB will persist its data
        """
        self.persist_directory = persist_directory
        self.client = chromadb.PersistentClient(path=persist_directory)

    def load_vectorized_data(self, 
                           vectorized_data_path: str,
                           collection_name: str = "documents") -> chromadb.Collection:
        """
        Load vectorized data from the specified directory into ChromaDB.
        
        Args:
            vectorized_data_path (str): Path to the directory containing vectorized data
            collection_name (str): Name of the collection to create/use in ChromaDB
            
        Returns:
            chromadb.Collection: The ChromaDB collection containing the loaded vectors
        """
        # Get or create collection
        collection = self.client.get_or_create_collection(name=collection_name)
        
        # Read all JSON files from the vectorized data directory
        for filename in os.listdir(vectorized_data_path):
            if filename.endswith('.json'):
                file_path = os.path.join(vectorized_data_path, filename)
                
                with open(file_path, 'r') as f:
                    data = json.load(f)
                    
                    # Extract the required components
                    documents = data.get('documents', [])
                    embeddings = data.get('embeddings', [])
                    metadata = data.get('metadata', [])
                    ids = data.get('ids', [])
                    
                    # Add vectors to the collection
                    collection.add(
                        documents=documents,
                        embeddings=embeddings,
                        metadatas=metadata,
                        ids=ids
                    )
        
        return collection

    def get_collection(self, collection_name: str = "documents") -> chromadb.Collection:
        """
        Get an existing collection from ChromaDB.
        
        Args:
            collection_name (str): Name of the collection to retrieve
            
        Returns:
            chromadb.Collection: The requested ChromaDB collection
        """
        return self.client.get_collection(name=collection_name)

    def delete_collection(self, collection_name: str = "documents") -> None:
        """
        Delete a collection from ChromaDB.
        
        Args:
            collection_name (str): Name of the collection to delete
        """
        self.client.delete_collection(name=collection_name)
```

This class provides the following functionality:

1. `__init__`: Initializes the ChromaDB client with a persistence directory
2. `load_vectorized_data`: Loads vectorized data from JSON files into a ChromaDB collection
3. `get_collection`: Retrieves an existing collection from ChromaDB
4. `delete_collection`: Deletes a collection from ChromaDB

You can use this class like this:

```python
# Example usage
loader = VectorStoreLoader(persist_directory="chroma_db")

# Load vectorized data into ChromaDB
collection = loader.load_vectorized_data(
    vectorized_data_path="vectorized_data",
    collection_name="my_documents"
)

# Later, you can retrieve the collection
collection = loader.get_collection("my_documents")

# If needed, delete the collection
loader.delete_collection("my_documents")
```

The class assumes that your vectorized data is stored in JSON files with the following structure:
```json
{
    "documents": [...],  // List of document texts
    "embeddings": [...], // List of vector embeddings
    "metadata": [...],   // List of metadata dictionaries
    "ids": [...]        // List of document IDs
}
```

Make sure your vectorized data follows this format for the loader to work correctly. Let me know if you need any modifications or have questions about the implementation!

---

_**User**_

@vectorized_data Check format to make sure that it matches loader logic

---

_**Assistant**_

I'll help you check if the JSON files in the vectorized_data folder match the expected format for the VectorStoreLoader class. The loader expects files to have this structure:

```json
{
    "documents": [...],  // List of document texts
    "embeddings": [...], // List of vector embeddings
    "metadata": [...],   // List of metadata dictionaries
    "ids": [...]        // List of document IDs
}
```

Looking at the files in the vectorized_data folder, I notice that they have a different structure. The files are organized by video_id and contain:

1. `*_metadata.json` - Contains video metadata
2. `*_patterns.json` - Contains question patterns
3. `*_questions.json` - Contains actual questions

Let me modify the VectorStoreLoader class to handle this structure:

```python:vector_store_loader.py
import chromadb
import os
import json
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
        self.client = chromadb.PersistentClient(path=persist_directory)

    def load_vectorized_data(self, 
                           vectorized_data_path: str,
                           collection_name: str = "documents") -> chromadb.Collection:
        """
        Load vectorized data from the specified directory into ChromaDB.
        
        Args:
            vectorized_data_path (str): Path to the directory containing vectorized data
            collection_name (str): Name of the collection to create/use in ChromaDB
            
        Returns:
            chromadb.Collection: The ChromaDB collection containing the loaded vectors
        """
        # Get or create collection
        collection = self.client.get_or_create_collection(name=collection_name)
        
        # Group related files by video_id
        file_groups = {}
        for filename in os.listdir(vectorized_data_path):
            if filename.endswith('.json'):
                video_id = filename.split('_')[0]
                if video_id not in file_groups:
                    file_groups[video_id] = []
                file_groups[video_id].append(filename)

        # Process each group of files
        for video_id, filenames in file_groups.items():
            metadata = {}
            patterns = []
            questions = []
            
            # Load data from each file
            for filename in filenames:
                file_path = os.path.join(vectorized_data_path, filename)
                with open(file_path, 'r') as f:
                    data = json.load(f)
                    
                if filename.endswith('_metadata.json'):
                    metadata = data
                elif filename.endswith('_patterns.json'):
                    patterns = data
                elif filename.endswith('_questions.json'):
                    questions = data

            # Process questions and patterns into documents
            documents = []
            metadatas = []
            ids = []
            
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
            if documents:
                collection.add(
                    documents=documents,
                    metadatas=metadatas,
                    ids=ids
                )
        
        return collection

    def get_collection(self, collection_name: str = "documents") -> chromadb.Collection:
        """
        Get an existing collection from ChromaDB.
        
        Args:
            collection_name (str): Name of the collection to retrieve
            
        Returns:
            chromadb.Collection: The requested ChromaDB collection
        """
        return self.client.get_collection(name=collection_name)

    def delete_collection(self, collection_name: str = "documents") -> None:
        """
        Delete a collection from ChromaDB.
        
        Args:
            collection_name (str): Name of the collection to delete
        """
        self.client.delete_collection(name=collection_name)
```

Key changes made:

1. Modified the loader to handle the specific file structure (metadata, patterns, questions)
2. Groups files by video_id to process related files together
3. Constructs meaningful document texts from the patterns and questions
4. Adds appropriate metadata for each document
5. Generates unique IDs for each document
6. Removed the embeddings parameter since ChromaDB will generate embeddings automatically

The loader now:
- Processes metadata, patterns and questions files for each video
- Creates document texts that combine relevant information
- Adds metadata to help with filtering and retrieval
- Uses ChromaDB's built-in embedding generation

You can use it like this:

```python
loader = VectorStoreLoader(persist_directory="chroma_db")
collection = loader.load_vectorized_data(
    vectorized_data_path="vectorized_data",
    collection_name="jlpt_questions"
)
```

Let me know if you'd like any adjustments to how the documents are structured or what metadata is included!

---

_**User**_

@vector_store_loader.py 
Doest it actually persist data within ChromaDB

---

_**Assistant**_

Yes, the code does persist data within ChromaDB through several mechanisms:

1. We use `chromadb.PersistentClient` instead of the in-memory client:
```python
self.client = chromadb.PersistentClient(path=persist_directory)
```
This ensures ChromaDB stores data on disk in the specified `persist_directory` rather than just in memory.

2. The `get_or_create_collection` method creates a persistent collection:
```python
collection = self.client.get_or_create_collection(name=collection_name)
```

3. When we add documents using `collection.add()`, ChromaDB automatically:
- Generates and stores embeddings for the documents
- Persists the documents, metadata, and IDs
- Saves everything to disk in the persist_directory

However, we could add some error handling and logging to make the persistence more robust:

```python:vector_store_loader.py
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
                documents = []
                metadatas = []
                ids = []
                
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
```

Key improvements for persistence:

1. Added directory creation: `os.makedirs(persist_directory, exist_ok=True)`
2. Added batch processing to handle large datasets more reliably
3. Added comprehensive error handling and logging
4. Added progress tracking for document loading
5. Added verification that data is properly loaded through logging

The data will be persisted in the specified `persist_directory` and will remain available even after the application restarts. You can verify the persistence by:

1. Loading data into a collection
2. Stopping your application
3. Restarting and using `get_collection()` to retrieve the previously loaded data

---

_**User**_

How I can connect manually to ChromaDB and see its content?

---

_**Assistant**_

I'll show you how to connect to ChromaDB and inspect its contents using Python. Here's a simple script you can use:

```python
import chromadb
from pprint import pprint

def inspect_chroma_db(persist_directory: str = "chroma_db", collection_name: str = "documents"):
    """
    Connect to ChromaDB and display collection contents
    """
    # Connect to the persistent ChromaDB instance
    client = chromadb.PersistentClient(path=persist_directory)
    
    try:
        # Get the collection
        collection = client.get_collection(collection_name)
        
        # Get collection stats
        print(f"\n=== Collection: {collection_name} ===")
        count = collection.count()
        print(f"Total documents: {count}")
        
        # Get all documents with their metadata
        result = collection.get(
            include=['documents', 'metadatas', 'embeddings', 'ids']
        )
        
        # Print document details
        print("\n=== Sample Documents ===")
        for i, (doc, metadata, doc_id) in enumerate(zip(
            result['documents'], 
            result['metadatas'], 
            result['ids']
        )):
            print(f"\nDocument {i+1}:")
            print(f"ID: {doc_id}")
            print("Metadata:", metadata)
            print("Content:", doc[:200], "..." if len(doc) > 200 else "")
            
            if i >= 4:  # Show only first 5 documents
                print("\n... (more documents available)")
                break
                
        # Show available collections
        print("\n=== Available Collections ===")
        collections = client.list_collections()
        for coll in collections:
            print(f"- {coll.name}")
            
    except Exception as e:
        print(f"Error accessing ChromaDB: {str(e)}")

if __name__ == "__main__":
    # Use this to inspect your ChromaDB contents
    inspect_chroma_db()
```

You can save this as `inspect_chroma.py` and run it to see the contents of your ChromaDB. You can also use it interactively in a Python shell:

```python
# Interactive usage example
from vector_store_loader import VectorStoreLoader
from inspect_chroma import inspect_chroma_db

# First load some data (if you haven't already)
loader = VectorStoreLoader(persist_directory="chroma_db")
loader.load_vectorized_data("vectorized_data", "jlpt_questions")

# Then inspect the contents
inspect_chroma_db(persist_directory="chroma_db", collection_name="jlpt_questions")

# You can also query specific documents
client = chromadb.PersistentClient(path="chroma_db")
collection = client.get_collection("jlpt_questions")

# Query by content
results = collection.query(
    query_texts=["JLPT N5 Listening"],
    n_results=2
)
pprint(results)

# Query by metadata
results = collection.get(
    where={"content_type": "question"}
)
pprint(results)
```

Some useful queries you can try:

1. Get documents by content type:
```python
results = collection.get(
    where={"content_type": "pattern"}  # or "question"
)
```

2. Get documents for a specific video:
```python
results = collection.get(
    where={"video_id": "specific_video_id"}
)
```

3. Search similar documents:
```python
results = collection.query(
    query_texts=["your search text here"],
    n_results=5
)
```

4. Get documents by topic:
```python
results = collection.get(
    where={"topic": "JLPT N5 Listening"}
)
```

5. Combine multiple filters:
```python
results = collection.get(
    where={
        "content_type": "question",
        "topic": "JLPT N5 Listening"
    }
)
```

Remember that ChromaDB stores the data in the `persist_directory` you specified when creating the `VectorStoreLoader`. Make sure you're pointing to the correct directory when inspecting the database.

---

_**User**_

Is there some CLI tool to check content of ChromaDB?

---

_**Assistant**_



ChromaDB doesn't provide an official CLI tool, but I can help you create a simple CLI script to inspect ChromaDB contents:

```python:chroma_cli.py
import chromadb
import argparse
import json
from typing import Optional, List
from tabulate import tabulate
import sys

def format_document(doc: str, max_length: int = 100) -> str:
    """Format document text for display"""
    if len(doc) > max_length:
        return doc[:max_length] + "..."
    return doc

def list_collections(client: chromadb.PersistentClient):
    """List all collections in the database"""
    collections = client.list_collections()
    if not collections:
        print("No collections found")
        return
    
    table_data = []
    for coll in collections:
        count = coll.count()
        table_data.append([coll.name, count])
    
    print(tabulate(table_data, headers=["Collection Name", "Document Count"], tablefmt="grid"))

def show_collection(client: chromadb.PersistentClient, collection_name: str, limit: Optional[int] = None):
    """Show contents of a specific collection"""
    try:
        collection = client.get_collection(collection_name)
        result = collection.get(
            include=['documents', 'metadatas', 'ids'],
            limit=limit
        )
        
        docs = result['documents']
        metas = result['metadatas']
        ids = result['ids']
        
        table_data = []
        for doc, meta, id in zip(docs, metas, ids):
            table_data.append([
                id[:10] + "...",
                json.dumps(meta, indent=2),
                format_document(doc)
            ])
        
        print(tabulate(table_data, headers=["ID", "Metadata", "Content"], tablefmt="grid"))
        
    except Exception as e:
        print(f"Error: {str(e)}")

def main():
    parser = argparse.ArgumentParser(description='ChromaDB CLI Tool')
    parser.add_argument('--path', default='chroma_db', help='Path to ChromaDB directory')
    
    subparsers = parser.add_subparsers(dest='command', help='Commands')
    
    # List collections command
    list_parser = subparsers.add_parser('list', help='List all collections')
    
    # Show collection command
    show_parser = subparsers.add_parser('show', help='Show collection contents')
    show_parser.add_argument('collection', help='Collection name')
    show_parser.add_argument('--limit', type=int, help='Limit number of documents shown')
    
    args = parser.parse_args()
    
    try:
        client = chromadb.PersistentClient(path=args.path)
        
        if args.command == 'list':
            list_collections(client)
        elif args.command == 'show':
            show_collection(client, args.collection, args.limit)
        else:
            parser.print_help()
            
    except Exception as e:
        print(f"Error connecting to ChromaDB: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```

To use this CLI tool, first install the required package:

```bash
pip install tabulate
```

Then you can use it like this:

```bash
# List all collections
python chroma_cli.py list

# Show contents of a specific collection
python chroma_cli.py show jlpt_questions

# Show limited number of documents from a collection
python chroma_cli.py show jlpt_questions --limit 5

# Specify a different ChromaDB path
python chroma_cli.py --path /path/to/chroma_db list
```

Example output:
```
# List collections:
+----------------+----------------+
| Collection Name| Document Count |
+----------------+----------------+
| jlpt_questions |      156      |
+----------------+----------------+

# Show collection:
+------------+----------------------+------------------+
| ID         | Metadata            | Content          |
+------------+----------------------+------------------+
| question_1...| {"video_id": "...", | Video: ABC123... |
+------------+----------------------+------------------+
```

This provides a simple way to inspect your ChromaDB contents from the command line. Let me know if you'd like any additional features or modifications!

---



---

