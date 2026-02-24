from google import genai
import os
from services.retriever import retrieve_context

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

@router.post("/query")
async def query_text(data: QueryInput):

    retrieved_chunks = retrieve_context(data.question)
    context = "\n\n".join(retrieved_chunks)

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

# import os
# from groq import Groq

# client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# def generate_answer(context, question):
#     prompt = f"""
#     You are a helpful study assistant.

#     Use the following text to answer the question.

#     Text:
#     {context}

#     Question:
#     {question}

#     Give a clear and concise answer.
#     """

#     response = client.chat.completions.create(
#         model="llama3-8b-8192",
#         messages=[
#             {"role": "user", "content": prompt}
#         ],
#     )

#     return response.choices[0].message.content

# import os
# from groq import Groq

# client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# def generate_answer(question, context):
#     prompt = f"""
#     Answer the question using only the context below.

#     Context:
#     {context}

#     Question:
#     {question}

#     Answer:
#     """

#     response = client.chat.completions.create(
#         model="llama3-8b-8192",
#         messages=[
#             {"role": "user", "content": prompt}
#         ],
#     )

#     return response.choices[0].message.content



# import os
# from openai import OpenAI

# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# def generate_answer(question, context):
#     prompt = f"""
# You are a senior law professor helping LLB students prepare for exams.

# Use ONLY the provided context.

# Context:
# {context}

# Question:
# {question}

# Generate:
# 1. 5-mark answer
# 2. 10-mark answer
# 3. 15-mark answer
# 4. Important case laws
# 5. Repeated exam topics if visible
# """

#     response = client.chat.completions.create(
#         model="gpt-4o-mini",
#         messages=[{"role": "user", "content": prompt}],
#         temperature=0.3
#     )

#     return response.choices[0].message.content
