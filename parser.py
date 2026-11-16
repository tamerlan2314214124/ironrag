import fitz  # PyMuPDF
from fastapi import FastAPI, UploadFile, File
import shutil
import os

app = FastAPI(title="IronRAG Parser Engine", version="0.1.0")

@app.post("/parse")
async def parse_document(file: UploadFile = File(...)):
    temp_file_path = f"temp_{file.filename}"
    with open(temp_file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    doc = fitz.open(temp_file_path)
    structured_chunks = []
    
    for page_num in range(len(doc)):
        page = doc[page_num]
        blocks = page.get_text("blocks")
        
        for b_idx, block in enumerate(blocks):
            x0, y0, x1, y1, text, block_no, block_type = block
            cleaned_text = text.strip()
            if cleaned_text:
                structured_chunks.append({
                    "page": page_num + 1,
                    "block_id": b_idx,
                    "bbox": [x0, y0, x1, y1],
                    "text": cleaned_text
                })
                
    os.remove(temp_file_path)
    
    return {
        "filename": file.filename,
        "total_pages": len(doc),
        "chunks_extracted": len(structured_chunks),
        "chunks": structured_chunks
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
