from flask import Blueprint, jsonify, request
from services.parametros_services import \
    listar as service_listar_parametros, \
    criar as service_criar_parametros, \
    atualizar as service_atualiza_parametros, \
    localizar as service_localiza_parametros, \
    remover as service_remover_parametros


coel_parametros = Blueprint('coel_parametros', __name__)


@coel_parametros.route('/parametros')
def listar_parametros():
    lista = service_listar_parametros()
    return jsonify(lista)


@coel_parametros.route('/parametros', methods=['POST'])
def cadastrar_parametros():
    novo_parametros = request.get_json()

    if novo_parametros is None:
        return jsonify({'erro': 'parametros invalidos'}), 400

    parametros = service_criar_parametros(novo_parametros)
    if parametros is None:
        return jsonify({'erro': 'parametros ja existe'}), 400
    return jsonify(parametros)


@coel_parametros.route('/parametros/<int:id>', methods=['PUT'])
def alterar_parametros(id_parametros):
    parametros_data = request.get_json()

    atualizado = service_atualiza_parametros(id_parametros, parametros_data["tab_de_alarmes"], 
                                             parametros_data["tab_parametros"], parametros_data["tab_parametros_dois"],
                                             parametros_data["id_produto"])

    if atualizado is not None:
        return jsonify(atualizado), 200
    return jsonify({'erro': 'parametros nao encontrado'}), 400


@coel_parametros.route('/parametros/<int:id>', methods=['GET'])
def localizar_parametros(id):
    produto = service_localiza_parametros(id)
    if produto is not None:
        return jsonify(produto)
    return jsonify({'erro': 'parametros não encontrado'}), 400


@coel_parametros.route('/parametros/<int:id>', methods=['DELETE'])
def remover_parametros(id):
    removido = service_remover_parametros(id)
    if removido == 1:
        return jsonify(removido), 202
    return jsonify({'erro': 'parametros não encontrado'}), 400
