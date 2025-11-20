from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv
from flask_jwt_extended import JWTManager

load_dotenv()

db = SQLAlchemy()

def init_app(app):

    database_url = os.getenv("DATABASE_URL")
    if database_url and "sslmode" not in database_url:
        database_url += "?sslmode=require"
    
    app.config['SQLALCHEMY_DATABASE_URI'] = database_url
    app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
        'connect_args': {
            'sslmode': 'require'
        }
    }
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # JWT Config
    app.config['JWT_SECRET_KEY'] = os.getenv("JWT_KEY")
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = 3600  # 1 jam
    app.config['JWT_REFRESH_TOKEN_EXPIRES'] = 86400  # 24 jam
  
    jwt = JWTManager(app)
    db.init_app(app)
    
    return app