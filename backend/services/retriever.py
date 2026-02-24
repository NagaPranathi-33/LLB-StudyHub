from sentence_transformers import SentenceTransformer

from vectorstore.chroma_client import collection

model = SentenceTransformer("all-MiniLM-L6-v2")


def retrieve_context(question, n_results=5):
    q_embedding = model.encode([question]).tolist()

    results = collection.query(query_embeddings=q_embedding, n_results=n_results)

    documents = results.get("documents", [])
    if not documents:
        return []

    return documents[0] if documents[0] else []
