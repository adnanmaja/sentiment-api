from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity

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
    
@bp.route('/me', methods=['GET'])
@jwt_required()
def get_current_user():
    try:
        # Get user ID from JWT token
        current_user_id = get_jwt_identity()
        
        # Query the user from database
        user = User.query.filter_by(id=current_user_id).first()
        
        if not user:
            return jsonify({'error': 'User not found'}), 404
        
        if not user.is_active:
            return jsonify({'error': 'User account is inactive'}), 401
        
        # Return whatever the fuck the user wants to see
        user_response = UserResponse.model_validate(user)
        return jsonify({
            'user': user_response.model_dump()
        }), 200
        
    except Exception as e:
        return jsonify({'error': f'Something fucked up: {str(e)}'}), 500