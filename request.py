import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'SepalLengthCm':4.2, 'SepalWidthCm':3.2, 'PetalLengthCm':1.7,'PetalWidthCm':0.9})

print(r.json())
