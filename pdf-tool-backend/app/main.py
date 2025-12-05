# main.py
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from .services.pdf_service import split

origins = [
    "http://localhost:5173"
]

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

@app.post("/api/split")
async def split(file: UploadFile = File(...)):
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400,detail="Wrong file format")

    try:
        content = await file.read()
        result_buffer = split(content)
        return StreamingResponse(
            result_buffer,
            media_type="application/pdf",
            headers={"Content-Deposition": "attachment; filename=download.pdf"}
        )
    except Exception as e:
        print(e)
