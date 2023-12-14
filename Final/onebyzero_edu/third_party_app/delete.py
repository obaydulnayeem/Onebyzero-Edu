import requests
import json

URL = "http://127.0.0.1:8000/study/create_course/"

data = {
    'id' : 23,
}

json_data = json.dumps(data) # converting python to json
r = requests.delete(url = URL, data = json_data)
data = r.json()
print(data)