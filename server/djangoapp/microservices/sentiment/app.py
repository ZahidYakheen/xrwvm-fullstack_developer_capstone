from flask import Flask, request, jsonify
from flask_cors import CORS
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

app = Flask(__name__)
CORS(app)

try:
    nltk.data.find('vader_lexicon')
except LookupError:
    nltk.download('vader_lexicon')

sid = SentimentIntensityAnalyzer()

@app.route('/')
def home():
    return "Sentiment Analyzer API is running!"

@app.route('/analyze/<string:text>')
def analyze(text):
    scores = sid.polarity_scores(text)
    if scores['compound'] >= 0.05:
        sentiment = 'positive'
    elif scores['compound'] <= -0.05:
        sentiment = 'negative'
    else:
        sentiment = 'neutral'
    return jsonify({'sentiment': sentiment, 'scores': scores})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=True)
