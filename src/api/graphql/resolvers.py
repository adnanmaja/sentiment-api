from ariadne import QueryType, convert_kwargs_to_snake_case
from ...models.model import Analysis, Post, User
import uuid

# Makasih deepseek wkw

query = QueryType()

@query.field("userAnalysisHistory")
@convert_kwargs_to_snake_case
def resolve_user_analysis_history(_, info, user_id, **filters):
    try:
        # Build base query
        query = Analysis.query.join(Post).join(User).filter(User.id == user_id)
        
        # Apply filters
        sentiment = filters.get('sentiment')
        category = filters.get('category')
        min_sentiment_score = filters.get('min_sentiment_score')
        max_sentiment_score = filters.get('max_sentiment_score')
        limit = filters.get('limit', 10)
        offset = filters.get('offset', 0)
        
        if sentiment:
            query = query.filter(Analysis.sentiment == sentiment)
        if category:
            query = query.filter(Analysis.category == category)
        if min_sentiment_score is not None:
            query = query.filter(Analysis.sentiment_score >= min_sentiment_score)
        if max_sentiment_score is not None:
            query = query.filter(Analysis.sentiment_score <= max_sentiment_score)
        
        # Order by analysis date (newest first) and apply pagination
        analyses = query.order_by(Analysis.analyzed_at.desc()).offset(offset).limit(limit).all()
        
        return analyses
        
    except Exception as e:
        # Log the error for debugging
        print(f"Error in resolve_user_analysis_history: {str(e)}")
        raise e

# Custom resolver for datetime fields to convert to ISO format
def resolve_datetime_field(obj, info):
    if hasattr(obj, info.field_name):
        dt = getattr(obj, info.field_name)
        return dt.isoformat() if dt else None
    return None

# Resolver for nested relationships
def resolve_post_analysis(analysis_obj, info):
    return analysis_obj.post

def resolve_post_user(post_obj, info):
    return post_obj.user