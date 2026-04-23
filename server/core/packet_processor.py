from typing import Optional 


def process_packet_data(event: dict) -> Optional[dict]:

    if not event:
        return None

    protocol = event.get("protocol", "").upper()

    if protocol not in ["TCP", "UDP", "ICMP"]:
        protocol = "OTHER"

    event["protocol"] = protocol

    event["src_port"] = event.get("src_port", 0)
    event["dst_port"] = event.get("dst_port", 0)

    event["processed"] = True

    return event