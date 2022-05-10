import constant as const
import socket
import json


class Client: # basic client 
    def __init__(self) -> None:
        self._server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._server.connect(const.ADDR)

    def _send(self, type_, specific, arguments:list) -> None:
        message = {const.TYPE_KEY:type_, const.SPECIFIC_KEY:specific, const.ARGS_KEY:arguments} # creo il pacchetto
        message = json.dumps(message) # lo trasform in un json
        message = message.encode(const.FORMAT)
        msg_lenght = len(message)
        send_lenght = str(msg_lenght).encode(const.FORMAT)
        send_lenght += b' ' * (const.HEADER - len(send_lenght))
        self._server.send(send_lenght)
        self._server.send(message)     

    def _recive(self) -> dict:
        msg_lenght = self._server.recv(const.HEADER).decode(const.FORMAT) # riceve prima la lunghezza del messaggio 
        if msg_lenght:
            msg_lenght = int(msg_lenght)
            message = self._server.recv(msg_lenght).decode(const.FORMAT) # riceve il messaggio in base alla sua lunghezza
            message = json.loads(message) # lo ritrasformo in un dictionary
            return message

    def disconnect(self):
        pass

    def disconnect_to(self):
        pass
    
    def connect_to(self):
        pass

    def send_message(self, msg):
        self._send(const.COMMAND_TYPE, const.SEND_SRV, [msg])

    def debug_func(self, command):
        command = command.split('-')
        if command[0] == 'send':
            self.send_message(command[1])


if __name__ == '__main__':
    cl = Client()
    while True:
        cl.debug_func(input('Debug command: '))
    
