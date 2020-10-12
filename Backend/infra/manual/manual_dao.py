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

model_name = "manual"


def listar():
    with str_conn as conn:
        with conn.cursor() as cursor:
            cursor.execute(f"SELECT * FROM {model_name}")
            rows = cursor.fetchall()
            registros = []
            for (id_manual, link_manual, manual_idioma, manual_tipo, nome_manual) in rows:
                registros.append(
                    {"id_manual": id_manual, "link_manual": link_manual, "manual_idioma": manual_idioma,
                     "manual_tipo": manual_tipo, "nome_manual": nome_manual})
            return registros


def consultar(id):
    with str_conn as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                f"SELECT * FROM {model_name} WHERE id_manual = ?", (id,))
            row = cursor.fetchone()
            if row is None:
                return None
            return ({"id_manual": row[0], "link_manual": row[1], "manual_idioma": row[2],
                     "manual_tipo": row[3], "nome_manual": row[4]})
