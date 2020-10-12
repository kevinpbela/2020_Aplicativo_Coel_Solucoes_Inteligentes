from infra.certificado.certificado_dao import \
    listar as dao_listar, \
    consultar as dao_consultar

def listar():
    return [certificado for certificado in dao_listar()]


def localizar(id):
    certificado = dao_consultar(id)
    if certificado is None:
        return None
    return certificado
