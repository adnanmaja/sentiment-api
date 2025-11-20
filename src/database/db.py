from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv
from flask_jwt_extended import JWTManager

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

db = SQLAlchemy()

def init_app(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
    app.config['from_attributes']=True
    app.config['JWT_SECRET_KEY'] = os.getenv("JWT_KEY")
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = 3600  # 1 jam
    app.config['JWT_REFRESH_TOKEN_EXPIRES'] = 86400  # 24 jam
    
    # Initialize JWTManager
    jwt = JWTManager(app)

    db.init_app(app)
    return app