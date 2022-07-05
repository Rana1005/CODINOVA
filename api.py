from email import header
import requests
import json

URL = "http://127.0.0.1:8000/"

def post_data(id = None):
    data={
        'name':'Devika',
        'email':'Devikarana@gmail.com',
        'dob': "2022-05-03",
        'gender':'female',
        'imgcheck':'test.png'
    }
    
    json_data = json.dumps(data)
    r = requests.post(url= URL, data=json_data)
    data=r.json()
    print(data)

post_data()