import psycopg2

# path / url de conexão
DB_PATH = "postgresql://neondb_owner:npg_m0ptxo7OaWAU@ep-orange-king-ahtsu5cn-pooler.c-3.us-east-1.aws.neon.tech/neondb?sslmode=require"

def get_connection():
    return psycopg2.connect(DB_PATH)