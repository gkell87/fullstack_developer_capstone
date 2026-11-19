# Uncomment the imports below before you add the function code
import requests
import os
from dotenv import load_dotenv

load_dotenv()

backend_url = os.getenv(
    'backend_url', default="https://sentianalyzer.2hd4e1b0i008.us-south.codeengine.appdomain.cloud/")
sentiment_analyzer_url = os.getenv(
    'sentiment_analyzer_url',
    default="http://localhost:5050/")

# *kwargs means keyword arguments
def get_request(endpoint, **kwargs):
    params = ''
    if (kwargs):
        for key, value in kwargs.item():
            params = params+key+'='+'&'

    request_url = backend_url+endpoint+'?'+params

    print("GET from {} ".format(request_url))
    try:
        # Call get method of requests library with URL and parameters
        response = requests.get(request_url)
        return response.json()
    except:
        # If any error eccurs
        print('Network Error Occured...')

# Create Sentiment Analyzer Puzzle
def analyze_review_sentiments(text):
    request_url = sentiment_analyzer_url+"analyze/"+text
    try:
        # call the GET method with URL an params
        response = requests.get(request_url)
        return response.json()
    except Exception as err:
        print(f"Unexpected {err = }, {type(err) = }")
        print('Network Exception Occured...')

def post_review(data_dict):
    request_url = backend_url+'/insert_review'
    try:
        response = requests.post(request_url, json = data_dict)
        print(response.json())
        return response.json()
    except:
        print('Network Exception Occurrerd...')