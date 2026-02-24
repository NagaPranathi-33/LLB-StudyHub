from sentence_transformers import SentenceTransformer
from db.chroma_client import collection

model = SentenceTransformer("all-MiniLM-L6-v2")

def store_chunks(chunks):
    embeddings = model.encode(chunks).tolist()

    collection.add(
        documents=chunks,
        embeddings=embeddings,
        ids=[f"chunk_{i}" for i in range(len(chunks))]
    )



# import os
# from openai import OpenAI
# from dotenv import load_dotenv
# from db.chroma_client import collection

# # Load environment variables from .env
# load_dotenv()

# # Now safely read the key
# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# def store_chunks(chunks):
#     embeddings = client.embeddings.create(
#         model="text-embedding-3-small",
#         input=chunks   # send entire list at once
#     )

#     vectors = [item.embedding for item in embeddings.data]

#     collection.add(
#         documents=chunks,
#         embeddings=vectors,
#         ids=[f"chunk_{i}" for i in range(len(chunks))]
#     )

