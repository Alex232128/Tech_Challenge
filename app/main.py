from fastapi import FastAPI, APIRouter
from fastapi.responses import JSONResponse
import json
from app.scraping import raspar_dados_embrapa
from app.fallback import carregar_fallback

app = FastAPI(title="API Vitivinicultura - Embrapa", version="1.0.0")

router = APIRouter()

@router.get("/dados", summary="Retorna os dados da vitivinicultura da Embrapa")
def get_dados():
    try:
        dados = raspar_dados_embrapa()
        return JSONResponse(content=dados)
    except Exception as e:
        fallback = carregar_fallback()
        return JSONResponse(content=fallback, status_code=206)

app.include_router(router, prefix="/api/v1")

@app.get("/")
def root():
    return {"message": "API pública de dados da vitivinicultura da Embrapa"}
