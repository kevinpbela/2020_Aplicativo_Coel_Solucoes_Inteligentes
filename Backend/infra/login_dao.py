import sqlite3
import pyodbc
from contextlib import closing
from model.login import Login


server = "coel.database.windows.net"
database = "Aplicativo"
username = "Adriano"
password = "Coelmatic01"
driver = '{ODBC Driver 17 for SQL Server}'

str_conn = pyodbc.connect('DRIVER='+driver+';SERVER='+server +
                          ';DATABASE='+database+';UID='+username+';PWD=' + password)

db_name = "login.db"
model_name = "login"


def con():
    return sqlite3.connect(db_name)


def listar():
    with str_conn as conn:
        with conn.cursor() as cursor:
            cursor.execute(f"SELECT * FROM {model_name}")
            rows = cursor.fetchall()
            registros = []
            for (id, nome, senha) in rows:
                registros.append(Login.criar({"id_usuario": id, "login": nome,
                                              "senha": senha}))
            return registros


def consultar(id_usuario):
    with str_conn as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                f"SELECT * FROM {model_name} WHERE id_usuario = ?", (int(id_usuario),))
            row = cursor.fetchone()
            if row is None:
                return None
            return Login.criar({"id_usuario": row[0], "login": row[1], "senha": row[2]})


def cadastrar(usuario):
    with str_conn as conn:
        with conn.cursor() as cursor:
            sql = f"INSERT INTO {model_name} (login, senha) VALUES (?, ?)"
            cursor.execute(sql, (usuario.login, usuario.senha))
            conn.commit()
            conn.close()

            # connection.commit()
            # if cursor.lastrowid:
            #     return login.__dict__()
            # else:
            #     return None
