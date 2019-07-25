from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
app = Flask(__name__)

app.config.from_object('config')

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "auth.login"
login_manager.login_message_category = "warning"

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


from app.home.controllers import mod_home as home
from app.auth.controllers import mod_auth as auth

app.register_blueprint(home)
app.register_blueprint(auth)

