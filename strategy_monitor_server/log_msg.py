import time
import json

logs = []

class LogMsg:
    def __init__(self):
        self._strategy_name = ""
        self._time = round(time.time()*1000)
        self._content = ""

def query_logs(json_str):
    obj = json.loads(json_str)
    start_index = obj["StartIndex"]
    query_logs = logs[start_index:]
    return json.dumps(query_logs)