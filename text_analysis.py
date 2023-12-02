import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')
from langdetect import detect

def analyze_text(text):
    # Sentiment analysis
    sia = SentimentIntensityAnalyzer()
    sentiment = sia.polarity_scores(text)

    # Basic content type analysis
    if text.strip().endswith('?'):
        content_type = 'question'
    elif text.strip().endswith('!'):
        content_type = 'exclamation'
    else:
        content_type = 'statement'

    # Determine speech rate based on content type and sentiment
    if content_type == 'question':
        rate = 'slow'
    elif content_type == 'exclamation' or sentiment['compound'] > 0.5:
        rate = 'fast'
    else:
        rate = 'medium'

    return {'rate': rate, 'content_type': content_type, 'sentiment': sentiment['compound']}


def enhanced_analyze_text(text):
    # Enhanced sentiment analysis
    # ... [existing sentiment analysis code] ...

    # Language detection
    detected_lang = detect(text)
    return {'rate': rate, 'language': detected_lang}