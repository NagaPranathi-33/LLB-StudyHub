from sentence_transformers import SentenceTransformer

from vectorstore.chroma_client import collection

model = SentenceTransformer("all-MiniLM-L6-v2")


def store_chunks(chunks, source_id: str):
    if not chunks:
        return 0

    embeddings = model.encode(chunks).tolist()
    ids = [f"{source_id}_chunk_{i}" for i in range(len(chunks))]
    metadatas = [{"source_id": source_id, "chunk_index": i} for i in range(len(chunks))]

    collection.add(
        documents=chunks,
        embeddings=embeddings,
        ids=ids,
        metadatas=metadatas,
    )

    return len(chunks)
