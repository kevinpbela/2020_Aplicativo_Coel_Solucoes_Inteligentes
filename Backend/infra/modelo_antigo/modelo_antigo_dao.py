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
model_name = "modelo_antigo"


# Query que lista tudo da tabela
def listar():
    with str_conn as conn:
        with conn.cursor() as cursor:
            cursor.execute(f"SELECT * FROM {model_name}")
            rows = cursor.fetchall()
            registros = []
            for (id_modelo_antigo, descricao_modelo_antigo, modelo_antigo,
                 observacao_modelo_antigo, id_foto) in rows:
                registros.append(
                    {"id_modelo_antigo": id_modelo_antigo, "descricao_modelo_antigo": descricao_modelo_antigo,
                     "modelo_antigo": modelo_antigo, "observacao_modelo_antigo": observacao_modelo_antigo,
                     "id_foto": id_foto})
            return registros


# Query que consulta por ID a tabela
def consultar(id):
    with str_conn as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                f"SELECT * FROM {model_name} WHERE id_modelo_antigo = ?", (id,))
            row = cursor.fetchone()
            if row is None:
                return None
            return ({"id_modelo_antigo": row[0], "descricao_modelo_antigo": row[1],
                     "modelo_antigo": row[2], "observacao_modelo_antigo": row[3],
                     "id_foto": row[4]})


# Query que insere os dados na tabela
def cadastrar(modelo_antigo):
    with str_conn as conn:
        with conn.cursor() as cursor:
            sql = f"INSERT INTO {model_name} (descricao_modelo_antigo, modelo_antigo, observacao_modelo_antigo, id_foto) VALUES (?, ?, ?, ?)"
            cursor.execute(sql, (modelo_antigo.descricao_modelo_antigo, modelo_antigo.modelo_antigo,
                                 modelo_antigo.observacao_modelo_antigo, modelo_antigo.id_foto))
            conn.commit()
            # conn.close()
            return modelo_antigo.__dict__()


# Query que altera os dados na tabela
def alterar(modelo_antigo):
    with str_conn as conn:
        with conn.cursor() as cursor:
            sql = f"UPDATE {model_name} SET descricao_modelo_antigo = ?, modelo_antigo = ?, observacao_modelo_antigo = ?, id_foto = ? WHERE id_modelo_antigo = ?"
            cursor.execute(sql, (modelo_antigo["descricao_modelo_antigo"], modelo_antigo["modelo_antigo"],
                                 modelo_antigo["observacao_modelo_antigo"], modelo_antigo["id_foto"], modelo_antigo["id"]))
            conn.commit()

# Query que remove os dados na tabela
def remover(modelo_antigo):
    with str_conn as conn:
        with conn.cursor() as cursor:
            sql = f"DELETE FROM {model_name} WHERE id_modelo_antigo = ?"
            cursor.execute(sql, modelo_antigo["id_modelo_antigo"])
            conn.commit()
