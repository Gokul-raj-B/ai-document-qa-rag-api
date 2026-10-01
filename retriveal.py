import chromadb

from embeddings import create_embeddings_for_chunks


# Connect to ChromaDB
chroma_client = chromadb.PersistentClient(
    path="../chroma_db"
)


# Get existing collection
collection = chroma_client.get_collection(
    name="documents"
)


# User question
question = "What is artificial intelligence?"


# Create embedding for the question
question_embedding = create_embeddings_for_chunks(
    [question]
)[0]


# Search ChromaDB using Gemini embedding
results = collection.query(
    query_embeddings=[question_embedding],
    n_results=3
)


print("Retrieved chunks:")

for chunk in results["documents"][0]:
    print("\n---")
    print(chunk)