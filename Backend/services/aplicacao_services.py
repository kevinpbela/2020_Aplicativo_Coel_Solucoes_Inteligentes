from infra.aplicacao.aplicacao_dao import \
    listar as dao_listar, \
    consultar as dao_consultar

def listar():
    return [aplicacao for aplicacao in dao_listar()]


def localizar(id):
    aplicacao = dao_consultar(id)
    if aplicacao is None:
        return None
    return aplicacao
