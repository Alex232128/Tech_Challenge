import os
import json
from app.scraping import raspar_dados_embrapa

def test_raspagem_e_fallback():
    # Executa a raspagem
    dados = raspar_dados_embrapa()

    # Verifica se os dados foram retornados corretamente
    assert isinstance(dados, dict)
    assert len(dados) > 0

    # Verifica se o fallback foi salvo corretamente
    caminho = "data/fallback.json"
    assert os.path.exists(caminho), "fallback.json não foi criado"

    with open(caminho, "r", encoding="utf-8") as f:
        fallback = json.load(f)

    assert fallback == dados, "O conteúdo do fallback.json não corresponde ao da raspagem"
