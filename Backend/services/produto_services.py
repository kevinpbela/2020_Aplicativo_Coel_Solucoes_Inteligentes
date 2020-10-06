from infra.produto.produto_dao import \
    listar as dao_listar, \
    consultar as dao_consultar, \
    cadastrar as dao_cadastrar

from model.produto import Produto


def listar():
    return [produto.__dict__() for produto in dao_listar()]


def localizar(id):
    produto = dao_consultar(id)
    if produto is None:
        return None
    return produto.__dict__()


def criar(produto):
    # if localizar(produto['id']) is None:
    produto = Produto.criar(produto)
    return dao_cadastrar(produto)
    # return None
