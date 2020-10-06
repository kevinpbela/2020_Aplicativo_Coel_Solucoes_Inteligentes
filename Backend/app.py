from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
from routes.routes_produto import coel_produto
from routes.routes_usuario import coel_usuario
import requests as Req

app = Flask(__name__)
app.register_blueprint(coel_produto)
app.register_blueprint(coel_usuario)
CORS(app)

@app.route('/')
def all():
    usuario = Req.get("http://localhost:3000/usuario").json()
    produto = Req.get("http://localhost:3000/produto").json()
    return usuario, produto


if __name__ == '__main__':
    app.run(host='localhost', port=3000)
