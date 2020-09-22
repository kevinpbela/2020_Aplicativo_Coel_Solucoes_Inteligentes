from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
from main import coel_app
import requests as Req
import infra.usuario_db as usuario_db

app = Flask(__name__)
app.register_blueprint(coel_app)
CORS(app)

@app.route('/')
def all():
    return Req.get("http://localhost:5000/usuario").json()

# usuario_db.init()

if __name__ == '__main__':
    app.run(host='localhost', port=3000)
