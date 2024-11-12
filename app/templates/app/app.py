""" from SentimentAnalysis import sentiment_analyzer

# Example usage
result = sentiment_analyzer("It's raining cats and gods")
if result:
    print(f"Sentiment: {result['label']}, Score: {result['score']}") """

from flask import Flask, request, render_template, jsonify
from SentimentAnalysis import sentiment_analyzer

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/sentimentAnalyzer', methods=['GET'])
def analyze():
    text = request.args.get('textToAnalyze')
    result = sentiment_analyzer(text)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
