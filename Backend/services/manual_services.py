from infra.manual.manual_dao import \
    listar as dao_listar, \
    consultar as dao_consultar

def listar():
    return [manual for manual in dao_listar()]


def localizar(id):
    manual = dao_consultar(id)
    if manual is None:
        return None
    return manual
