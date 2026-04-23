from database.repository import save_event

def test_db():

    event = {
        "timestamp": "2026-03-24",
        "src_ip": "1.1.1.1",
        "dst_ip": "2.2.2.2",
        "protocol": "TCP",
        "src_port": 123,
        "dst_port": 80,
        "length": 100
    }

    save_event(event)

    print("Event saved to DB ✔")