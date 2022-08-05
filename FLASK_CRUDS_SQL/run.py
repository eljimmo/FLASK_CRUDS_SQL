from flask import Flask, redirect, render_template, url_for
from flask_bootstrap import Bootstrap
import os
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from asset import *
from auth import *



bootstrap = Bootstrap()
db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'authentication.do_login'
login_manager.session_protection = 'strong'

app = Flask(__name__)
bootstrap = Bootstrap()

Bootstrap(app)



from auth import *
app.register_blueprint(authentication)

from asset import *
app.register_blueprint(main)

if __name__ == "__main__":
    app.run(debug=True)