# main.py
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import StreamingResponse
# Importiamo la logica come modulo! 
from .services.pdf_service import say_hi

app = FastAPI()

@app.post("/api/split")
async def split(file: UploadFile = File(...)):
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400,detail="Wrong file format")

    try:
        content = await file.read()
        result_buffer = say_hi(content)
        return StreamingResponse(
            result_buffer,
            media_type="application/pdf",
            headers={"Content-Deposition": "attachment; filename=download.pdf"}
        )
    except Exception as e:
        print(e)