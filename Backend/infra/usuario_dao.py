import sqlite3
import pyodbc
from contextlib import closing
from model.usuario import Usuario


server = "coel.database.windows.net"
database = "Aplicativo"
username = "Adriano"
password = "Coelmatic01"
driver = '{ODBC Driver 17 for SQL Server}'

str_conn = pyodbc.connect('DRIVER='+driver+';SERVER='+server +
                          ';DATABASE='+database+';UID='+username+';PWD=' + password)

model_name = "usuario"


def listar():
    with str_conn as conn:
        with conn.cursor() as cursor:
            cursor.execute(f"SELECT * FROM {model_name}")
            rows = cursor.fetchall()
            registros = []
            for (id, email, login, nome, senha) in rows:
                registros.append(Usuario.criar({"id": id, "email": email, "login": login, "nome": nome,
                                                "senha": senha}))
            return registros


def consultar(id):
    with str_conn as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                f"SELECT * FROM {model_name} WHERE id = ?", (int(id),))
            row = cursor.fetchone()
            if row is None:
                return None
            return Usuario.criar({"id": row[0], "email": row[1], "login": row[2], "nome": row[3], "senha": row[4]})


def cadastrar(usuario):
    with str_conn as conn:
        with conn.cursor() as cursor:
            sql = f"INSERT INTO {model_name} (email, login, nome, senha) VALUES (?, ?, ?, ?)"
            cursor.execute(sql, (usuario.email, usuario.login,
                                 usuario.nome, usuario.senha))
            conn.commit()
            return usuario.__dict__()
            conn.close()
