from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from ...schemas.post import PostRequest, PostResponse
from ...models.model import Post, Analysis, User
from ...database.db import db
from ...ml_model.transformers import process_content

bp = Blueprint('posts', __name__)

@bp.route("/post", methods=["POST"])
@jwt_required()
def upload():
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Nggak ada JSON yg diberikan'}), 400
        
        post_data = PostRequest(**data)
        current_user_id = get_jwt_identity()
        user = User.query.get(current_user_id)
        
        if not user:
            return jsonify({'error': 'User tidak ditemukan'}), 404

        post = Post(
            user_id=current_user_id,
            content=post_data.content
        )

        db.session.add(post)
        db.session.commit() 
        
     
        analysis_results = process_content(post_id=post.id, text=post_data.content)
        
     
        analysis = Analysis(
            post_id=post.id,
            sentiment=analysis_results['sentiment'],
            sentiment_score=analysis_results['sentiment_score'],
            category=analysis_results['category'],
            category_score=analysis_results['category_score']
        )
        
        db.session.add(analysis)
        db.session.commit()


        db.session.refresh(post)
        db.session.refresh(analysis)

        response_data = PostResponse(
            id=str(post.id),
            content=post.content,
            created_at=post.created_at,
            sentiment=analysis.sentiment,
            sentiment_score=analysis.sentiment_score,
            category=analysis.category,
            category_score=analysis.category_score,
            analyzed_at=analysis.analyzed_at
        )

        return jsonify(response_data.model_dump()), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": f"Error karena: {e}"}), 500
