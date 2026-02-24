import io
import uuid

import PyPDF2
from fastapi import APIRouter, File, HTTPException, UploadFile

from services.chunker import chunk_text
from services.embeddings import store_chunks

router = APIRouter()


@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are supported")

    contents = await file.read()

    try:
        pdf_reader = PyPDF2.PdfReader(io.BytesIO(contents))
        text = ""

        for page in pdf_reader.pages:
            text += page.extract_text() or ""

        chunks = chunk_text(text)
        source_id = uuid.uuid4().hex
        stored_count = store_chunks(chunks, source_id)

        if stored_count == 0:
            raise HTTPException(
                status_code=400,
                detail="Could not extract readable text from PDF",
            )

        return {
            "message": "PDF processed and stored successfully",
            "length": len(text),
            "chunks_stored": stored_count,
            "source_id": source_id,
        }
    except HTTPException:
        raise
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error)) from error
