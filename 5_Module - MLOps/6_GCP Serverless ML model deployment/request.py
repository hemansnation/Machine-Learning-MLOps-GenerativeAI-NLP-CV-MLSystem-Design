import requests

url = 'https://us-east1-mlops-ml-models.cloudfunctions.net/sentiment_analysis_function'

a = input("Enter your string: ")

r = requests.post(url, json={
    "model":["DecisionClassifier"],
    "x":[a]
})

print(r.text)