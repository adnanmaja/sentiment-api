from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, create_refresh_token

from ...schemas.user import UserLogin, UserResponse,  TokenResponse
from ...models.model import User

bp = Blueprint('login', __name__)

@bp.route('/login', methods=['POST'])
def login():
    try:

        data = request.get_json()
        if not data:
            return jsonify({'error': 'Nggak ada JSON yg diberikan'}), 400
        
        user_data = UserLogin(**data)

        user = User.query.filter_by(email=user_data.email).first()
        
        if not user or not user.check_password(user_data.password):
            return jsonify({'error': 'Password atau email salah!'}), 401
        
        if not user.is_active:
            return jsonify({'error': 'is_active = False??'}), 401
        
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
        
        return jsonify(response_data.model_dump()), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500