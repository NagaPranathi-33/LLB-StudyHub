from fastapi import APIRouter
from pydantic import BaseModel
from google import genai
import os
from services.retriever import retrieve_context  # adjust path if needed

router = APIRouter()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

class QueryInput(BaseModel):
    question: str

@router.post("/query")
async def query_text(data: QueryInput):
    try:
        # Retrieve relevant chunks
        chunks = retrieve_context(data.question)
        context = "\n\n".join(chunks)

        prompt = f"""
You are a legal assistant.

Use ONLY the context below to answer the question.

Context:
{context}

Question:
{data.question}
"""

        response = client.models.generate_content(
            model="gemini-1.5-flash",
            contents=prompt
        )

        return {"answer": response.text}

    except Exception as e:
        print("ERROR:", e)
        return {"error": str(e)}




# from fastapi import APIRouter
# from pydantic import BaseModel
# import google.generativeai as genai
# import os

# router = APIRouter()

# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# model = genai.GenerativeModel("gemini-3-flash-preview")

# class QueryInput(BaseModel):
#     question: str

# @router.post("/query")
# async def query_text(data: QueryInput):
#     try:
#         response = model.generate_content(data.question)
#         return {"answer": response.text}
#     except Exception as e:
#         print("ERROR:", e)
#         return {"error": str(e)}




# from fastapi import APIRouter
# from pydantic import BaseModel
# from groq import Groq
# import os

# router = APIRouter()

# client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# class QueryInput(BaseModel):
#     question: str

# @router.post("/query")
# async def query_text(data: QueryInput):
#     completion = client.chat.completions.create(
#         model="llama-3.1-8b-instant",
#         messages=[
#             {"role": "system", "content": "You are a helpful legal assistant."},
#             {"role": "user", "content": data.question}
#         ]
#     )

#     answer = completion.choices[0].message.content

#     return {"answer": answer}




# from fastapi import APIRouter
# from pydantic import BaseModel

# router = APIRouter()

# class QueryInput(BaseModel):
#     question: str

# @router.post("/query")
# async def query_text(data: QueryInput):
#     # Dummy response for now
#     return {
#         "answer": f"You asked: {data.question}"
#     }




# from fastapi import APIRouter
# from pydantic import BaseModel
# from services.generator import generate_answer

# router = APIRouter()

# class QueryRequest(BaseModel):
#     text: str
#     question: str

# @router.post("/query")
# def query(data: QueryRequest):
#     try:
#         answer = generate_answer(data.text, data.question)
#         return {"answer": answer}
#     except Exception as e:
#         return {"error": str(e)}


# from fastapi import APIRouter
# from pydantic import BaseModel
# from services.generator import generate_answer

# router = APIRouter()

# class QueryRequest(BaseModel):
#     text: str
#     question: str

# @router.post("/query")
# def query(data: QueryRequest):
#     answer = generate_answer(data.text, data.question)
#     return {"answer": answer}


# from fastapi import APIRouter
# from pydantic import BaseModel

# from services.retriever import retrieve_context
# from services.generator import generate_answer

# router = APIRouter()

# class QueryRequest(BaseModel):
#     question: str

# @router.post("/query")
# def query_llb(data: QueryRequest):
#     context = retrieve_context(data.question)
#     answer = generate_answer(data.question, context)
#     return {"answer": answer}
