from strategy_monitor_server import order_msg
from strategy_monitor_server import log_msg
import json

#策略字典
strategys = {}

#创建策略信息
def new_strategy_info(name):
    strategy = strategys.get(name,StrategyInfo())
    strategys.setdefault(name,strategy)
    return strategy

#策略信息
class StrategyInfo:
    def __init__(self):
        self._name = ""
        self._profile = 0
        self._positions = {}
    
    #更新持仓信息
    def update_position(self,instrument_id,direction,date_type,vol):
        position = self._positions.get(instrument_id,PositionInfo())
        if direction == Direction.LONG:
            if date_type == DateType.TD:
                position._td_long = vol
            else:
                position._yd_long = vol
        else:
            if date_type == DateType.TD:
                position._td_short = vol
            else:
                position._yd_short = vol
        self._positions.setdefault(instrument_id,position)

    #增加或更新订单消息
    def add_or_update_order(self,order_id,instrument_id,direction,open_close,qty,leave_qty,status):
        order = order_msg.OrderMsg()
        order._strategy_name = self._name
        order._order_id = order_id
        order._instrument_id = instrument_id
        order._direction = direction
        order._open_close = open_close
        order._qty = qty
        order._status = status
        order_msg.orders.append(order)
    
    #增加日志
    def add_log(self,log):
        info = log_msg.LogMsg()
        info._strategy_name = self._name
        info._content = log
        log_msg.logs.append(info)

#查询策略
def query_strategys(json_str):
    return json.dumps(strategys)

#持仓信息
class PositionInfo:
    def __init__(self):
        self._strategy_name = ""
        self._instrument_id = ""
        self._td_long = 0
        self._td_short = 0
        self._yd_long = 0
        self._yd_short = 0

#持仓方向
class Direction:
    LONG="多"
    SHORT="空"

#开平
class OpenClose:
    OPEN="开"
    CLOSE="平"

#持仓类型
class DateType:
    YD="今"
    TD="昨"
