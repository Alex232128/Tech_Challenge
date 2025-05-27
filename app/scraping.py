import requests
from bs4 import BeautifulSoup
import json
import os

def raspar_dados_embrapa():
    url = "http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_02"
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.content, "html.parser")
    tabelas = soup.find_all("table")

    resultados = {}
    for idx, tabela in enumerate(tabelas):
        linhas = []
        for tr in tabela.find_all("tr"):
            colunas = [td.get_text(strip=True) for td in tr.find_all(["td", "th"])]
            if colunas:
                linhas.append(colunas)
        resultados[f"tabela_{idx+1}"] = linhas

    # Salvando como fallback automático
    os.makedirs("data", exist_ok=True)
    with open("data/fallback.json", "w", encoding="utf-8") as f:
        json.dump(resultados, f, ensure_ascii=False, indent=2)

    return resultados
