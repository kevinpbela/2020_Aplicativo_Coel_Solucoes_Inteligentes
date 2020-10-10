from infra.categoria.categoria_dao import \
    listar as dao_listar, \
    consultar as dao_consultar, \
    cadastrar as dao_cadastrar, \
    remover as dao_remover, \
    alterar as dao_alterar

from model.categoria import Categoria


def listar():
    return [categoria.__dict__() for categoria in dao_listar()]


def localizar(id):
    categoria = dao_consultar(id)
    if categoria is None:
        return None
    return categoria.__dict__()


def criar(categoria_dados):
    categoria = Categoria.criar(categoria_dados)
    return dao_cadastrar(categoria)


def remover(id):
    dados_categoria = localizar(id)
    if dados_categoria is None:
        return 0
    dao_remover(Categoria.criar(dados_categoria))
    return 1


def atualizar(id_categoria, categoria, sub_categoria_um, sub_categoria_dois,
              sub_categoria_tres, sub_categoria_quatro, id_produto):
    categoria = Categoria.criar({"id_categoria": id_categoria, "categoria": categoria, "sub_categoria_um": sub_categoria_um,
                                 "sub_categoria_dois": sub_categoria_dois, "sub_categoria_tres": sub_categoria_tres,
                                 "sub_categoria_quatro": sub_categoria_quatro, "id_produto": id_produto})
    dao_alterar(categoria)
    return localizar(id)
