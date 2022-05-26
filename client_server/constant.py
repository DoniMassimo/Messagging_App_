import json
import socket
import time
from threading import Event, Thread

import jsbeautifier

PORT = 5050
SERVER = '192.168.3.66'
ADDR = (socket.gethostbyname(socket.gethostname()), PORT)
FORMAT = 'utf-8'
HEADER = 64

PING = '->'
COMMAND = 'COMM'
OUTCOME = 'OUTC'  #* OUCOME ARGS KEY
NOTIFYCATION = 'NOTY'


#* COMMAND CONSTANT
DISCONNECT = 'DISCONNECT'
DISCONNECT_TO = 'DISCONNECT_TO'
CONNECT_TO = 'CONNECT_TO'
SEND_MSG = 'SEND_MSG'
SET_NAME = 'SET_NAME'
SEND_FRIEND_REQ = 'SEND_FRIEND_REQ'

#* OUTCOME ARGS
SUCCESS = 'SUCCESS'
FAILED = 'FAILED'

#* NOTIFICATIONS CONSTANT
MESSAGE = 'MESSAGE'
VISUALIZED_MSG = 'VISUALIZED_MSG'
ARRIVEDE_MSG = 'ARRIVED_MSG'

#* MESSAGE ARGS KEY
SENDER = 'SENDER'
RECIPIENT = 'RECIPIENT'
HASH = 'HASH'
ID = 'ID'

#* SET NAME ARGS KEY
NAME = 'NAME'

#* STANDARD PACKET KEY
TYPE_KEY = 'TYPE'
SPECIFIC_KEY = 'SPECIFIC'
ARGS_KEY = 'ARGS'


def print_dict(dict_, info=''):
    print('\n')
    opts = jsbeautifier.default_options()
    opts.indent_size = 2
    print(info + '\n' + jsbeautifier.beautify(json.dumps(dict_), opts=opts))


# class a():
#     def __init__(self) -> None:
#         pass
#     def ciao(self):
#         print('baby')

#     def ei(self):
#         #self.child.ciao()
#         self.ciao()
        

# class b(a):
#     def ciao(self):
#         print('yooooo')

# v = b()
# v.ei()