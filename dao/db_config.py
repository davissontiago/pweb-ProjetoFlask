import psycopg2
import os
from psycopg2 import OperationalError 

# path / url de conexão
DB_PATH = os.environ.get("DATABASE_URL")

def get_connection():
    if not DB_PATH:
        raise ConnectionError("Variável de ambiente 'DATABASE_URL' não definida no ambiente de execução.")

    try:
        return psycopg2.connect(DB_PATH)
    except OperationalError as e:
        print(f"ERRO CRÍTICO DE CONEXÃO: {e}")
        raise ConnectionError("Falha na conexão com o banco de dados. Verifique logs do Vercel para detalhes.")