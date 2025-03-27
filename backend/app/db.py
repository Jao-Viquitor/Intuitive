import mysql.connector
import os

def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_DATABASE')
    )

def carregar_consulta(nome_arquivo):
    caminho = os.path.join(os.path.dirname(__file__), f'../../db/{nome_arquivo}')
    with open(caminho, 'r', encoding='utf-8') as arquivo:
        return arquivo.read()