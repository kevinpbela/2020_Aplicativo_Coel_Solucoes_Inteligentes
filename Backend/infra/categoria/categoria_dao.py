import sqlite3
import pyodbc
from contextlib import closing
from model.categoria import Categoria

server = "coel.database.windows.net"
database = "Aplicativo"
username = "Adriano"
password = "Coelmatic01"
driver = '{SQL Server}'

str_conn = pyodbc.connect('DRIVER='+driver+';SERVER='+server +
                          ';DATABASE='+database+';UID='+username+';PWD=' + password)

model_name = "categoria"


def listar():
    with str_conn as conn:
        with conn.cursor() as cursor:
            cursor.execute(f"SELECT * FROM {model_name}")
            rows = cursor.fetchall()
            registros = []
            for (id_categoria, categoria, sub_categoria_um, sub_categoria_dois, sub_categoria_tres, sub_categoria_quatro, id_produto) in rows:
                registros.append(Categoria.criar({"id_categoria": id_categoria, "categoria": categoria, "sub_categoria_um": sub_categoria_um,
                                                  "sub_categoria_dois": sub_categoria_dois, "sub_categoria_tres": sub_categoria_tres,
                                                  "sub_categoria_quatro": sub_categoria_quatro, "id_produto": id_produto}))
            return registros


def consultar(id):
    with str_conn as conn:
        with conn.cursor() as cursor:
            cursor.execute(f"SELECT * FROM {model_name} WHERE id_categoria = ?", (int(id),))
            row = cursor.fetchone()
            if row is None:
                return None
            return Categoria.criar({"id_categoria": row[0], "categoria": row[1], "sub_categoria_um": row[2],
                                    "sub_categoria_dois": row[3], "sub_categoria_tres": row[4], "sub_categoria_quatro": row[5],
                                    "id_produto": row[6]})


def cadastrar(categoria):
    with str_conn as conn:
        with conn.cursor() as cursor:
            sql = f"INSERT INTO {model_name} (categoria, sub_categoria_um, sub_categoria_dois, sub_categoria_tres, sub_categoria_quatro, id_produto VALUES (?, ?, ?, ?, ?, ?)"
            cursor.execute(sql, (categoria.categoria, categoria.sub_categoria_um, categoria.sub_categoria_dois,
                                 categoria.sub_categoria_tres, categoria.sub_categoria_quatro, categoria.id_produto))
            conn.commit()
            conn.close()
            return categoria.__dict__()


def alterar(categoria):
    with str_conn as conn:
        with conn.cursor() as cursor:
            sql = f"UPDATE {model_name} SET id_categoria = ?, categoria = ?, sub_categoria_um = ?, sub_categoria_dois = ?, sub_categoria_tres = ?, sub_categoria_quatro = ?, id_produto = ?"
            cursor.execute(sql, (categoria.id_categoria, categoria.categoria, categoria.sub_categoria_um, categoria.sub_categoria_dois,
                                 categoria.sub_categoria_tres, categoria.sub_categoria_quatro, categoria.id_produto))
            conn.commit()


def remover(categoria):
    with str_conn as conn:
        with conn.cursor() as cursor:
            sql = f"DELETE FROM {model_name} WHERE id_categoria = ?"
            cursor.execute(sql, f"{categoria.id_produto}")
            conn.commit()
