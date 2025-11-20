from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from ...schemas.user import ChangePassword
from ...models.model import User
from ...database.db import db
import uuid

bp = Blueprint('pwchange', __name__)

@bp.route('/change-password', methods=['POST'])
@jwt_required()
def change_password():
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Nggak ada JSON yg diberikan'}), 400
        
        password_data = ChangePassword(**data)
        
        current_user_id = get_jwt_identity()
        user = User.query.get(current_user_id)
        
        if not user or not user.check_password(password_data.current_password):
            return jsonify({'error': 'Password baru invalid'}), 401
        
        user.set_password(password_data.new_password)
        user.token_version = str(uuid.uuid4())[:10]
        
        db.session.commit()
        
        return jsonify({'message': 'Password berhasil diganti'}), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500