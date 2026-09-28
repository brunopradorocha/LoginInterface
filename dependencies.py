import psycopg2
from dotenv import load_dotenv
import os
from contextlib import contextmanager

load_dotenv()

DATABASE = os.getenv("DATABASE")
HOST = os.getenv("HOST")
PASSWORD = os.getenv("PASSWORD")
PORT = os.getenv("PORT")