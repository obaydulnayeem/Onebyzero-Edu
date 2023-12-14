import requests
import json

URL = "http://127.0.0.1:8000/study/create_course/"

data = {
    'id' : 24,
    "title": "Python-updated2",
    # "code": "PY100updated",
    "credit": 2.0,
}

json_data = json.dumps(data) # converting python to json
r = requests.put(url = URL, data = json_data)
data = r.json() # extracting the request
print(data)
