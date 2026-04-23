from typing import Optional
from core.packet_processor import process_packet_data
from core.event_manager import add_event
from detection.rule_engine import detect_rules
from response.notification import send_alert
from utils.logger import log_event
from database.repository import save_event, save_alert




def process_event(event: dict):

    processed_event = process_packet_data(event)

    if processed_event is None:
        return

    log_event(processed_event)
    add_event(processed_event)

    # 🔥 SAVE EVENT
    save_event(processed_event)

    threat = detect_rules(processed_event)

    if threat:
        send_alert(processed_event, threat)

        # 🔥 SAVE ALERT
        save_alert(processed_event, threat)