# Imports
import sqlite3
import pyodbc
from contextlib import closing
from model.usuario import Usuario

# String de conexão com Banco
server = "coel.database.windows.net"
database = "Aplicativo"
username = "Adriano"
password = "Coelmatic01"
driver = '{SQL Server}'

str_conn = pyodbc.connect('DRIVER='+driver+';SERVER='+server +
                          ';DATABASE='+database+';UID='+username+';PWD=' + password)

# Tabela
model_name = "usuario"


# Query que lista tudo da tabela
def listar():
    with str_conn as conn:
        with conn.cursor() as cursor:
            cursor.execute(f"SELECT * FROM {model_name}")
            rows = cursor.fetchall()
            registros = []
            for (id_usuario, login, senha) in rows:
                registros.append(
                    {"id_usuario": id_usuario, "login": login, "senha": senha})
            return registros


# Query que consulta por ID a tabela
def consultar(login):
    with str_conn as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                f"SELECT * FROM {model_name} WHERE login = ?", (login,))
            row = cursor.fetchone()
            if row is None:
                return None
            return ({"id_usuario": row[0], "login": row[1], "senha": row[2]})


# Query que insere os dados na tabela
def cadastrar(usuario):
    with str_conn as conn:
        with conn.cursor() as cursor:
            sql = f"INSERT INTO {model_name} (login, senha) VALUES (?, ?)"
            cursor.execute(sql, (usuario.login, usuario.senha))
            conn.commit()
            # conn.close()
            return usuario.__dict__()
