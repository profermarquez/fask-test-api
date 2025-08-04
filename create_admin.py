from app import create_app, mongo
from werkzeug.security import generate_password_hash

app = create_app()

with app.app_context():
    username = "admin"
    password = "admin123"

    # Verifica si ya existe
    if mongo.db.users.find_one({"username": username}):
        print("ℹ️ El usuario admin ya existe.")
    else:
        hashed_pw = generate_password_hash(password)
        mongo.db.users.insert_one({
            "username": username,
            "password": hashed_pw,
            #"role": "admin"  
        })
        print("✅ Usuario admin creado.")
