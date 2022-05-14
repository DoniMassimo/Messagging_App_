import constant as const
import socket
import json
from threading import Thread, Event


class Client: 
    def __init__(self) -> None:
        self._server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self._server.connect(const.ADDR)
            print('connesso')
            self._start_client = Thread(target=self._start).start()
        except socket.error:
            print('[ERRORE]: impossibile connettersi al server')
        self._name = ''  
        self._coll_events = {  # collections of event
            'name_set':{
                'event':Event()                
            },
            'name_check':{
                'event':Event(),
                'info':''
            }
        }        

    def _start(self):
        Thread(target=self._wait_name_check).start() # fa partire un thread che controlla se il nome è gia stato scelto    
        while True:
            recv_mess = self._recive()            
            if recv_mess[const.TYPE_KEY] == const.COMMAND:
                pass
            elif recv_mess[const.TYPE_KEY] == const.OUTCOME:
                self._exe_outcome(recv_mess)

    def _wait_name_check(self): # aspette che il nome si stato verificato dal server
        while True:
            self._coll_events['name_set']['event'].wait()
            self._coll_events['name_set']['event'].clear()
            self._send(const.COMMAND, const.SET_NAME, [self._name])            
            self._coll_events['name_check']['event'].wait()            
            if self._coll_events['name_check']['info'] == const.SUCCESS:
                break

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

    def _exe_outcome(self, outcome):
        match outcome[const.SPECIFIC_KEY]:
            case const.SET_NAME: # setta l'evento e aggiunge delle info, come ad esempio se il nome è già preso
                self._coll_events['name_check']['info'] = outcome[const.ARGS_KEY][0]
                self._coll_events['name_check']['event'].set()

    #?#### PUBLIC FUNCTION
    def set_name(self, name):
        self._name = name
        self._coll_events['name_set']['event'].set()
        self._coll_events['name_check']['event'].wait()
        if self._coll_events['name_check']['info'] == const.SUCCESS:
            return True
        else:
            return False

    def disconnect(self):
        pass

    def disconnect_to(self):
        pass
    
    def connect_to(self):
        pass

    def send_message(self, recipient, message):
        self._send(const.COMMAND, const.SEND_MSG, [recipient, message])

    def debug_func(self, command): 
        command = command.split('-')
        if command[0] == 'setn': # set name-name
            if self.set_name(command[1]) == True:
                print(f'[OUTPUT-SUCCESS]: impostazione nome <{command[1]}> eseguita con successo!')
            else:
                print(f'[OUTPUT-FAILED]: impostazione nome <{command[1]}> fallita!')
        elif command[0] == 'send': # recipient-message
            self.send_message(command[1], command[2])


def start_client():
    pass


if __name__ == '__main__':        
    cl = Client()
    while True:
        cl.debug_func(input('Debug command: '))
    
