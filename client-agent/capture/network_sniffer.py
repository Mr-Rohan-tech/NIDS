import platform

def start_sniffing(callback):
    os_type = platform.system()

    try:
        if os_type in ["Linux", "Darwin", "Windows"]:
            from capture.scapy_sniffer import start_scapy_sniff
            print(f"[INFO] Using Scapy Sniffer on {os_type}")
            start_scapy_sniff(callback)

    except Exception as e:
        print("[WARNING] Sniffer failed:", e)

        from capture.fallback_monitor import start_fallback
        start_fallback(callback)