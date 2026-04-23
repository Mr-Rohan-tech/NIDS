import psutil
import time
from datetime import datetime

def start_fallback(callback):
    print("[INFO] Running fallback monitor...")

    while True:
        connections = psutil.net_connections()

        for conn in connections:
            if conn.raddr:
                event = {
                    "timestamp": str(datetime.now()),
                    "src_ip": conn.laddr.ip if conn.laddr else "unknown",
                    "dst_ip": conn.raddr.ip,
                    "protocol": "TCP",
                    "length": 0
                }

                callback(event)

        time.sleep(2)