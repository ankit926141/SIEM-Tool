import json

def store_log(entry):
    with open("storage/parsed_logs.json", "a") as f:
        f.write(json.dumps(entry) + "\n")
