from infra.usuario.usuario_dao import \
    listar as dao_listar, \
    consultar as dao_consultar, \
    cadastrar as dao_cadastrar

from model.usuario import Usuario


def listar():
    return [usuario for usuario in dao_listar()]


def localizar(login):
    usuario = dao_consultar(login)
    if usuario is None:
        return None
    return usuario


def criar(usuario_dados):
    usuario = Usuario.criar(usuario_dados)
    return dao_cadastrar(usuario)
