from database.db import get_connection


def save_event(event):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO events (timestamp, src_ip, dst_ip, protocol, src_port, dst_port, length)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (
        event.get("timestamp"),
        event.get("src_ip"),
        event.get("dst_ip"),
        event.get("protocol"),
        event.get("src_port"),
        event.get("dst_port"),
        event.get("length"),
    ))

    conn.commit()
    cursor.close()
    conn.close()


def save_alert(event, threat):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO alerts (timestamp, src_ip, threat, details)
    VALUES (%s, %s, %s, %s)
    """, (
        event.get("timestamp"),
        event.get("src_ip"),
        threat,
        str(event),
    ))

    conn.commit()
    cursor.close()
    conn.close()
    
    
def get_events(limit=50):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM events
    ORDER BY id DESC
    LIMIT %s
    """, (limit,))

    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return rows


def get_alerts(limit=50):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM alerts
    ORDER BY id DESC
    LIMIT %s
    """, (limit,))

    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return rows