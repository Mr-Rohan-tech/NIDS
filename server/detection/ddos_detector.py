from collections import defaultdict
import time

ddos_tracker = defaultdict(list)

DDOS_THRESHOLD = 150   # 🔥 increased
DDOS_WINDOW = 5


def detect_ddos(event):
    src_ip = event.get("src_ip")

    # Ignore small packets (noise)
    if event.get("length", 0) < 60:
        return None

    now = time.time()

    ddos_tracker[src_ip].append(now)

    ddos_tracker[src_ip] = [
        t for t in ddos_tracker[src_ip]
        if now - t < DDOS_WINDOW
    ]

    if len(ddos_tracker[src_ip]) > DDOS_THRESHOLD:
        return f"DDoS attack detected from {src_ip}"

    return None