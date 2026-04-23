from capture.network_sniffer import start_sniffing
from agent.sender import send_event

def handle_event(event):
    if event:
        send_event(event)

if __name__ == "__main__":
    print("[AGENT] Real-time IDS started...")
    start_sniffing(handle_event)