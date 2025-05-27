import json

def carregar_fallback():
    with open("data/fallback.json", "r", encoding="utf-8") as f:
        return json.load(f)
