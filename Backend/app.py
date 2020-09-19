from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
from main import login_app
import requests as Req
import infra.login_db as login_db

app = Flask(__name__)
app.register_blueprint(login_app)
CORS(app)

@app.route('/')
def all():
    return Req.get("http://localhost:5000/usuario").json()

login_db.init()

if __name__ == '__main__':
    app.run(host='localhost', port=3000)
