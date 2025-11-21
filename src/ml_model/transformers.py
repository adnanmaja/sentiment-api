import os
from textblob import TextBlob


class LightweightTopicClassifier:
    def __init__(self):
        self.categories = {
            "Technology": {'computer', 'phone', 'software', 'internet', 'digital', 'tech', 'app', 'device', 'iphone', 'android', 'code'},
            "Sports": {'game', 'team', 'player', 'score', 'sport', 'basketball', 'football', 'win', 'match', 'championship'},
            "Politics": {'government', 'election', 'policy', 'political', 'vote', 'law', 'congress', 'president', 'campaign'},
            "Entertainment": {'movie', 'film', 'actor', 'music', 'show', 'celebrity', 'entertainment', 'tv', 'netflix'},
            "Science": {'research', 'study', 'scientific', 'discovery', 'experiment', 'data', 'analysis', 'university', 'physics'}
        }
    
    def classify(self, text):
        text_lower = text.lower()
        scores = {}
        
        for category, keywords in self.categories.items():
            score = sum(1 for keyword in keywords if keyword in text_lower)
            scores[category] = score
        
        best_category = max(scores, key=scores.get)
        best_score = scores[best_category]
        
        total_keywords = sum(scores.values())
        confidence = best_score / max(total_keywords, 1) if total_keywords > 0 else 0
        
        if best_score == 0:
            return {'labels': ['Others'], 'scores': [0.8]}
        else:
            return {'labels': [best_category], 'scores': [min(confidence + 0.3, 0.99)]}

# Initialize classifiers
topic_classifier = LightweightTopicClassifier()
CATEGORIES = ["Technology", "Sports", "Politics", "Entertainment", "Science", "Others"]

def get_sentiment(text):
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity
    
    if polarity > 0.1:
        return {'label': 'POSITIVE', 'score': min(abs(polarity) + 0.5, 0.99)}
    elif polarity < -0.1:
        return {'label': 'NEGATIVE', 'score': min(abs(polarity) + 0.5, 0.99)}
    else:
        return {'label': 'NEUTRAL', 'score': 0.8}

def process_content(post_id, text):
    try:
        # Sentiment (replacement)
        sentiment = get_sentiment(text[:512])
        
        # Classification (replacement)
        classification = topic_classifier.classify(text[:512])
        
        return {
            'post_id': post_id,
            'sentiment': sentiment['label'],
            'sentiment_score': round(sentiment['score'], 4),
            'category': classification['labels'][0],
            'category_score': round(classification['scores'][0], 4),
        }
        
    except Exception as exc:
        print(f"Error processing {post_id}: {exc}")
        return {
            'post_id': post_id,
            'sentiment': 'NEUTRAL',
            'sentiment_score': 0.5,
            'category': 'Others',
            'category_score': 0.5,
        }