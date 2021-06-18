import sqlite3
from flask import Flask

# Configurações
DATABASE = './flaskr.db'
SECRET KEY = 'pudim'
USERNAME = 'admin'
PASSWORD = 'admin'

# Aplicação
app = Flask(__name__)
app.config.from_object(__name__)

def connect_db():
    return sqlite3.connect(DATABASE)

@app.route('/')
def index():
    return "Hello World!"