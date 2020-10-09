import sqlite3
import pyodbc
from contextlib import closing
from model.produto import Produto


server = "coel.database.windows.net"
database = "Aplicativo"
username = "Adriano"
password = "Coelmatic01"
driver = '{SQL Server}'

str_conn = pyodbc.connect('DRIVER='+driver+';SERVER='+server +
                          ';DATABASE='+database+';UID='+username+';PWD=' + password)

model_name = "produto"


def listar():
    with str_conn as conn:
        with conn.cursor() as cursor:
            cursor.execute(f"SELECT * FROM {model_name}")
            rows = cursor.fetchall()
            registros = []
            for (id_produto, alimentacao, caracteristica, categoria_venda,
                    certificado, codigo_pedido, descricao_completa,
                    descricao_reduzida, fabricante, funcao,
                    id_categoria, modelo, montagem, status, tag, id_parametros,
                    id_equivalencia, id_historico, id_ligacoes) in rows:
                registros.append(Produto.criar({"id_produto": id_produto, "alimentacao": alimentacao, "caracteristica": caracteristica,
                                                "categoria_venda": categoria_venda, "certificado": certificado, "codigo_pedido": codigo_pedido,
                                                "descricao_completa": descricao_completa, "descricao_reduzida": descricao_reduzida,
                                                "fabricante": fabricante, "funcao": funcao, "id_categoria": id_categoria, "modelo": modelo,
                                                "montagem": montagem, "status": status, "tag": tag, "id_parametros": id_parametros,
                                                "id_equivalencia": id_equivalencia, "id_historico": id_historico, "id_ligacoes": id_ligacoes}))
            return registros


def consultar(id):
    with str_conn as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                f"SELECT * FROM {model_name} WHERE id = ?", (int(id),))
            row = cursor.fetchone()
            if row is None:
                return None
            return Produto.criar({"id_produto": row[0], "alimentacao": row[1], "caracteristica": row[2],
                                  "categoria_venda": row[3], "certificado": row[4], "codigo_pedido": row[5],
                                  "descricao_completa": row[6], "descricao_reduzida": row[7], "fabricante": row[8],
                                  "funcao": row[9], "id_categoria": row[10], "modelo": row[11], "montagem": row[12],
                                  "status": row[13], "tag": row[14], "id_parametros": row[15],
                                  "id_equivalencia": row[16], "id_historico": row[17], "id_ligacoes": row[18]})


def cadastrar(produto):
    with str_conn as conn:
        with conn.cursor() as cursor:
            sql = f"INSERT INTO {model_name} (alimentacao, caracteristica, categoria_venda, certificado, codigo_pedido, descricao_completa, descricao_reduzida, fabricante, funcao, id_categoria, modelo, montagem, status, tag, id_parametros, id_equivalencia, id_historico, id_ligacoes (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
            cursor.execute(sql, (produto.alimentacao, produto.caracteristica, produto.categoria_venda, produto.certificado,
                                 produto.codigo_pedido, produto.descricao_completa, produto.descricao_reduzida,
                                 produto.fabricante, produto.funcao, produto.id_categoria, produto.modelo, produto.montagem,
                                 produto.status, produto.tag, produto.id_parametros,
                                 produto.id_equivalencia, produto.id_historico, produto.id_ligacoes))
            conn.commit()
            conn.close()
            return produto.__dict__()


def alterar(produto):
    with str_conn as conn:
        with conn.cursor() as cursor:
            sql = f"UPDATE {model_name} SET alimentacao = ?, caracteristica = ?, categoria_venda = ?, certificado = ?, codigo_pedido = ?, descricao_completa = ?, descricao_reduzida = ?, fabricante = ?, funcao = ?, id_categoria = ?, modelo = ?, montagem = ?, status = ?, tag = ?, id_parametros = ?, id_equivalencia= ?, id_historico = ?,  id_ligacoes = ?"
            cursor.execute(sql, (produto.alimentacao, produto.caracteristica, produto.categoria_venda, produto.certificado,
                                 produto.codigo_pedido, produto.descricao_completa, produto.descricao_reduzida,
                                 produto.fabricante, produto.funcao, produto.id_categoria, produto.modelo, produto.montagem,
                                 produto.status, produto.tag, produto.id_parametros,
                                 produto.id_equivalencia, produto.id_historico, produto.id_ligacoes))
            conn.commit()


def remover(produto):
    with str_conn as conn:
        with conn.cursor() as cursor:
            sql = f"DELETE FROM {model_name} WHERE id_produto = ?"
            cursor.execute(sql, f"{produto.id_produto}")
            conn.commit()
