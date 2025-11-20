from flask import Blueprint, request, jsonify
from ...database.db import db
from ...models.model import User
from ...schemas.user import UserCreate, UserResponse, TokenResponse
from flask_jwt_extended import create_access_token, create_refresh_token

bp = Blueprint('register', __name__)

@bp.route("/register", methods=["POST"])
def register():
    try:

        data = request.get_json()
        if not data:
            return jsonify({'error': 'Tidak ada JSON yg diberikan'}), 400
        
        user_data = UserCreate(**data)

        if User.query.filter_by(email=user_data.email).first():
            return jsonify({'error': 'User sudah ada'}), 400

        user = User(
            name=user_data.name,
            email=user_data.email,
            is_active=True
        )
        user.set_password(user_data.password)
        
        db.session.add(user)
        db.session.commit()
 
        access_token = create_access_token(
            identity=str(user.id),
            additional_claims={'token_version': user.token_version}
        )
        refresh_token = create_refresh_token(
            identity=str(user.id),
            additional_claims={'token_version': user.token_version}
        )
        
        response_data = TokenResponse(
            access_token=access_token,
            refresh_token=refresh_token,
            user=UserResponse.model_validate(user)
        )
        
        return jsonify(response_data.model_dump()), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500
