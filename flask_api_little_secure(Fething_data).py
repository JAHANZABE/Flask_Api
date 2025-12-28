import requests

Headers = {
    "X-API-KEY": "JZapi-Key"
}

r = requests.get("https://jahanzabekhan.pythonanywhere.com/sAPI/A1", headers=Headers)
print(r.status_code)
print(r.text)
