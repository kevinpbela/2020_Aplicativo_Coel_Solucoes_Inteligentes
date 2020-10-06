from flask import Blueprint, jsonify, request
from services.produto_services import listar as service_listar_produto

coel_produto = Blueprint('coel_produto', __name__)


@coel_produto.route('/produto')
def listar_produto():
    lista = service_listar_produto()
    return jsonify(lista)
