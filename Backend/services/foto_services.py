from infra.foto.foto_dao import \
    listar as dao_listar, \
    consultar as dao_consultar

def listar():
    return [foto for foto in dao_listar()]


def localizar(id):
    foto = dao_consultar(id)
    if foto is None:
        return None
    return foto
