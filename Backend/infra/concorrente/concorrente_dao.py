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
model_name = "concorrente"


# Query que lista tudo da tabela
def listar():
    with str_conn as conn:
        with conn.cursor() as cursor:
            cursor.execute(f"SELECT * FROM {model_name}")
            rows = cursor.fetchall()
            registros = []
            for (id_concorrente, codigo_concorrente, descricao_concorrente,
                 empresa_concorrente, observacao_concorrente) in rows:
                registros.append(
                    {"id_concorrente": id_concorrente, "codigo_concorrente": codigo_concorrente,
                     "descricao_concorrente": descricao_concorrente, "empresa_concorrente": empresa_concorrente,
                     "observacao_concorrente": observacao_concorrente})
            return registros


# Query que consulta por ID a tabela
def consultar(id):
    with str_conn as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                f"SELECT * FROM {model_name} WHERE id_concorrente = ?", (id,))
            row = cursor.fetchone()
            if row is None:
                return None
            return ({"id_concorrente": row[0], "codigo_concorrente": row[1],
                     "descricao_concorrente": row[2], "empresa_concorrente": row[3],
                     "observacao_concorrente": row[4]})


# Query que insere os dados na tabela
def cadastrar(concorrente):
    with str_conn as conn:
        with conn.cursor() as cursor:
            sql = f"INSERT INTO {model_name} (codigo_concorrente, descricao_concorrente, empresa_concorrente, observacao_concorrente) VALUES (?, ?, ?, ?)"
            cursor.execute(sql, (concorrente.codigo_concorrente, concorrente.descricao_concorrente,
                                 concorrente.empresa_concorrente, concorrente.observacao_concorrente))
            conn.commit()
            # conn.close()
            return concorrente.__dict__()


# Query que altera os dados na tabela
def alterar(concorrente):
    with str_conn as conn:
        with conn.cursor() as cursor:
            sql = f"UPDATE {model_name} SET codigo_concorrente = ?, descricao_concorrente = ?, empresa_concorrente = ?, observacao_concorrente = ? WHERE id_concorrente = ?"
            cursor.execute(sql, (concorrente["codigo_concorrente"], concorrente["descricao_concorrente"],
                                 concorrente["empresa_concorrente"], concorrente["observacao_concorrente"], concorrente["id"]))
            conn.commit()


# Query que remove os dados na tabela
def remover(concorrente):
    with str_conn as conn:
        with conn.cursor() as cursor:
            sql = f"DELETE FROM {model_name} WHERE id_concorrente = ?"
            cursor.execute(sql, concorrente["id_concorrente"])
            conn.commit()
