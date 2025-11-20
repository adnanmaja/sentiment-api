from flask_restx import Namespace, Resource, fields
from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt, create_access_token, create_refresh_token
import uuid
from ..routes.register import register
from ..routes.login import login
from ..routes.pwchange import change_password
from ...schemas.user import UserLogin, UserResponse, TokenResponse, UserCreate, ChangePassword
from ...models.model import User
from ...database.db import db

auth_ns = Namespace('auth', description='Authentication operations', path='/api')

user_create_model = auth_ns.model('UserCreate', {
    'name': fields.String(required=True, description='User full name'),
    'email': fields.String(required=True, description='User email address'),
    'password': fields.String(required=True, description='User password')
})

user_login_model = auth_ns.model('UserLogin', {
    'email': fields.String(required=True, description='User email address'),
    'password': fields.String(required=True, description='User password')
})

change_password_model = auth_ns.model('ChangePassword', {
    'current_password': fields.String(required=True, description='Current password'),
    'new_password': fields.String(required=True, description='New password')
})

user_response_model = auth_ns.model('UserResponse', {
    'name': fields.String(description='User full name'),
    'email': fields.String(description='User email address'),
    'id': fields.String(description='User ID'),
    'created_at': fields.DateTime(description='Creation timestamp'),
    'is_active': fields.Boolean(description='User active status')
})

token_response_model = auth_ns.model('TokenResponse', {
    'access_token': fields.String(description='JWT access token'),
    'refresh_token': fields.String(description='JWT refresh token'),
    'user': fields.Nested(user_response_model, description='User information')
})

success_message_model = auth_ns.model('SuccessMessage', {
    'message': fields.String(description='Success message')
})

error_message_model = auth_ns.model('ErrorMessage', {
    'error': fields.String(description='Error message')
})

@auth_ns.route('/register')
class Register(Resource):
    @auth_ns.expect(user_create_model)
    @auth_ns.response(201, 'Success', token_response_model)
    @auth_ns.response(400, 'Bad Request', error_message_model)
    @auth_ns.response(500, 'Internal Server Error', error_message_model)
    def post(self):
        return register()

@auth_ns.route('/login')
class Login(Resource):
    @auth_ns.expect(user_login_model)
    @auth_ns.response(200, 'Success', token_response_model)
    @auth_ns.response(400, 'Bad Request', error_message_model)
    @auth_ns.response(401, 'Unauthorized', error_message_model)
    @auth_ns.response(500, 'Internal Server Error', error_message_model)
    def post(self):
        return login()

@auth_ns.route('/change-password')
class ChangePassword(Resource):
    @auth_ns.expect(change_password_model)
    @auth_ns.response(200, 'Success', success_message_model)
    @auth_ns.response(400, 'Bad Request', error_message_model)
    @auth_ns.response(401, 'Unauthorized', error_message_model)
    @auth_ns.response(500, 'Internal Server Error', error_message_model)
    @jwt_required()
    def post(self):
        return change_password()