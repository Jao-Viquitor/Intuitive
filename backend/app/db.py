import os
import psycopg2.extras

def get_db_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_DATABASE"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        cursor_factory=psycopg2.extras.RealDictCursor
    )

def carregar_consulta(nome_arquivo):
    caminho = os.path.join(os.path.dirname(__file__), f'../../db/{nome_arquivo}')
    with open(caminho, 'r', encoding='utf-8') as arquivo:
        return arquivo.read()