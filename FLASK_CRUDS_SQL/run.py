from flask import Flask, redirect, render_template, url_for
from flask_bootstrap import Bootstrap
import os
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


bootstrap = Bootstrap()
db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'authentication.do_login'
login_manager.session_protection = 'strong'

app = Flask(__name__)
bootstrap = Bootstrap()

Bootstrap(app)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/addasset')
def add_asset():
    return render_template("add_asset.html")


if __name__ == "__main__":
    app.run(debug=True)