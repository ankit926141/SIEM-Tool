blacklisted_ips = ["192.168.1.10"]

def detect_threat(log):
    alerts = []
    if log["ip"] in blacklisted_ips:
        alerts.append(f"Blacklisted IP detected: {log['ip']}")
    if log["event"] == "LOGIN_FAILED":
        alerts.append(f"Failed login by {log['user']}")
    return alerts
