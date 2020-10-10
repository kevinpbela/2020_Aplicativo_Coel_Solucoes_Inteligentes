import requests as Req
from flask import Flask, jsonify, request, render_template
from flask_cors import CORS

from routes.routes_produto import coel_produto
from routes.routes_usuario import coel_usuario
from routes.routes_categoria import coel_categoria
from routes.parametros_categoria import coel_parametros


app = Flask(__name__)
app.register_blueprint(coel_produto)
app.register_blueprint(coel_usuario)
app.register_blueprint(coel_categoria)
app.register_blueprint(coel_parametros)
CORS(app)

@app.route('/')
def all():
    usuario = Req.get("http://localhost:3000/usuario").json()
    produto = Req.get("http://localhost:3000/produto").json()
    categoria = Req.get("http://localhost:3000/categoria").json()
    parametros = Req.get("http://localhost:3000/parametros").json()
    return usuario, produto, categoria, parametros


if __name__ == '__main__':
    app.run(host='localhost', port=3000)
