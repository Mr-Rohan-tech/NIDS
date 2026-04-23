import logging
import os

# Create logs folder if not exists
os.makedirs("logs", exist_ok=True)

# Configure logger
logging.basicConfig(
    filename="logs/system.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def log_event(event):
    logging.info(f"EVENT: {event}")

def log_alert(threat, event):
    logging.warning(f"ALERT: {threat} | EVENT: {event}")