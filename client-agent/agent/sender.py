import requests

URL = "http://127.0.0.1:8000/api/ingest/"

def send_event(event):
    try:
        res = requests.post(URL, json=event)
        print("[SENT]", res.json())
    except Exception as e:
        print("[ERROR]", e)