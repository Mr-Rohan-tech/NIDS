import requests

def test_ingest_api():
    url = "http://127.0.0.1:8000/ingest"

    test_event = {
        "timestamp": "2026-03-24",
        "src_ip": "192.168.1.100",
        "dst_ip": "192.168.1.1",
        "protocol": "TCP",
        "src_port": 1234,
        "dst_port": 80,
        "length": 500
    }

    response = requests.post(url, json=test_event)

    print("Status:", response.status_code)
    print("Response:", response.text)