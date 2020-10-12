import sqlite3
import pyodbc
from contextlib import closing

server = "coel.database.windows.net"
database = "Aplicativo"
username = "Adriano"
password = "Coelmatic01"
driver = '{SQL Server}'

str_conn = pyodbc.connect('DRIVER='+driver+';SERVER='+server +
                          ';DATABASE='+database+';UID='+username+';PWD=' + password)

model_name = "aplicacao_navegacao"


def listar():
    with str_conn as conn:
        with conn.cursor() as cursor:
            cursor.execute(f"SELECT * FROM {model_name}")
            rows = cursor.fetchall()
            registros = []
            for (id_aplicacao_navegacao, aplicacao_navegacao) in rows:
                registros.append(
                    {"id_aplicacao_navegacao": id_aplicacao_navegacao, "aplicacao_navegacao": aplicacao_navegacao})
            return registros


def consultar(id):
    with str_conn as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                f"SELECT * FROM {model_name} WHERE id_aplicacao_navegacao = ?", (id,))
            row = cursor.fetchone()
            if row is None:
                return None
            return ({"id_aplicacao_navegacao": row[0], "aplicacao_navegacao": row[1]})
