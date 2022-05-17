from client_server import constant as const
import socket
import json
from threading import Thread, Event
from queue import Queue
import debug_forlder  



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
            'name_set': {
                'event': Event()
            },
            'name_check': {
                'event': Event(),
                'info': ''
            },
            'new_mess': {
                'call': None,  # function, guarda la documentazioe per sapere i parametri passati
                'info': Queue()
            },
            'disconnect': {
                'event': Event()
            }
        }

    def _start(self):
        # fa partire un thread che controlla se il nome è gia stato scelto
        Thread(target=self._wait_name_check).start()
        while True:
            if self._coll_events['disconnect']['event'].is_set():
                break
            recv_mess = self._recive()
            if recv_mess[const.TYPE_KEY] == const.COMMAND:
                pass
            elif recv_mess[const.TYPE_KEY] == const.OUTCOME:
                self._exe_outcome(recv_mess)
            elif recv_mess[const.TYPE_KEY] == const.NOTIFYCATION:
                self._exe_notification(recv_mess)
        self._server.close()
        self = None

    def _wait_name_check(self):  # aspette che il nome si stato verificato dal server
        while True:
            self._coll_events['name_set']['event'].wait()
            self._coll_events['name_set']['event'].clear()
            self._send(const.COMMAND, const.SET_NAME, {const.NAME: self._name})
            self._coll_events['name_check']['event'].wait()
            if self._coll_events['name_check']['info'] == const.SUCCESS:
                break

    def _send(self, type_, specific, arguments: dict) -> None:
        message = {const.TYPE_KEY: type_, const.SPECIFIC_KEY: specific,
                   const.ARGS_KEY: arguments}  # creo il pacchetto
        message = json.dumps(message)  # lo trasform in un json
        message = message.encode(const.FORMAT)
        msg_lenght = len(message)
        send_lenght = str(msg_lenght).encode(const.FORMAT)
        send_lenght += b' ' * (const.HEADER - len(send_lenght))
        self._server.send(send_lenght)
        self._server.send(message)

    def _recive(self) -> dict:
        msg_lenght = self._server.recv(const.HEADER).decode(
            const.FORMAT)  # riceve prima la lunghezza del messaggio
        if msg_lenght:
            # riceve il messaggio in base alla sua lunghezza
            msg_lenght = int(msg_lenght)
            message = self._server.recv(msg_lenght).decode(const.FORMAT)
            message = json.loads(message)  # lo ritrasformo in un dictionary
            return message

    def _exe_command(self, packet):
        pass

    def _exe_outcome(self, packet):
        match packet[const.SPECIFIC_KEY]:
            case const.SET_NAME:  # setta l'evento e aggiunge delle info, come ad esempio se il nome è già preso
                self._coll_events['name_check']['info'] = packet[const.ARGS_KEY][const.OUTCOME]
                self._coll_events['name_check']['event'].set()
            case const.DISCONNECT:
                self._coll_events['disconnect']['event'].set()

    def _exe_notification(self, packet):
        match packet[const.SPECIFIC_KEY]:
            case const.MESSAGE:
                self._coll_events['new_mess']['call'](
                    packet[const.ARGS_KEY][const.MESSAGE], packet[const.ARGS_KEY][const.SENDER])

    # ?#### PUBLIC FUNCTION

    def set_name(self, name):
        self._name = name
        self._coll_events['name_set']['event'].set()
        self._coll_events['name_check']['event'].wait()
        if self._coll_events['name_check']['info'] == const.SUCCESS:
            return True
        else:
            self._coll_events['name_set']['event'].clear()
            self._coll_events['name_check']['event'].clear()
            return False

    def set_event(self, new_message):
        self._coll_events['new_mess']['call'] = new_message

    def disconnect(self):
        self._send(const.COMMAND, const.DISCONNECT, {})

    def disconnect_to(self):
        pass

    def connect_to(self):
        pass

    def send_message(self, recipient, message):
        self._send(const.COMMAND, const.SEND_MSG, {const.SENDER: self._name,
                                                   const.RECIPIENT: recipient, const.MESSAGE: message})

    def debug_func(self, command):
        command = command.split('-')
        if command[0] == 'setn':  # set name-name
            if self.set_name(command[1]) == True:
                print(
                    f'[OUTPUT-SUCCESS]: impostazione nome <{command[1]}> eseguita con successo!')
            else:
                print(
                    f'[OUTPUT-FAILED]: impostazione nome <{command[1]}> fallita!')
        elif command[0] == 'send':  # recipient-message
            self.send_message(command[1], command[2])
        elif command[0] == 'diss':  # disconnect-server
            self.disconnect()
            return True
        else:
            print('COMANDO NON RICONOSCIUTO!!!')


class gui:
    def __init__(self) -> None:
        self.cl = Client()
        self.cl.set_event(new_message=self.message)
        self.start_input = Thread(target=self.input_).start()

    def input_(self):
        while True:
            if self.cl.debug_func(input('Debug command: ')) == True:
                break

    def message(self, msg, sender_name):
        print(f'[message from {sender_name}]: {msg}')

def start():
    gui_obj = gui()

if __name__ == '__main__':
    gui_obj = gui()
