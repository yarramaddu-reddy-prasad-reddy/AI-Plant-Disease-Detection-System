import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://neondb_owner:npg_SIwKy2pJHv0Q@ep-late-block-ax6yhxgu-pooler.c-4.us-east-2.aws.neon.tech/neondb?sslmode=require&channel_binding=require"
)


def get_connection():
    return psycopg2.connect(DATABASE_URL)