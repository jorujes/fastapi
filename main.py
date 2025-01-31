from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class FormData(BaseModel):
    discipline: str
    text_type: str
    theme: str
    total_pages: str
    reference_format: str

@app.post("/receber-form")
async def receber_form(data: FormData):
    print("Dados recebidos:", data.dict())  # Isso aparecerá nos logs do Railway
    return {"status": "sucesso", "dados": data}