from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app import db

product_bp = Blueprint('product', __name__)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Float, nullable=False)

@product_bp.route('/products', methods=['GET'])
@jwt_required()
def get_products():
    products = Product.query.all()
    return jsonify([{"id": p.id, "name": p.name, "price": p.price} for p in products])

@product_bp.route('/products', methods=['POST'])
@jwt_required()
def add_product():
    data = request.get_json()
    new_product = Product(name=data['name'], price=data['price'])
    db.session.add(new_product)
    db.session.commit()
    return jsonify({"msg": "Producto agregado"}), 201