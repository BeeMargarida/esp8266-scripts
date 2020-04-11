# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
# import uos
#uos.dupterm(None, 1) # disable REPL on UART(0)
import gc
#import webrepl
#webrepl.start()
#gc.collect()

##############################

import wifi
from server import Server

wifi.connect()
server = Server()
