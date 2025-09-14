import chromadb
import os
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction

class VectorStore:
    def __init__(self, persist_directory="./vector_db"):
        self.persist_directory = os.path.abspath(persist_directory)
        embedding_func = SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")

        # Check if persist directory exists to decide clearly
        if os.path.exists(self.persist_directory) and os.listdir(self.persist_directory):
            print("✅ Existing vector store found. Loading...")
        else:
            print("💾 No existing vector store. Creating new one...")
            os.makedirs(self.persist_directory, exist_ok=True)

        self.client = chromadb.PersistentClient(path=self.persist_directory)
        self.collection = self.client.get_or_create_collection(
            name="rag_collection",
            embedding_function=embedding_func
        )

    def add_chunks(self, chunks):
        existing_ids = set(self.collection.get(include=[])["ids"])
        
        documents, metadatas, ids = [], [], []
        for chunk in chunks:
            chunk_id = f"{chunk['doc']}_{chunk['chunk_id']}"
            if chunk_id not in existing_ids:
                documents.append(chunk['content'])
                metadatas.append({"source": chunk["doc"], "chunk_id": chunk["chunk_id"]})
                ids.append(chunk_id)

        if documents:
            self.collection.add(documents=documents, metadatas=metadatas, ids=ids)
            print(f"✅ Added {len(documents)} new chunks to vector store.")
        else:
            print("🚀 All chunks already exist in the vector store. Skipping addition.")

    def query(self, query_text, n_results=3):
        results = self.collection.query(query_texts=[query_text], n_results=n_results)
        return results
