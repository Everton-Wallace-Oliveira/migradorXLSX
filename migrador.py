import pandas as pd
import json
from pymongo import MongoClient
from dotenv import load_dotenv

MONGO_URI = os.getenv("MONGO_URI")
DATABASE_NAME = os.getenv("DATABASE_NAME")
COLLECTION_NAME = os.getenv("COLLECTION_NAME")

with open("dicionario.json", "r", encoding="utf-8") as f:
    MAPEAMENTO_VALORES = json.load(f)

def transformar_excel_por_mapeamento(data, MAPEAMENTO_VALORES):
    try:
        for coluna in data.columns:
            if coluna in MAPEAMENTO_VALORES:
                print(f"Aplicando mapeamento para a coluna: {coluna}")
                data[coluna] = data[coluna].astype(str).map(MAPEAMENTO_VALORES[coluna]).fillna(data[coluna])
        return data
    except Exception as e:
        print(f"Erro ao transformar os dados: {e}")
        return data