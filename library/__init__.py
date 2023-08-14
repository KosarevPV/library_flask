from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from library.config import Config

db = SQLAlchemy()
login_manager = LoginManager()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)

    from library.main.routes import main
    from library.readers.routes import readers
    from library.library.routes import library

    app.register_blueprint(main)
    app.register_blueprint(readers)
    app.register_blueprint(library)

    return app
