from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from app import mongo

auth_bp = Blueprint('auth', __name__)

""" @auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data['username']
    password = generate_password_hash(data['password'])

    if mongo.db.users.find_one({"username": username}):
        return jsonify({"msg": "Usuario ya existe"}), 400

    mongo.db.users.insert_one({"username": username, "password": password})
    return jsonify({"msg": "Usuario registrado"}), 201
 """
@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = mongo.db.users.find_one({"username": data['username']})

    if user and check_password_hash(user['password'], data['password']):
        token = create_access_token(identity=str(user['_id']))
        return jsonify({"access_token": token})
    return jsonify({"msg": "Credenciales inválidas"}), 401