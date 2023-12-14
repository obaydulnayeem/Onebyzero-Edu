import requests
import json

URL = "http://127.0.0.1:8000/study/create_course/"

data = {
    "title": "Djano",
    "code": "Dj100",
    "credit": 3.0,
    "department": 1,
    "year": 3,
    "semester": 2,
    "syllabus": "Django Syllabus",
}


json_data = json.dumps(data) # dump method python object k json e convert kore
r = requests.post(url = URL, data = json_data)
data = r.json()
print(data)