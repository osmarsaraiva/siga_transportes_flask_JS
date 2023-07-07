from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///minhaloja.db'
app.config['SECRET_KEY'] = 'DSFGEDFKL12321'
db = SQLAlchemy(app)
bcrypt = bcrypt(app)


from loja.admin import rotas