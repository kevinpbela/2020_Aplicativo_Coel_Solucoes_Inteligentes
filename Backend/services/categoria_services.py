from infra.categoria.categoria_dao import \
    listar as dao_listar, \
    consultar as dao_consultar

def listar():
    return [categoria for categoria in dao_listar()]


def localizar(id):
    categoria = dao_consultar(id)
    if categoria is None:
        return None
    return categoria
