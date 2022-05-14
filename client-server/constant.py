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
OUTCOME = '&&OC:'
NOTIFYCATION = '&&NO:'


# DEFAULT_MESSAGE = {
#     'COMMAND':{
#         'DISCONNECT':COMMAND_TAG + 'DISCONNECT',
#         'DISCONNECT_TO':COMMAND_TAG + 'DISCONNECT_TO',
#         'CONNECT_TO:':COMMAND_TAG + 'CONNECT_TO:',
#         'SEND_MSG':COMMAND_TAG + 'SEND_MSG',
#         'SEND_SRV':COMMAND_TAG + 'SEND_SRV' #! remove
#     },
#     'OUTCOME':{
#         'SUCCESS':OUTCOME_TAG + 'SUCCESS',
#         'FAILED':OUTCOME_TAG + 'FAILED'
#     }
# }

#* COMMAND CONSTANT
DISCONNECT = 'DISCONNECT',
DISCONNECT_TO = 'DISCONNECT_TO',
CONNECT_TO = 'CONNECT_TO',
SEND_MSG = 'SEND_MSG',
SET_NAME = 'SET_NAME'

#* OUTCOME CONSTANT
SUCCESS = 'SUCCESS'
FAILED = 'FAILED'

#* NOTIFICATIONS CONSTANT
MESSAGE = 'MESSAGE'

# SUCCESS_MSG = OUTCOME_TAG + 'SUCCESS'
# FAILED_MSG = OUTCOME_TAG + 'FAILED'


## DICT KEY

TYPE_KEY = 'TYPE'
SPECIFIC_KEY = 'SPECIFIC'
ARGS_KEY = 'ARGS'

# COMMAND_KEY = 'COMMAND'
# INFO_KEY = 'INFO'
# OUTCOME_KEY = 'OUTCOME'


def print_dict(dict_, info=''):
    print('\n')
    opts = jsbeautifier.default_options()
    opts.indent_size = 2
    print(info + '\n' + jsbeautifier.beautify(json.dumps(dict_), opts=opts))
 