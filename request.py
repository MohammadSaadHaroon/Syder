import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={ 'Obtain marks':80, 'Time':60})

print(r.json())