import requests
import json
from transformers import BertTokenizer, BertForSequenceClassification
from transformers import pipeline

def sentiment_analyzer(text_to_analyze):
    # Load pre-trained model and tokenizer
    model_name = "nlptown/bert-base-multilingual-uncased-sentiment"
    tokenizer = BertTokenizer.from_pretrained(model_name)
    model = BertForSequenceClassification.from_pretrained(model_name)

    # Create a sentiment-analysis pipeline
    nlp = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)

    # Perform sentiment analysis
    results = nlp(text_to_analyze)

    # Extract sentiment label and score from the results
    label = results[0]['label']
    score = results[0]['score']

    # Return a dictionary containing sentiment analysis results
    return {'label': label, 'score': score}



