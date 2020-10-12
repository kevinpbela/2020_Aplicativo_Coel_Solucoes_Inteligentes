import requests as Req
from flask import Flask, jsonify, request, render_template
from flask_cors import CORS

from routes.routes_usuario import coel_usuario
from routes.routes_alimentacao import coel_alimentacao
from routes.routes_aplicacao import coel_aplicacao
from routes.routes_aplicacao_navegacao import coel_navegacao
from routes.routes_categoria import coel_categoria
from routes.routes_funcao import coel_funcao
from routes.routes_foto import coel_foto
from routes.routes_categoria_venda import coel_categoria_venda
from routes.routes_certificado import coel_certificado
from routes.routes_montagem import coel_montagem
from routes.routes_manual import coel_manual


app = Flask(__name__)
app.register_blueprint(coel_usuario)
app.register_blueprint(coel_alimentacao)
app.register_blueprint(coel_aplicacao)
app.register_blueprint(coel_navegacao)
app.register_blueprint(coel_categoria)
app.register_blueprint(coel_funcao)
app.register_blueprint(coel_foto)
app.register_blueprint(coel_certificado)
app.register_blueprint(coel_montagem)
app.register_blueprint(coel_manual)
CORS(app)


@app.route('/')
def all():
    usuario = Req.get("http://localhost:3000/usuario").json()
    alimentacao = Req.get("http://localhost:3000/alimentacao").json()
    aplicacao = Req.get("http://localhost:3000/aplicacao").json()
    navegacao = Req.get("http://localhost:3000/navegacao").json()
    categoria = Req.get("http://localhost:3000/categoria").json()
    funcao = Req.get("http://localhost:3000/funcao").json()
    foto = Req.get("http://localhost:3000/foto").json()
    categoria_venda = Req.get("http://localhost:3000/categoria_venda").json()
    certificado = Req.get("http://localhost:3000/certificado").json()
    montagem = Req.get("http://localhost:3000/montagem").json()
    manual = Req.get("http://localhost:3000/manual").json()

    return (usuario, alimentacao, aplicacao, navegacao, categoria, funcao,
            foto, categoria_venda, certificado, montagem, manual)


if __name__ == '__main__':
    app.run(host='localhost', port=3000)
