from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.upload import router as upload_router
from routes.query import router as query_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(upload_router, prefix="/api")
app.include_router(query_router, prefix="/api")

@app.get("/")
def root():
    return {"message": "Backend running"}


# from dotenv import load_dotenv
# load_dotenv()

# from fastapi import FastAPI
# from routes import upload, query

# app = FastAPI()

# #app.include_router(upload.router, prefix="/api")
# app.include_router(query.router, prefix="/api")

# @app.get("/")
# def root():
#     return {"message": "LLB Study Hub API Running"}
