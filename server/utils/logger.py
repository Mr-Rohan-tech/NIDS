import logging
import os

# Create logs directory
os.makedirs("logs", exist_ok=True)

# SYSTEM LOGGER (events)
system_logger = logging.getLogger("system_logger")
system_logger.setLevel(logging.INFO)

system_handler = logging.FileHandler("logs/system.log")
system_handler.setFormatter(
    logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
)

system_logger.addHandler(system_handler)


# ALERT LOGGER (alerts only)
alert_logger = logging.getLogger("alert_logger")
alert_logger.setLevel(logging.WARNING)

alert_handler = logging.FileHandler("logs/alerts.log")
alert_handler.setFormatter(
    logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
)

alert_logger.addHandler(alert_handler)


# Functions
def log_event(event):
    system_logger.info(f"EVENT: {event}")


def log_alert(threat, event):
    alert_logger.warning(f"ALERT: {threat} | EVENT: {event}")