from flask import Flask
from flask_jwt_extended import JWTManager
from flask_pymongo import PyMongo
from flask_sqlalchemy import SQLAlchemy

jwt = JWTManager()
mongo = PyMongo()
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Configuraciones desde archivo externo
    app.config.from_object('app.config.Config')

    jwt.init_app(app)
    mongo.init_app(app)
    db.init_app(app)

    from app.auth import auth_bp
    from app.product import product_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(product_bp)

    with app.app_context():
        from app.product import Product  # Importá el modelo
        db.create_all()  # Crea las tablas si no existen

    return app
