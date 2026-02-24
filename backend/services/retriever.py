from sentence_transformers import SentenceTransformer
from db.chroma_client import collection

model = SentenceTransformer("all-MiniLM-L6-v2")

def retrieve_context(question):
    q_embedding = model.encode([question]).tolist()

    results = collection.query(
        query_embeddings=q_embedding,
        n_results=5
    )

    return results["documents"][0]



# import os
# from openai import OpenAI
# from db.chroma_client import collection

# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# def retrieve_context(question):
#     q_embedding = client.embeddings.create(
#         model="text-embedding-3-small",
#         input=question
#     ).data[0].embedding

#     results = collection.query(
#         query_embeddings=[q_embedding],
#         n_results=5
#     )

#     return results["documents"][0]
