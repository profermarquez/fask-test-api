class Config:
    JWT_SECRET_KEY = 'super-secret-key'
    MONGO_URI = 'mongodb://mongo:27017/users_db'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@postgres:5432/products_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False