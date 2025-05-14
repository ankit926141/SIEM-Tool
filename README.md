# 🔐 Simple SIEM Tool (Security Information and Event Management)

A lightweight and educational Security Information and Event Management (SIEM) system built with Python and Flask. This project monitors system logs in real-time, detects suspicious activity (like failed logins or blacklisted IPs), and provides a simple web dashboard to view parsed logs and alerts.

---

## 📌 Features

- 🧠 Real-time log monitoring using `watchdog`
- 📝 Log parsing with regex-based extractor
- 🚨 Rule-based threat detection engine
- 💾 Local storage for logs and alerts
- 🌐 Web dashboard using Flask (view logs/alerts in browser)
- ⚙️ Easily extendable: add more parsing rules, alert conditions, and integrations

---

## 🧱 Project Structure

siem-tool/
├── main.py # Watches log file and processes new entries
├── app.py # Flask dashboard for viewing logs and alerts
├── requirements.txt # Dependencies
│
├── logs/
│ └── system.log # Source log file being monitored
├── storage/
│ └── parsed_logs.json # Parsed logs stored in JSON format
├── alerts/
│ └── alerts.log # Triggered alerts saved here
│
├── parsers/
│ └── basic_parser.py # Log line parser
├── rules/
│ └── detector.py # Custom threat detection rules
├── alerts/
│ └── store_alerts.py # Writes alerts to log file



---

## 🚀 Use Cases

| Scenario | How This SIEM Helps |
|----------|---------------------|
| 🔍 Detect brute-force attempts | Tracks multiple failed login events |
| ⚠️ Flag risky IPs | Alerts on blacklisted IP addresses |
| 📚 Learn cybersecurity basics | Great for understanding log parsing, threat detection, and SIEM concepts |
| 🛠️ Prototype alerting systems | Acts as a starter SIEM pipeline for real deployments |

---

## 🔧 Setup Instructions

1. **Clone the repo** (or create a new Codespace)
2. **Install dependencies** (Flask pre-installed in Codespaces):
    ```bash
    pip install watchdog
    ```

3. **Run Flask dashboard** (in Terminal 1):
    ```bash
    python app.py
    ```

4. **Run the log watcher** (in Terminal 2):
    ```bash
    python main.py
    ```

5. **Simulate a log entry** (in Terminal 3):
    ```bash
    echo "[2025-05-14 12:00:00] LOGIN_FAILED user=admin ip=192.168.1.10" >> logs/system.log
    ```

6. **View results**:
    - Go to the browser preview in Codespaces
    - `/logs` → View parsed logs
    - `/alerts` → View triggered alerts

---

## 📌 Example Log Format

Each line in `system.log` should look like:



[2025-05-14 12:00:00] LOGIN_FAILED user=admin ip=192.168.1.10

yaml
Copy
Edit

---

## 🧠 How It Works (Flow)

1. `main.py` watches `logs/system.log` for changes.
2. New log lines are passed to `basic_parser.py`.
3. Parsed logs are saved to `parsed_logs.json`.
4. `detector.py` checks the parsed data against security rules.
5. If threats are detected, alerts are saved to `alerts.log`.
6. `app.py` serves a Flask dashboard at `/logs` and `/alerts`.

---

## 🌱 Future Improvements (Ideas)

- [ ] Add rate-limiting detection (e.g., multiple login failures in short time)
- [ ] Integrate email or Slack alerting
- [ ] Add a frontend UI with charts (maybe using React or Bootstrap)
- [ ] Load rules from YAML/JSON
- [ ] Add log rotation & archiving
- [ ] Add authentication to dashboard

---

## 📖 Learn More

- [What is a SIEM?](https://en.wikipedia.org/wiki/Security_information_and_event_management)
- [MITRE ATT&CK](https://attack.mitre.org/) — a global knowledge base of adversary behavior
- [Syslog Format](https://tools.ietf.org/html/rfc5424)

---

## 👨‍💻 Author

Built by [Your Name] as a beginner-friendly cybersecurity project to understand how a SIEM system works.

Feel free to fork, star, and contribute!

---
