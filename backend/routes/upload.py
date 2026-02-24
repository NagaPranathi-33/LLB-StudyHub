from fastapi import APIRouter, UploadFile, File
import PyPDF2
import io

router = APIRouter()

@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    contents = await file.read()

    pdf_reader = PyPDF2.PdfReader(io.BytesIO(contents))
    text = ""

    for page in pdf_reader.pages:
        text += page.extract_text() or ""

    return {
        "message": "PDF processed successfully",
        "length": len(text)
    }




# from fastapi import APIRouter
# from pydantic import BaseModel

# router = APIRouter()

# class TextInput(BaseModel):
#     content: str

# @router.post("/upload")
# async def upload_text(data: TextInput):
#     # For now just return what you received
#     return {
#         "message": "Text received successfully",
#         "length": len(data.content)
#     }




# from fastapi import APIRouter, UploadFile, File, HTTPException
# import shutil
# import os

# from services.pdf_parser import extract_text
# from services.chunker import chunk_text
# from services.embeddings import store_chunks

# router = APIRouter()

# UPLOAD_DIR = "uploads"
# os.makedirs(UPLOAD_DIR, exist_ok=True)

# @router.post("/upload")
# async def upload_pdf(file: UploadFile = File(...)):
#     file_path = os.path.join(UPLOAD_DIR, file.filename)

#     with open(file_path, "wb") as buffer:
#         shutil.copyfileobj(file.file, buffer)

#     text = extract_text(file_path)
#     chunks = chunk_text(text)
#     try:
#         store_chunks(chunks)
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))


#     return {"message": "PDF processed and stored successfully"}

