from scapy.all import sniff
from datetime import datetime


def process_packet(packet):
    try:
        # Process only IP packets
        if not packet.haslayer("IP"):
            return None

        ip_layer = packet["IP"]

        # Ignore broadcast traffic
        if ip_layer.dst == "255.255.255.255":
            return None

        # Initialize defaults
        proto = "OTHER"
        src_port = 0
        dst_port = 0

        # Detect protocol and ports
        if packet.haslayer("TCP"):
            proto = "TCP"
            src_port = packet["TCP"].sport
            dst_port = packet["TCP"].dport

        elif packet.haslayer("UDP"):
            proto = "UDP"
            src_port = packet["UDP"].sport
            dst_port = packet["UDP"].dport

        elif packet.haslayer("ICMP"):
            proto = "ICMP"

        # Create structured event
        event = {
            "timestamp": str(datetime.now()),
            "src_ip": ip_layer.src,
            "dst_ip": ip_layer.dst,
            "protocol": proto,
            "src_port": src_port,
            "dst_port": dst_port,
            "length": len(packet)
        }

        return event

    except Exception:
        return None


def start_scapy_sniff(callback):
    sniff(
        prn=lambda pkt: callback(process_packet(pkt)),
        store=False,
        filter="ip",          # Capture only IP packets
        promisc=True          # Enable promiscuous mode (more visibility)
    )