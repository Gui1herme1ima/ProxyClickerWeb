from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sua_chave_secreta'

from app import routes