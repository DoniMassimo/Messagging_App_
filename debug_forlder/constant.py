import socket
import jsbeautifier
import json
from threading import Thread, Event
import time


PORT = 5050
SERVER = '192.168.3.66'
ADDR = (socket.gethostbyname(socket.gethostname()), PORT)
FORMAT = 'utf-8'
HEADER = 64

PING = '->'
COMMAND = '&&DO:'
OUTCOME = '&&OC:'  #* OUCOME ARGS KEY
NOTIFYCATION = '&&NO:'


#* COMMAND CONSTANT
DISCONNECT = 'DISCONNECT'
DISCONNECT_TO = 'DISCONNECT_TO'
CONNECT_TO = 'CONNECT_TO'
SEND_MSG = 'SEND_MSG'
SET_NAME = 'SET_NAME'

#* OUTCOME CONSTANT
SUCCESS = 'SUCCESS'
FAILED = 'FAILED'

#* NOTIFICATIONS CONSTANT
MESSAGE = 'MESSAGE'

#* MESSAGE ARGS KEY
SENDER = 'SENDER'
RECIPIENT = 'RECIPIENT'

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

