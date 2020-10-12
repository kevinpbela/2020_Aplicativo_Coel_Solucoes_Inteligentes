from infra.montagem.montagem_dao import \
    listar as dao_listar, \
    consultar as dao_consultar

def listar():
    return [montagem for montagem in dao_listar()]


def localizar(id):
    montagem = dao_consultar(id)
    if montagem is None:
        return None
    return montagem
