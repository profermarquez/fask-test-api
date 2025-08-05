from flask import Flask, request
from flask_jwt_extended import JWTManager
from flask_pymongo import PyMongo
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS  
from dotenv import load_dotenv
import os
import logging

# Cargar variables de entorno
load_dotenv()

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

    # Habilitar CORS (todos los orígenes por defecto)
    CORS(app)  # 👈 agregado

    # Si querés permitir solo ciertos dominios:
    # CORS(app, resources={r"/*": {"origins": ["http://localhost:4200", "https://midominio.com"]}})

    #  Asegurar carpeta de logs
    os.makedirs("logs", exist_ok=True)

    # Configuración del logger global
    access_logger = logging.getLogger("access_logger")
    access_logger.setLevel(logging.INFO)
    handler = logging.FileHandler("logs/accesos.log")
    handler.setFormatter(logging.Formatter('%(asctime)s - %(message)s'))
    if not access_logger.hasHandlers():
        access_logger.addHandler(handler)

    # Middleware global: registrar cada request
    @app.before_request
    def registrar_acceso():
        if request.path != "/favicon.ico":
            ip = request.remote_addr
            ruta = request.path
            metodo = request.method
            agente = request.headers.get("User-Agent", "desconocido")
            access_logger.info(f"{metodo} {ruta} - IP: {ip} - UA: {agente}")

    from app.auth import auth_bp
    from app.product import product_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(product_bp)

    with app.app_context():
        from app.product import Product
        db.create_all()

    return app
