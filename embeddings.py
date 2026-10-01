import os
from dotenv import load_dotenv
from google import genai

'''load_dotenv()
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def create_embedding(text: str):
    response = client.models.embed_content(
        model="gemini-embedding-001",
        contents=text
    )
    return response.embeddings[0].values


def create_embeddings_for_chunks(chunks):
    embeddings = []
    for i, chunk in enumerate(chunks):
        embedding = create_embedding(chunk)
        embeddings.append(embedding)
    return embeddings'''



load_dotenv()


client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def create_embeddings_for_chunks(chunks):

    response = client.models.embed_content(
        model="gemini-embedding-001",
        contents=chunks
    )

    embeddings = []

    for embedding in response.embeddings:

        embeddings.append(embedding.values)

    return embeddings