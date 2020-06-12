"""
@author: JOFIN F ARCHBALD
@version: 1.0
"""
import requests

data = {
    "author": "Jofin",
    "content": {
        "username": "Notildore",
        "email_id": "Notildore@gmail.com",
        "blogs": ["Python oops", "Java Blockchain", "C++ waste"],
        "result": dict(cpp=0, python=0, java=0)
    }
}
res = requests.request("POST", 'http://127.0.0.1:5000/bc/mine', json=data)
print(res.status_code)
print(res.text)
