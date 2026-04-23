from detection.port_scan_detector import detect_port_scan
from detection.ddos_detector import detect_ddos
from detection.brute_force_detector import detect_bruteforce
import time


TRUSTED_IPS = {"192.168.1.1"}

SAFE_PORTS = {53, 67, 68, 123, 137, 138, 139, 445}

LOGIN_PORTS = {21, 22, 23, 3389}


# 🔥 Cooldown system
last_alert_time = {}
COOLDOWN = 30


def is_internal_ip(ip: str):
    return (
        ip.startswith("192.168.") or
        ip.startswith("10.") or
        ip.startswith("172.16.") or
        ip == "127.0.0.1"
    )


def detect_rules(event: dict):

    src_ip = event.get("src_ip")
    dst_port = event.get("dst_port", 0)

    if not src_ip:
        return None

    # 🚫 Ignore trusted IP
    if src_ip in TRUSTED_IPS:
        return None

    # 🚫 Ignore internal traffic (VERY IMPORTANT)
    if is_internal_ip(src_ip):
        return None

    # 🚫 Ignore safe ports
    if dst_port in SAFE_PORTS:
        return None

    # 🚫 Ignore small packets
    if event.get("length", 0) < 40:
        return None

    # 🚫 Cooldown (prevent spam)
    now = time.time()
    if src_ip in last_alert_time:
        if now - last_alert_time[src_ip] < COOLDOWN:
            return None

    # 🔍 Run detectors

    threat = detect_port_scan(event)
    if threat:
        last_alert_time[src_ip] = now
        return threat

    threat = detect_ddos(event)
    if threat:
        last_alert_time[src_ip] = now
        return threat

    if dst_port in LOGIN_PORTS:
        threat = detect_bruteforce(event)
        if threat:
            last_alert_time[src_ip] = now
            return threat

    return None