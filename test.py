import time
import random

from strategy_monitor_server import monitor_server,strategy_info
from strategy_monitor_server.strategy_info import Direction,DateType,OpenClose

def run_test():
    monitor_server.run_server(9527)
    strategy1 = strategy_info.new_strategy_info("stg1")
    strategy2 = strategy_info.new_strategy_info("stg2")
    strategy3 = strategy_info.new_strategy_info("stg3")
    while True:
        # position
        update_position(strategy1,"TA109")
        update_position(strategy1,"Y2201")
        update_position(strategy1,"rb2105")
        update_position(strategy2,"TA109")
        update_position(strategy2,"Y2201")
        update_position(strategy2,"rb2105")
        update_position(strategy3,"TA109")
        update_position(strategy3,"Y2201")
        update_position(strategy3,"rb2105")
        #order
        new_order_msg(strategy1)
        new_order_msg(strategy2)
        new_order_msg(strategy3)
        #log
        new_log_msg(strategy1)
        new_log_msg(strategy2)
        new_log_msg(strategy3)
        #延时
        print("等待。。。")
        time.sleep(10)


def update_position(strategy,instrument):
    vol = random.randint(1,100)
    strategy.update_position(instrument,Direction.LONG,DateType.TD,vol)
    vol = random.randint(1,100)
    strategy.update_position(instrument,Direction.LONG,DateType.YD,vol)
    vol = random.randint(1,100)
    strategy.update_position(instrument,Direction.SHORT,DateType.TD,vol)
    vol = random.randint(1,100)
    strategy.update_position(instrument,Direction.SHORT,DateType.YD,vol)

def new_order_msg(strategy):
    oid = "id_" + str(random.randint(1,30))
    oqty = random.randint(1,100)
    strategy.add_or_update_order(
        order_id = oid
        ,instrument_id = "TA109"
        ,direction = Direction.LONG
        ,open_close = OpenClose.OPEN
        ,qty = oqty
        ,leave_qty = 1
        ,status = "正常"
    )

count = 0
def new_log_msg(strategy):
    global count
    count+=1
    strategy.add_log("日志："+str(count))