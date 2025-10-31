import psycopg2
import os

# path / url de conexão
DB_PATH = os.environ.get("DATABASE_URL")

def get_connection():
    return psycopg2.connect(DB_PATH)