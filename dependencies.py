import psycopg
from dotenv import load_dotenv
import os
from contextlib import contextmanager

load_dotenv()

DATABASE = os.getenv("DATABASE")
HOST = os.getenv("HOST")
USERDB = os.getenv("USERDB")
PASSWORD = os.getenv("PASSWORD")
PORT = os.getenv("PORT")

@contextmanager
def instance_cursor():
    connection = psycopg.connect(
        dbname = DATABASE,
        host = HOST,
        user = USERDB,
        password = PASSWORD,
        port = PORT)
    cursor = connection.cursor()
    try:
        # Explicação do decorador '@contextmanager' + 'yield':  Entregue o cursor para quem chamou o with, mas pause a função aqui. Quando o with terminar, continue a execução a partir daqui."
        yield cursor
    finally:
        if(connection):
            cursor.close()
            connection.close()
            print("Conexão com PostgreSQL fechada.")

def consulta_geral():
    with instance_cursor() as cursor:
        query =  '''
            SELECT 
                * 
            FROM
                REGISTROS
                '''
        cursor.execute(query)
        # O retorno de toda a consulta irá para a variável 'request'
        request = cursor.fetchall()
        return request

def consulta_username(user):
    with instance_cursor() as cursor:
        query =  '''
            SELECT 
                nome, usuario, senha
            FROM
                REGISTROS
            WHERE
                usuario = %s
                '''
        cursor.execute(query, (user,))
        request = cursor.fetchall()
        return request

def cria_tabela():
    # Como essa função usa commit, não usarei a função instance_cursor() 
    connection = psycopg.connect(
        dbname = DATABASE,
        host = HOST,
        user = USERDB,
        password = PASSWORD,
        port = PORT)
    cursor = connection.cursor()

    query =  '''
      CREATE TABLE REGISTROS (
         nome varchar(255),
         usuario varchar(255),
         senha varchar(255)
        )
            '''
    
    cursor.execute(query)
    connection.commit()

    if(connection):
        cursor.close()
        connection.close()
        print("Conexão com PostgreSQL fechada.")

def add_registro(nome, user, senha):
    connection = psycopg.connect(
        dbname=DATABASE,
        host=HOST,
        user=USERDB,
        password=PASSWORD,
        port=PORT
    )

    cursor = connection.cursor()

    query = '''
        INSERT INTO REGISTROS (nome, usuario, senha)
        VALUES (%s, %s, %s)
    '''

    cursor.execute(query, (nome, user, senha))

    connection.commit()

    cursor.close()
    connection.close()

    print("Conexão com PostgreSQL fechada.")


    
   