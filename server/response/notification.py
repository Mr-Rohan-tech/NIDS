from utils.logger import log_alert

def send_alert(event, threat):
    print("\n🚨 ALERT 🚨")
    print(f"Threat: {threat}")
    print(f"Event: {event}")
    print("-" * 50)

    # Log alert
    log_alert(threat, event)