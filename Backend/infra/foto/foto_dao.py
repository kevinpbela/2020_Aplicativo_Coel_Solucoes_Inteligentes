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

model_name = "foto"


def listar():
    with str_conn as conn:
        with conn.cursor() as cursor:
            cursor.execute(f"SELECT * FROM {model_name}")
            rows = cursor.fetchall()
            registros = []
            for (id_foto, foto) in rows:
                registros.append(
                    {"id_foto": id_foto, "foto": foto})
            return registros


def consultar(id):
    with str_conn as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                f"SELECT * FROM {model_name} WHERE id_foto = ?", (id,))
            row = cursor.fetchone()
            if row is None:
                return None
            return ({"id_foto": row[0], "foto": row[1]})
