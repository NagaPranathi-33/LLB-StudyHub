from functools import lru_cache
import os

from dotenv import load_dotenv
from fastapi import APIRouter, HTTPException
from google import genai
from pydantic import BaseModel

from services.retriever import retrieve_context

load_dotenv()
router = APIRouter()


@lru_cache(maxsize=1)
def get_genai_client() -> genai.Client:
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise RuntimeError(
            "GOOGLE_API_KEY is missing. Set it in your environment or .env file."
        )

    return genai.Client(api_key=api_key)


class QueryInput(BaseModel):
    question: str


@router.post("/query")
async def query_text(data: QueryInput):
    try:
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

        client = get_genai_client()
        response = client.models.generate_content(
            model="gemini-1.5-flash",
            contents=prompt,
        )

        return {"answer": response.text}

    except RuntimeError as error:
        raise HTTPException(status_code=500, detail=str(error)) from error
    except Exception as error:
        print("ERROR:", error)
        raise HTTPException(status_code=500, detail=str(error)) from error
