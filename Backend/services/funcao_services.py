from infra.funcao.funcao_dao import \
    listar as dao_listar, \
    consultar as dao_consultar

def listar():
    return [funcao for funcao in dao_listar()]


def localizar(id):
    funcao = dao_consultar(id)
    if funcao is None:
        return None
    return funcao
