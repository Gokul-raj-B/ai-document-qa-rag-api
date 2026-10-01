import os
import chromadb
from dotenv import load_dotenv
from google import genai
from pdf_loader import extract_text_from_pdf
from chunking import split_text
from embeddings import create_embeddings_for_chunks

# Load environment variables
load_dotenv()

# Gemini client
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

# ChromaDB client
chroma_client = chromadb.PersistentClient(
    path="C:/Users/Gokulraj/Desktop/intern/Ai_doc_rag/chroma_db"
)

# Create collection
collection = chroma_client.get_or_create_collection(
    name="documents"
)
print("Already stored:", collection.count())
# 1. Read PDF
text = extract_text_from_pdf(r"C:\Users\Gokulraj\Desktop\intern\Ai_doc_rag\documents\sample.pdf")

# 2. Split PDF into chunks
chunks = split_text(text)
print("Total chunks:", len(chunks))

# 3. Process chunks in batches
batch_size = 20

for i in range(0, len(chunks), batch_size):

    batch = chunks[i:i + batch_size]

    print(
        f"Processing chunks {i + 1} "
        f"to {min(i + batch_size, len(chunks))}..."
    )

    # Create embeddings for current batch
    embeddings = create_embeddings_for_chunks(batch)


    # Store in ChromaDB
    for j, embedding in enumerate(embeddings):

        chunk_index = i + j

        collection.add(
            ids=[str(chunk_index)],
            documents=[chunks[chunk_index]],
            embeddings=[embedding]
        )


print("\nCompleted!")

print(
    "Total documents stored:",
    collection.count()
)