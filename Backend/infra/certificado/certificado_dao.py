# Imports
import sqlite3
import pyodbc
from contextlib import closing

# String de conexão com Banco
server = "coel.database.windows.net"
database = "Aplicativo"
username = "Adriano"
password = "Coelmatic01"
driver = '{SQL Server}'

str_conn = pyodbc.connect('DRIVER='+driver+';SERVER='+server +
                          ';DATABASE='+database+';UID='+username+';PWD=' + password)

# Tabela
model_name = "certificado"


# Query que lista tudo da tabela
def listar():
    with str_conn as conn:
        with conn.cursor() as cursor:
            cursor.execute(f"SELECT * FROM {model_name}")
            rows = cursor.fetchall()
            registros = []
            for (id_certificado, certificado) in rows:
                registros.append(
                    {"id_certificado": id_certificado, "certificado": certificado})
            return registros


# Query que consulta por ID a tabela
def consultar(id):
    with str_conn as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                f"SELECT * FROM {model_name} WHERE id_certificado = ?", (id,))
            row = cursor.fetchone()
            if row is None:
                return None
            return ({"id_certificado": row[0], "certificado": row[1]})
