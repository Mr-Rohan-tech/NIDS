from detection.port_scan_detector import detect_port_scan

def test_port_scan():

    event = {
        "src_ip": "10.0.0.2",
        "dst_port": 0
    }

    # simulate multiple ports
    for port in range(20):
        event["dst_port"] = port
        threat = detect_port_scan(event)

    print("Port Scan:", threat)