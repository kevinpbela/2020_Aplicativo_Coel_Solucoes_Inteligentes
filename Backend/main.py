from flask import Blueprint, jsonify, request
from services.usuario_services import \
    listar as service_listar, \
    localizar as service_localiza, \
    criar as service_criar

coel_app = Blueprint('coel_app', __name__)


@coel_app.route('/usuario')
def listar_usuario():
    lista = service_listar()
    return jsonify(lista)


@coel_app.route('/usuario', methods=['POST'])
def cadastrar_usuario():
    novo_usuario = request.get_json()

    if 'login' not in novo_usuario or 'senha' not in novo_usuario:
        return jsonify({'erro': 'usuario sem login ou senha'}), 400

    usuario = service_criar(novo_usuario)
    if usuario is None:
        return jsonify({'erro': 'usuario ja existe'}), 400
    return jsonify(usuario)


@coel_app.route('/usuario/<int:id>', methods=['GET'])
def localizar_usuario(id: int):
    usuario = service_localiza(id)
    if usuario is not None:
        return jsonify(usuario)
    return jsonify({'erro': 'usuario nao encontrado'}), 400
