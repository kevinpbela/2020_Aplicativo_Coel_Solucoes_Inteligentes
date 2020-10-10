from infra.parametros.parametros_dao import \
    listar as dao_listar, \
    consultar as dao_consultar, \
    cadastrar as dao_cadastrar, \
    remover as dao_remover, \
    alterar as dao_alterar

from model.parametros import Parametros


def listar():
    return [parametros.__dict__() for parametros in dao_listar()]


def localizar(id):
    parametros = dao_consultar(id)
    if parametros is None:
        return None
    return parametros.__dict__()


def criar(parametros_dados):
    parametros = Parametros.criar(parametros_dados)
    return dao_cadastrar(parametros)


def remover(id):
    dados_parametros = localizar(id)
    if dados_parametros is None:
        return 0
    dao_remover(Parametros.criar(dados_parametros))
    return 1


def atualizar(id_parametros, tab_de_alarmes, tab_parametros,
              tab_parametros_dois, id_produto):
    parametros = Parametros.criar({"id_parametros": id_parametros, "tab_de_alarmes": tab_de_alarmes,
                                   "tab_parametros": tab_parametros, "tab_parametros_dois": tab_parametros_dois,
                                   "id_produto": id_produto})
    dao_alterar(parametros)
    return localizar(id)
