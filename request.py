import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url, json=['projeto':100, 'dinamica':200, 'enduro':300])

print(r.jason)
