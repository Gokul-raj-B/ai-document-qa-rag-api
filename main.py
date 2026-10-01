import os

import chromadb
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel
from google import genai

from embeddings import create_embeddings_for_chunks


load_dotenv()


app = FastAPI(
    title="AI Document Q&A API"
)


# Gemini client
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


# ChromaDB
chroma_client = chromadb.PersistentClient(
    path="C:/Users/Gokulraj/Desktop/intern/Ai_doc_rag/chroma_db"
)

collection = chroma_client.get_collection(
    name="documents"
)


# Request model
class Question(BaseModel):
    question: str


@app.get("/")
def home():
    return {"message": "AI Document Q&A API is running"}


@app.post("/ask")
def ask_question(data: Question):

    # User question
    question = data.question


    # Create embedding for question
    question_embedding = create_embeddings_for_chunks(
        [question]
    )[0]


    # Retrieve relevant chunks
    results = collection.query(
        query_embeddings=[question_embedding],
        n_results=3
    )


    # Get retrieved chunks
    retrieved_chunks = results["documents"][0]


    # Create context
    context = "\n\n".join(retrieved_chunks)


    # Prompt
    prompt = f"""
    Answer the question using only the information
    provided in the context.

    Context:
    {context}

    Question:
    {question}

    Answer:
    """


    # Gemini response
    response = client.models.generate_content(
        model=os.getenv("GEMINI_MODEL"),
        contents=prompt
    )


    return {
        "question": question,
        "answer": response.text
    }