import sqlite3
import pyodbc
from contextlib import closing
from model.parametros import Parametros


server = "coel.database.windows.net"
database = "Aplicativo"
username = "Adriano"
password = "Coelmatic01"
driver = '{SQL Server}'

str_conn = pyodbc.connect('DRIVER='+driver+';SERVER='+server +
                          ';DATABASE='+database+';UID='+username+';PWD=' + password)

model_name = "parametros"


def listar():
    with str_conn as conn:
        with conn.cursor() as cursor:
            cursor.execute(f"SELECT * FROM {model_name}")
            rows = cursor.fetchall()
            registros = []
            for (id_parametros, tab_de_alarmes, tab_parametros, tab_parametros_dois, id_produto) in rows:
                registros.append(Parametros.criar({"id_parametros": id_parametros,
                                                   "tab_de_alarmes": tab_de_alarmes,
                                                   "tab_parametros": tab_parametros,
                                                   "tab_parametros_dois": tab_parametros_dois,
                                                   "id_produto": id_produto}))
            return registros


def consultar(id):
    with str_conn as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                f"SELECT * FROM {model_name} WHERE id_parametros = ?", (int(id),))
            row = cursor.fetchone()
            if row is None:
                return None
            return Parametros.criar({"id_parametros": row[0],
                                     "tab_de_alarmes": row[1],
                                     "tab_parametros": row[2],
                                     "tab_parametros_dois": row[3],
                                     "id_produto": row[4]})


def cadastrar(parametros):
    with str_conn as conn:
        with conn.cursor() as cursor:
            sql = f"INSERT INTO {model_name} (tab_de_alarmes, tab_parametros, tab_parametros_dois, id_produto VALUES (?, ?, ?, ?)"
            cursor.execute(sql, (parametros.tab_de_alarmes, parametros.tab_parametros, parametros.tab_parametros_dois,
                                 parametros.id_produto))
            conn.commit()
            conn.close()
            return parametros.__dict__()


def alterar(parametros):
    with str_conn as conn:
        with conn.cursor() as cursor:
            sql = f"UPDATE {model_name} SET id_parametros = ?, tab_de_alarmes = ?, tab_parametros = ?, tab_parametros_dois = ?, id_produto = ?"
            cursor.execute(sql, (parametros.id_parametros, parametros.tab_de_alarmes, parametros.tab_parametros, parametros.tab_parametros_dois,
                                 parametros.id_produto))
            conn.commit()


def remover(categoria):
    with str_conn as conn:
        with conn.cursor() as cursor:
            sql = f"DELETE FROM {model_name} WHERE id_parametros = ?"
            cursor.execute(sql, f"{categoria.id_produto}")
            conn.commit()
