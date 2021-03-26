import json

orders = []

class OrderMsg:
    def __init__(self):
        from strategy_monitor_server.strategy_info import Direction,OpenClose
        self._order_id = ""
        self._strategy_name = ""
        self._instrument_id = ""
        self._direction = Direction.LONG
        self._open_close = OpenClose.OPEN
        self._qty = 0
        self._leave_qty = 0
        self._status = "正常"

def query_orders(json_str):
    obj = json.loads(json_str)
    start_index = obj["StartIndex"]
    query_orders = orders[start_index:]
    return json.dumps(query_orders)