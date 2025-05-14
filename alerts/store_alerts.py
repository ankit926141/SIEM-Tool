def save_alert(message):
    with open("alerts/alerts.log", "a") as f:
        f.write(message + "\n")
    print(f"Alert saved: {message}")