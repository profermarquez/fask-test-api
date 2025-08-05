import pytest
from app import create_app, db

@pytest.fixture
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",  # DB en memoria
        "MONGO_URI": "mongodb://localhost:27017/test_db",  # Si querés testear mongo real
    })

    with app.app_context():
        db.create_all()  # Solo si querés usar SQLAlchemy
        yield app

@pytest.fixture
def client(app):
    return app.test_client()
