import os
import chromadb

from dotenv import load_dotenv
from google import genai

from embeddings import create_embeddings_for_chunks


load_dotenv()


# Gemini client
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


# Connect to ChromaDB
chroma_client = chromadb.PersistentClient(
    path="../chroma_db"
)

collection = chroma_client.get_collection(
    name="documents"
)


# User question
question = "What is supervised learning?"


# Create embedding for question
question_embedding = create_embeddings_for_chunks(
    [question]
)[0]


# Retrieve relevant chunks
results = collection.query(
    query_embeddings=[question_embedding],
    n_results=3
)


# Get retrieved text
retrieved_chunks = results["documents"][0]


# Combine chunks into one context
context = "\n\n".join(retrieved_chunks)


# Create prompt for Gemini
prompt = f"""
Answer the question using only the information provided in the context.

Context:
{context}

Question:
{question}

Answer:
"""


# Generate final answer
response = client.models.generate_content(
    model=os.getenv("GEMINI_MODEL"),
    contents=prompt
)


print("\n----- FINAL ANSWER -----")
print(response.text)