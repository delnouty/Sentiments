# Import Flask, render_template, request from the flask framework package
from flask import Flask, render_template, request, jsonify
# Import the sentiment_analyzer function from the package created
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

# Initiate the flask app
app = Flask(__name__, template_folder='app/templates', static_folder='app/static')

@app.route("/sentimentAnalyzer")
def sent_analyzer():
    ''' This code receives the text from the HTML interface and 
        runs sentiment analysis over it using sentiment_analyzer()
        function. The output returned shows the label and its confidence 
        score for the provided text.
    '''
    text = request.args.get('textToAnalyze')
    result = sentiment_analyzer(text)
    return jsonify(result)

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    ''' This functions executes the flask app and deploys it on localhost:5000
    '''
    app.run(debug=True, host='0.0.0.0', port=5000)
