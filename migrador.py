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

def migrate_data(excel_file_path, output_csv_path):
    try:
        client = MongoClient(MONGO_URI)
        db = client[DATABASE_NAME]
        collection = db[COLLECTION_NAME]
        print("Conexão com MongoDB estabelecida com sucesso!")

        data = pd.read_excel(excel_file_path)
        print(f"Dados carregados com sucesso do arquivo: {excel_file_path}")

        data = transformar_excel_por_mapeamento(data, MAPEAMENTO_VALORES)

        data.to_csv(output_csv_path, index=False, encoding="utf-8")
        print(f"Arquivo CSV criado com sucesso: {output_csv_path}")

        data_dict = data.to_dict(orient="records")

        if data_dict:
            collection.insert_many(data_dict)
            print(f"{len(data_dict)} registros inseridos com sucesso no MongoDB!")
        else:
            print("Nenhum dado encontrado para migrar.")
    
    except Exception as e:
        print(f"Erro ao migrar os dados: {e}")
    finally:
        client.close()