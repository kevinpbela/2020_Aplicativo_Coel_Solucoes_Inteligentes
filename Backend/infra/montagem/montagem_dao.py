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

model_name = "montagem"


def listar():
    with str_conn as conn:
        with conn.cursor() as cursor:
            cursor.execute(f"SELECT * FROM {model_name}")
            rows = cursor.fetchall()
            registros = []
            for (id_montagem, montagem) in rows:
                registros.append(
                    {"id_montagem": id_montagem, "montagem": montagem})
            return registros


def consultar(id):
    with str_conn as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                f"SELECT * FROM {model_name} WHERE id_montagem = ?", (id,))
            row = cursor.fetchone()
            if row is None:
                return None
            return ({"id_montagem": row[0], "montagem": row[1]})
