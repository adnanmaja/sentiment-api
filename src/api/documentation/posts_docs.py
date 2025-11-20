from flask_restx import Namespace, Resource, fields
from ..routes.post import upload

ns = Namespace('posts', description='Post operations', path='/api')

post_model = ns.model('PostCreate', {
    'content': fields.String(required=True, example='Hello everyone!')
})

post_response_model = ns.model('PostResponse', {
    'id': fields.String(example='0d528b7e-b5ba-41ed-aa72-c0de46a2845f'),
    'content': fields.String(example='Hello everyone!'),
    'created_at': fields.DateTime(),
    'sentiment': fields.String(example='POSITIVE'),
    'sentiment_score': fields.Float(example=0.9778941),
    'category': fields.String(example='lainnya'),
    'category_score': fields.Float(example=0.20389),
    'analyzed_at': fields.DateTime()
})

@ns.route('/post')
class PostUpload(Resource):
    @ns.expect(post_model)
    @ns.response(201, 'Success', post_response_model)
    @ns.response(400, 'Bad Request')
    @ns.response(500, 'Server Error')
    def post(self):
        return upload()