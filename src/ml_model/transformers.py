from transformers import pipeline
from celery import Celery

app = Celery('content_processor', broker='redis://localhost:6379/0', backend='redis://localhost:6379/0')

classifier_pipeline = pipeline(
    "zero-shot-classification",
    model="prajjwal1/bert-tiny-mnli"
)

sentiment_pipeline = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")


CATEGORIES = ["teknologi", "olahraga", "politik", "hiburan", "sains", "lainnya"]

# @app.task(max_retries=3)
def process_content(post_id, text):
    try:
        # Sentiment
        sentiment = sentiment_pipeline(text[:512])[0]
        
        # Classification
        classification = classifier_pipeline(text[:512], CATEGORIES, multi_class=False)
        
        return {
            'post_id': post_id,
            'sentiment': sentiment['label'],
            'sentiment_score': sentiment['score'],
            'category': classification['labels'][0],
            'category_score': classification['scores'][0],
        }
        
    except Exception as exc:
        process_content.retry(args=[post_id, text], exc=exc, countdown=60)
