from flask import Blueprint, jsonify, request
from services.produto_services import \
    listar as service_listar_produto, \
    criar as service_criar_produto, \
    atualizar as service_atualiza_produto, \
    localizar as service_localiza_produto, \
    remover as service_remover_produto
    

coel_produto = Blueprint('coel_produto', __name__)


@coel_produto.route('/produto')
def listar_produto():
    lista = service_listar_produto()
    return jsonify(lista)


@coel_produto.route('/produto', methods=['POST'])
def cadastrar_produto():
    novo_produto = request.get_json()

    if novo_produto is None:
        return jsonify({'erro': 'produto invalido'}), 400

    produto = service_criar_produto(novo_produto)
    if produto is None:
        return jsonify({'erro': 'aluno ja existe'}), 400
    return jsonify(produto)


@coel_produto.route('/produto/<int:id>', methods=['PUT'])
def alterar_produto(id_produto):
    produto_data = request.get_json()

    atualizado = service_atualiza_produto(id_produto, produto_data["alimentacao"], produto_data["caracteristica"],
                                  produto_data["categoria_venda"], produto_data["certificado"], produto_data["codigo_pedido"],
                                  produto_data["descricao_completa"], produto_data["descricao_reduzida"],
                                  produto_data["fabricante"], produto_data["funcao"], produto_data["id_categoria"],
                                  produto_data["modelo"], produto_data["montagem"], produto_data["status"], produto_data["tag"],
                                  produto_data["id_parametros"])

    if atualizado is not None:
        return jsonify(atualizado), 200
    return jsonify({'erro': 'produto nao encontrado'}), 400


@coel_produto.route('/produto/<int:id>', methods=['GET'])
def localizar_aluno(id):
    produto = service_localiza_produto(id)
    if produto is not None:
        return jsonify(produto)
    return jsonify({'erro': 'produto não encontrado'}), 400


@coel_produto.route('/produto/<int:id>', methods=['DELETE'])
def remover_aluno(id):
    removido = service_remover_produto(id)
    if removido == 1:
        return jsonify(removido), 202
    return jsonify({'erro': 'produto não encontrado'}), 400
