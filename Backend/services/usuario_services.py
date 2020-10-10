from infra.usuario.usuario_dao import \
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


def criar(usuario_dados):
    usuario = Usuario.criar(usuario_dados)
    return dao_cadastrar(usuario)
