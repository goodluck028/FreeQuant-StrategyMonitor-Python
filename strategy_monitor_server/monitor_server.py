import zmq
import sys
import _thread
import json
from strategy_monitor_server import strategy_info
from strategy_monitor_server import log_msg
from strategy_monitor_server import order_msg

deal_funs = {}

def run_server(port):
    _thread.start_new_thread(run_thread,(port,))

def run_thread(port):
    #注册子处理函数
    reg_deal_fun
    #启动服务
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind(f"tcp://*:{port}")
    while True:
        try:
            json_str = socket.recv()
            result = deal_msg(json_str)
            socket.send(result)
        except Exception as e:
            print('异常:',e)

#注册子处理函数
def reg_deal_fun():
    deal_funs["StrategyQuery"] = strategy_info.query_strategys
    deal_funs["LogQuery"] = log_msg.query_logs
    deal_funs["OrderQuery"] = order_msg.query_orders

#处理消息
def deal_msg(json_str):
    msg = json.loads(json_str)
    fun = deal_funs[msg["ClassName"]]
    return fun(msg["JsonObj"])