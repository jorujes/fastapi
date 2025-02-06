import subprocess
from fastapi import FastAPI
from pydantic import BaseModel
from process import executar_processo_completo  # Importando nossa função do process.py

app = FastAPI()

class FormData(BaseModel):
    discipline: str
    text_type: str
    theme: str
    total_pages: int
    reference_format: str

@app.post("/receber-form")
async def receber_form(data: FormData):
    print("📥 Dados recebidos:", data.dict())  # Logs no Railway
    
    # Chama o processo completo para gerar o índice
    indice = executar_processo_completo(
        data.discipline,
        data.theme,
        data.text_type,
        data.total_pages
    )
    
    return {"status": "sucesso", "dados_recebidos": data, "indice_gerado": indice}

@app.get("/installed-packages")
def list_installed_packages():
    installed_packages = subprocess.check_output(["pip", "freeze"]).decode("utf-8")
    return {"installed_packages": installed_packages.split("\n")}
