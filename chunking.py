from pdf_loader import extract_text_from_pdf

def split_text(text: str, chunk_size: int = 1000, overlap: int = 200):
    chunks = []

    start = 0

    while start < len(text):
        end = start + chunk_size

        chunk = text[start:end]

        if chunk.strip():
            chunks.append(chunk.strip())

        start += chunk_size - overlap
    
    #print("Total chunks:", len(chunks))

    '''for i, chunk in enumerate(chunks):
        print(f"\n--- Chunk {i + 1} ---")
        print(chunk)'''
    return chunks