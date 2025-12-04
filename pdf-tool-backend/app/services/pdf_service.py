#pdf_service.py
from pypdf import PdfReader, PdfWriter
import io

def say_hi(file_bytes: bytes):
    input_stream = io.BytesIO(file_bytes)
    
    reader = PdfReader(input_stream)
    writer = PdfWriter()

    for i in range(3):
        writer.add_page(reader.pages[i])

    output_buffer=io.BytesIO()
    writer.write(output_buffer)
    output_buffer.seek(0)

    return output_buffer