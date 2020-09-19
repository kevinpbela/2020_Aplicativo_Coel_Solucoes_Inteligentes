from infra.login_dao import \
    listar as dao_listar, \
    consultar as dao_consultar, \
    cadastrar as dao_cadastrar

from model.login import Login


def listar():
    return [login.__dict__() for login in dao_listar()]


def localizar(id_usuario):
    login = dao_consultar(id_usuario)
    if login is None:
        return None
    return login.__dict__()


def criar(usuario):
    if localizar(usuario['id_usuario']) is None:
        login = Login.criar(usuario)
        return dao_cadastrar(login)
    return None
