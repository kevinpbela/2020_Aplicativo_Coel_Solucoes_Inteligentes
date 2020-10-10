from flask import Blueprint, jsonify, request
from services.categoria_services import \
    listar as service_listar_categoria, \
    criar as service_criar_categoria, \
    atualizar as service_atualiza_categoria, \
    localizar as service_localiza_categoria, \
    remover as service_remover_categoria


coel_categoria = Blueprint('coel_categoria', __name__)


@coel_categoria.route('/categoria')
def listar_categoria():
    lista = service_listar_categoria()
    return jsonify(lista)


@coel_categoria.route('/categoria', methods=['POST'])
def cadastrar_categoria():
    nova_categoria = request.get_json()

    if nova_categoria is None:
        return jsonify({'erro': 'categoria invalida'}), 400

    categoria = service_criar_categoria(nova_categoria)
    if categoria is None:
        return jsonify({'erro': 'categoria ja existe'}), 400
    return jsonify(categoria)


@coel_categoria.route('/categoria/<int:id>', methods=['PUT'])
def alterar_categoria(id_categoria):
    categoria_data = request.get_json()

    atualizado = service_atualiza_categoria(id_categoria, categoria_data["categoria"], categoria_data["sub_categoria_um"],
                                            categoria_data["sub_categoria_dois"], categoria_data["sub_categoria_tres"],
                                            categoria_data["sub_categoria_quatro"], categoria_data["id_produto"])

    if atualizado is not None:
        return jsonify(atualizado), 200
    return jsonify({'erro': 'categoria nao encontrado'}), 400


@coel_categoria.route('/categoria/<int:id>', methods=['GET'])
def localizar_aluno(id):
    produto = service_localiza_categoria(id)
    if produto is not None:
        return jsonify(produto)
    return jsonify({'erro': 'categoria não encontrado'}), 400


@coel_categoria.route('/categoria/<int:id>', methods=['DELETE'])
def remover_aluno(id):
    removido = service_remover_categoria(id)
    if removido == 1:
        return jsonify(removido), 202
    return jsonify({'erro': 'categoria não encontrado'}), 400
