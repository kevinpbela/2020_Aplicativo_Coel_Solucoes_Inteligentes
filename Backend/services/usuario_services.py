from infra.usuario_dao import \
    listar as dao_listar, \
    consultar as dao_consultar, \
    cadastrar as dao_cadastrar

from model.usuario import Usuario


def listar():
    return [usuario.__dict__() for usuario in dao_listar()]


def localizar(id):
    usuario = dao_consultar(id)
    if usuario is None:
        return None
    return usuario.__dict__()


def criar(usuario):
    # if localizar(usuario['id']) is None:
    usuario = Usuario.criar(usuario)
    return dao_cadastrar(usuario)
    # return None
