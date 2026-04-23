from detection.rule_engine import detect_rules

def test_detection():

    # Simulate multiple requests (DDoS)
    event = {
        "timestamp": "2026-03-24",
        "src_ip": "10.0.0.1",
        "dst_ip": "192.168.1.1",
        "protocol": "TCP",
        "src_port": 1234,
        "dst_port": 80,
        "length": 500
    }

    for i in range(60):
        threat = detect_rules(event)

    print("Detected:", threat)