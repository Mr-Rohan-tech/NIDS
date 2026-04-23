from collections import defaultdict
import time

brute_force_tracker = defaultdict(list)

BRUTE_THRESHOLD = 15
BRUTE_WINDOW = 30

# 🔥 ONLY REAL LOGIN PORTS
TARGET_PORTS = {22, 21, 3389, 23}


def detect_bruteforce(event):
    src_ip = event.get("src_ip")
    dst_port = event.get("dst_port")

    # Ignore non-login ports
    if dst_port not in TARGET_PORTS:
        return None

    now = time.time()

    brute_force_tracker[src_ip].append(now)

    brute_force_tracker[src_ip] = [
        t for t in brute_force_tracker[src_ip]
        if now - t < BRUTE_WINDOW
    ]

    if len(brute_force_tracker[src_ip]) > BRUTE_THRESHOLD:
        return f"Brute force attack detected on port {dst_port} from {src_ip}"

    return None