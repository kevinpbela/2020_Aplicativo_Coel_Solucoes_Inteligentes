from infra.alimentacao.alimentacao_dao import \
    listar as dao_listar, \
    consultar as dao_consultar

def listar():
    return [alimentacao for alimentacao in dao_listar()]


def localizar(id):
    alimentacao = dao_consultar(id)
    if alimentacao is None:
        return None
    return alimentacao
