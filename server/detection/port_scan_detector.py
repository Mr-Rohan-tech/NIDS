from collections import defaultdict
import time

port_scan_tracker = defaultdict(list)

PORT_SCAN_THRESHOLD = 10
PORT_SCAN_WINDOW = 10

def detect_port_scan(event):
    src_ip = event.get("src_ip")
    dst_port = event.get("dst_port", 0)

    now = time.time()

    port_scan_tracker[src_ip].append((dst_port, now))

    port_scan_tracker[src_ip] = [
        (p, t) for (p, t) in port_scan_tracker[src_ip]
        if now - t < PORT_SCAN_WINDOW
    ]

    unique_ports = {p for (p, _) in port_scan_tracker[src_ip]}

    if len(unique_ports) > PORT_SCAN_THRESHOLD:
        return f"Port scan detected from {src_ip}"

    return None