import zmq
import sys
import _thread
import json
from Crypto.Cipher import AES
from strategy_monitor_server import strategy_info
from strategy_monitor_server import log_msg
from strategy_monitor_server import order_msg
from strategy_monitor_server import config

deal_funs = {}

def run_server():
    _thread.start_new_thread(run_thread)

def run_thread():
    #注册子处理函数
    reg_deal_fun
    #启动服务
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind(f"tcp://*:{config.PORT}")
    while True:
        try:
            json_bytes = socket.recv()
            json_str = decrypt(json_bytes).decode()
            result = deal_msg(json_str)
            socket.send(result)
        except Exception as e:
            print('异常:',e)

#解密
def decrypt(content):
    iv = "hqiFLiPTJkk9xDSA".encode()
    key = config.PASSWORD.encode()
    while len(key) % 16 != 0:
        key += b'\x00'
    aes = AES.new(config.PASSWORD,AES.MODE_CBC,iv)
    return aes.decrypt(content)

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