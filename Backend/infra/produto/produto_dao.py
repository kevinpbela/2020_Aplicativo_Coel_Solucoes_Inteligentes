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
model_name = "produto"


# Query que lista tudo da tabela
def listar():
    with str_conn as conn:
        with conn.cursor() as cursor:
            cursor.execute(f"SELECT * FROM {model_name}")
            rows = cursor.fetchall()
            registros = []
            for (id_produto, descricao_completa, descricao_reduzida, link_codigo_pedido,
                 link_dimensoes, link_esquema_ligacao, link_exemplo_ligacao,
                 link_site, link_tabela_alarmes, link_tabela_parametros, modelo,
                 status, id_alimentacao, id_aplicacao, id_aplicacao_navegacao,
                 id_categoria, id_categoria_venda, id_certificado, id_concorrente,
                 id_foto, id_funcao, id_manual, id_modelo_antigo, id_montagem) in rows:
                registros.append(
                    {"id_produto": id_produto, "descricao_completa": descricao_completa,
                     "descricao_reduzida": descricao_reduzida, "link_codigo_pedido": link_codigo_pedido,
                     "link_dimensoes": link_dimensoes, "link_esquema_ligacao": link_esquema_ligacao,
                     "link_exemplo_ligacao": link_exemplo_ligacao, "link_site": link_site,
                     "link_tabela_alarmes": link_tabela_alarmes, "link_tabela_parametros": link_tabela_parametros,
                     "modelo": modelo, "status": status, "id_alimentacao": id_alimentacao,
                     "id_aplicacao": id_aplicacao, "id_aplicacao_navegacao": id_aplicacao_navegacao,
                     "id_categoria": id_categoria, "id_categoria_venda": id_categoria_venda,
                     "id_certificado": id_certificado, "id_concorrente": id_concorrente,
                     "id_foto": id_foto, "id_funcao": id_funcao, "id_manual": id_manual,
                     "id_modelo_antigo": id_modelo_antigo, "id_montagem": id_montagem})
            return registros


# Query que consulta por ID a tabela
def consultar(id):
    with str_conn as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                f"SELECT * FROM {model_name} WHERE id_produto = ?", (id,))
            row = cursor.fetchone()
            if row is None:
                return None
            return ({"id_produto": row[0], "descricao_completa": row[1], "descricao_reduzida": row[2],
                     "link_codigo_pedido": row[3], "link_dimensoes": row[4], "link_esquema_ligacao": row[5],
                     "link_exemplo_ligacao": row[6], "link_site": row[7], "link_tabela_alarmes": row[8],
                     "link_tabela_parametros": row[9], "modelo": row[10], "status": row[11],
                     "id_alimentacao": row[12], "id_aplicacao": row[13], "id_aplicacao_navegacao": row[14],
                     "id_categoria": row[15], "id_categoria_venda": row[16], "id_certificado": row[17],
                     "id_concorrente": row[18], "id_foto": row[19], "id_funcao": row[20],
                     "id_manual": row[21], "id_modelo_antigo": row[22], "id_montagem": row[23]})


# Query que insere os dados na tabela
def cadastrar(produto):
    with str_conn as conn:
        with conn.cursor() as cursor:
            sql = f"INSERT INTO {model_name} (descricao_completa, descricao_reduzida, link_codigo_pedido, link_dimensoes, link_esquema_ligacao, link_exemplo_ligacao, link_site, link_tabela_alarmes, link_tabela_parametros, modelo, status, id_alimentacao, id_aplicacao, id_aplicacao_navegacao, id_categoria, id_categoria_venda, id_certificado, id_concorrente, id_foto, id_funcao, id_manual, id_modelo_antigo, id_montagem) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
            cursor.execute(sql, (produto.descricao_completa, produto.descricao_reduzida, produto.link_codigo_pedido,
                                 produto.link_dimensoes, produto.link_esquema_ligacao, produto.link_exemplo_ligacao,
                                 produto.link_site, produto.link_tabela_alarmes, produto.link_tabela_parametros,
                                 produto.modelo, produto.status, produto.id_alimentacao, produto.id_aplicacao,
                                 produto.id_aplicacao_navegacao, produto.id_categoria, produto.id_categoria_venda,
                                 produto.id_certificado, produto.id_concorrente, produto.id_foto, produto.id_funcao,
                                 produto.id_manual, produto.id_modelo_antigo, produto.id_montagem))
            conn.commit()
            # conn.close()
            return produto.__dict__()


# Query que altera os dados na tabela
def alterar(produto):
    with str_conn as conn:
        with conn.cursor() as cursor:
            sql = f"UPDATE {model_name} SET descricao_completa = ?, descricao_reduzida = ?, link_codigo_pedido = ?, link_dimensoes = ?, link_esquema_ligacao = ?, link_exemplo_ligacao = ?, link_site = ?, link_tabela_alarmes = ?, link_tabela_parametros = ?, modelo = ?, status = ?, id_alimentacao = ?, id_aplicacao = ?, id_aplicacao_navegacao = ?, id_categoria = ?, id_categoria_venda = ?, id_certificado = ?, id_concorrente = ?, id_foto = ?, id_funcao = ?, id_manual = ?, id_modelo_antigo = ?, id_montagem = ? WHERE id_produto = ?"
            cursor.execute(sql, (produto["descricao_completa"], produto["descricao_reduzida"], produto["link_codigo_pedido"],
                                 produto["link_dimensoes"], produto["link_esquema_ligacao"], produto["link_exemplo_ligacao"],
                                 produto["link_site"], produto["link_tabela_alarmes"], produto["link_tabela_parametros"],
                                 produto["modelo"], produto["status"], ["id_alimentacao"], produto["id_aplicacao"],
                                 produto["id_aplicacao_navegacao"], produto["id_categoria"], produto["id_categoria_venda"],
                                 produto["id_certificado"], produto["id_concorrente"], produto["id_foto"], produto["id_funcao"],
                                 produto["id_manual"], produto["id_modelo_antigo"], produto['id_montagem'],
                                 produto["id_produto"]))
            conn.commit()

# Query que remove os dados na tabela


def remover(produto):
    with str_conn as conn:
        with conn.cursor() as cursor:
            sql = f"DELETE FROM {model_name} WHERE id_produto = ?"
            cursor.execute(sql, produto["id_produto"])
            conn.commit()
