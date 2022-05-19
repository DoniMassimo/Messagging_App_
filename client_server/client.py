from client_server import constant as const
#import constant as const
from debug_forlder import Multi_level_menu, support_library_v1 as sl

import socket
import json
import os
from threading import Thread, Event
from queue import Queue


def clear():
    os.system('clear')


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
        self._msg_history = {
            '((<friend>))': {
                '((<msg_id>))': {'status': 'other-fail-arrived-read', 'message': str}
            }
        }  # message history
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
            },
            'visualized_mess': {  # messaggio visualizzato
                'call': None,
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
            # creao dei thread cosi anche se l'esecuzione è lunga puo continuare a ascoltare i messaggi in entrata
            if recv_mess[const.TYPE_KEY] == const.COMMAND:
                pass
            elif recv_mess[const.TYPE_KEY] == const.OUTCOME:
                Thread(target=self._exe_outcome(recv_mess)).start()
            elif recv_mess[const.TYPE_KEY] == const.NOTIFYCATION:
                Thread(target=self._exe_notification(recv_mess)).start()
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
            # setta l'evento e aggiunge delle info, come ad esempio se il nome è già preso
            case const.SET_NAME:
                self._coll_events['name_check']['info'] = packet[const.ARGS_KEY][const.OUTCOME]
                self._coll_events['name_check']['event'].set()
            case const.DISCONNECT:
                self._coll_events['disconnect']['event'].set()
            case const.MESSAGE:  # messaggio visualizzato
                pass

    def _exe_notification(self, packet):
        match packet[const.SPECIFIC_KEY]:
            case const.MESSAGE:
                # chaimo l'evento messaggio
                self._coll_events['new_mess']['call'](
                    packet[const.ARGS_KEY][const.MESSAGE], packet[const.ARGS_KEY][const.SENDER])
                self._msg_history[packet[const.ARGS_KEY][const.SENDER]] = {packet[const.ARGS_KEY][const.ID]: {
                    'status': 'other', 'message': packet[const.ARGS_KEY][const.MESSAGE]}}
                # manda una rispsta: messaggio arrivato
                self._send(const.OUTCOME, const.MESSAGE, {
                           const.ID: packet[const.ARGS_KEY][const.ID], const.OUTCOME: const.SUCCESS})

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

    def set_event(self, new_message, visualized_message):
        self._coll_events['new_mess']['call'] = new_message
        self._coll_events['visualized_mess']['call'] = visualized_message

    def disconnect(self):
        self._send(const.COMMAND, const.DISCONNECT, {})

    def disconnect_to(self):
        pass

    def connect_to(self):
        pass

    def send_message(self, recipient, message):
        self._send(const.COMMAND, const.SEND_MSG, {
                   const.SENDER: self._name, const.RECIPIENT: recipient,
                   const.ID: hash(message), const.MESSAGE: message})

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
        self.cache = {
            'messages': []  # {sender:str, message:str}
        }
        self.set_name()
        self.input_()

    # GUI FUNCTION

    def set_name(self):
        while True:
            name = input('inserisci un nome: ')
            if self.cl.set_name(name) == True:
                break
        print('nome inserito')

    def input_(self):
        menumap = '1 accetta richieste-2 manda richiesta-3 manda messaggio-4 mostra messaggi-5 close'
        menumap_s = menumap.split('-')
        main_menu = Multi_level_menu(menu_map=menumap)
        while True:
            clear()
            ret = main_menu.start_menu()
            if ret == menumap_s[0]:
                pass
            elif ret == menumap_s[1]:
                pass
            elif ret == menumap_s[2]:
                self.send_message()
            elif ret == menumap_s[3]:
                self.show_messages()
            elif ret == menumap_s[4]:
                break

    def accept_friends(self):
        pass

    def send_message(self):
        clear()
        recipient = input('inserisci il destinatario: ')
        msg = input('inserisci il messaggio: ')
        self.cl.send_message(recipient, msg)

    def show_messages(self):
        clear()
        for msg in self.cache['messages']:
            print('sender: ' + msg['sender'] +
                  '\nmessage: ' + msg['message'] + '\n\n')
        self.cache['messages'].clear()
        input()

    # CLIENT EVENT FUNCTION

    def message(self, msg, sender_name):
        self.cache['messages'].append({'sender': sender_name, 'message': msg})


def start():
    gui_obj = gui()


if __name__ == '__main__':
    gui_obj = gui()
    pass
