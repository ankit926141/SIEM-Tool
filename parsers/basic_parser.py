import re

def parse_log(line):
    pattern = r"\[(.*?)\] (\w+) user=(\w+) ip=(\d+\.\d+\.\d+\.\d+)"
    match = re.match(pattern, line)
    if match:
        return {
            "timestamp": match.group(1),
            "event": match.group(2),
            "user": match.group(3),
            "ip": match.group(4)
        }
    return None
