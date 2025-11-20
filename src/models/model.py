from src.database.db import db  
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Text, Float
from datetime import datetime, timezone
from sqlalchemy.dialects.postgresql import UUID, JSON
from sqlalchemy.orm import relationship
import uuid

# === Importnya gjls error mulu, pake ini dulu aj dh ===================

# ==================================================================

class User(db.Model):  
    __tablename__ = "users"
    id = db.Column(UUID(as_uuid=False), primary_key=True, default=uuid.uuid4)
    name = db.Column(String, nullable=False)
    email = db.Column(String, unique=True, nullable=False)
    password_hash = db.Column(String) 
    token_version = db.Column(String(10), default="v1")
    created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc))
    is_active = db.Column(Boolean, default=True)

    posts = relationship("Post", back_populates="user")

    def set_password(self, password):
        # Di hash
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        # Apakah hash nya sama?
        if not self.password_hash:
            return False
        return check_password_hash(self.password_hash, password)

class Post(db.Model):  
    __tablename__="posts"
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = db.Column(UUID(as_uuid=True), ForeignKey('users.id'), nullable=False)
    title = db.Column(String(300))
    content = db.Column(Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))

    user = relationship("User", back_populates="posts")
    analysis = relationship("Analysis", back_populates="post", uselist=False)

class Analysis(db.Model):  
    __tablename__="analysis"
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    post_id = db.Column(UUID(as_uuid=True), ForeignKey('posts.id'), nullable=False, unique=True)
    sentiment_score = db.Column(Float)  
    tags = db.Column(JSON)  
    analyzed_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))

    post = relationship("Post", back_populates="analysis")

