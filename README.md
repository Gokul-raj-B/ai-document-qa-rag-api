# AI Document Q&A API

An AI-powered Document Question Answering API built using FastAPI, Google Gemini, embeddings, and ChromaDB.

The system reads information from a PDF document, divides the extracted text into chunks, converts the chunks into embeddings, stores them in ChromaDB, retrieves the most relevant information for a user's question, and uses Google Gemini to generate an answer based on the retrieved context.

## Architecture

PDF Document
↓
Text Extraction
↓
Text Chunking
↓
Embeddings
↓
ChromaDB Vector Database
↓
User Question
↓
Question Embedding
↓
Relevant Chunk Retrieval
↓
Gemini LLM
↓
Final Answer
↓
FastAPI JSON Response

## Technologies Used

* Python
* FastAPI
* Uvicorn
* Google Gemini API
* Gemini Embeddings
* ChromaDB
* PyMuPDF
* Pydantic
* python-dotenv

## Project Structure

```text
Ai_doc_rag/
├── app/
│   ├── __init__.py
│   ├── pdf_loader.py
│   ├── chunking.py
│   ├── embeddings.py
│   ├── vector.py
│   ├── retriveal.py
│   ├── rag.py
│   └── main.py
├── documents/
│   └── sample.pdf
├── chroma_db/
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

## How It Works

### 1. PDF Text Extraction

The PDF document is read using PyMuPDF and the text is extracted from each page.

### 2. Text Chunking

The extracted text is divided into smaller chunks so that relevant sections can be efficiently processed and retrieved.

### 3. Embeddings

Each text chunk is converted into a numerical vector using the Gemini embedding model.

### 4. Vector Database

The embeddings and corresponding text chunks are stored in ChromaDB.

### 5. Retrieval

When the user asks a question, the question is converted into an embedding.

ChromaDB compares the question embedding with the stored document embeddings and retrieves the most relevant chunks.

### 6. Generation

The retrieved chunks are provided as context to Google Gemini.

Gemini generates the final answer using the retrieved document information.

### 7. FastAPI

FastAPI provides the `/ask` API endpoint through which users can submit questions and receive AI-generated answers.

## API Endpoint

### POST `/ask`

Request:

```json
{
  "question": "What is supervised learning?"
}
```

Response:

```json
{
  "question": "What is supervised learning?",
  "answer": "..."
}
```

## Running the Project

### 1. Install dependencies

```powershell
uv pip install -r requirements.txt
```

### 2. Configure environment variables

Create a `.env` file:

```text
GEMINI_API_KEY=your_api_key_here
GEMINI_MODEL=your_model_name
```

Do not upload the `.env` file to GitHub.

### 3. Start the FastAPI server

Go to the `app` folder:

```powershell
cd app
```

Run:

```powershell
uv run uvicorn main:app --reload
```

### 4. Open Swagger UI

Open the FastAPI documentation in your browser and use the `/ask` endpoint to ask questions about the document.

## Features

* PDF document processing
* Text chunking
* Gemini embeddings
* ChromaDB vector storage
* Semantic retrieval
* Retrieval-Augmented Generation (RAG)
* Google Gemini based answer generation
* FastAPI REST API
* Swagger API documentation

## Future Improvements

* Support multiple PDF documents
* Add PDF upload API
* Store page numbers as metadata
* Improve chunking strategy
* Add authentication
* Add conversation history
* Add source references in API responses
* Deploy the API to the cloud

## Author

Gokul Raj
