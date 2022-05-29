import json
import os
import socket
from queue import Queue
from threading import Event, Thread
from client_server import constant as const
from debug_forlder import Multi_level_menu
from debug_forlder import support_library_v1 as sl


def clear():
    os.system('clear')


class Client:
    def __init__(self) -> None:
        self._name = ''
        self._msg_history = {
            '((<friend>))': {
                '((<msg_id>))': {
                    'status': 'other-fail-sended-arrived-read',
                    'message': 'str',
                }
            }
        }  # message history
        self._coll_events = {  # collections of event
            'name_set': {'event': Event()},
            'name_check': {'event': Event(), 'info': ''},
            'disconnect': {'event': Event()},
        }

    def _start(self):
        history = []
        try:
            # fa partire un thread che controlla se il nome è gia stato scelto
            Thread(target=self._wait_name_check).start()
            while True:
                if self._coll_events['disconnect']['event'].is_set():
                    break
                recv_mess = self._recive()
                history.append(recv_mess)
                # creao dei thread cosi anche se l'esecuzione è lunga puo continuare a ascoltare i messaggi in entrata
                if recv_mess[const.TYPE_KEY] == const.COMMAND:
                    pass
                elif recv_mess[const.TYPE_KEY] == const.OUTCOME:
                    Thread(target=self._exe_outcome(recv_mess)).start()
                elif recv_mess[const.TYPE_KEY] == const.NOTIFYCATION:
                    Thread(target=self._exe_notification(recv_mess)).start()
            self._server.close()
            self = None
        except Exception as e:
            print()
            const.print_dict(history)
            print(self._name)
            const.print_dict(self._msg_history)
            raise e

    def _wait_name_check(self):  # aspette che il nome si stato verificato dal server
        while True:
            self._coll_events['name_set']['event'].wait()
            self._coll_events['name_set']['event'].clear()
            self._send(const.COMMAND, const.SET_NAME, {const.NAME: self._name})
            self._coll_events['name_check']['event'].wait()
            if self._coll_events['name_check']['info'] == const.SUCCESS:
                break

    def _send(self, type_, specific, arguments: dict) -> None:
        message = {
            const.TYPE_KEY: type_,
            const.SPECIFIC_KEY: specific,
            const.ARGS_KEY: arguments,
        }  # creo il pacchetto
        message = json.dumps(message)  # lo trasform in un json
        message = message.encode(const.FORMAT)
        msg_lenght = len(message)
        send_lenght = str(msg_lenght).encode(const.FORMAT)
        send_lenght += b' ' * (const.HEADER - len(send_lenght))
        self._server.send(send_lenght)
        self._server.send(message)

    def _recive(self) -> dict:
        msg_lenght = self._server.recv(const.HEADER).decode(
            const.FORMAT
        )  # riceve prima la lunghezza del messaggio
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
                self._coll_events['name_check']['info'] = packet[const.ARGS_KEY][
                    const.OUTCOME
                ]
                self._coll_events['name_check']['event'].set()
            case const.DISCONNECT:
                self._coll_events['disconnect']['event'].set()

    def _exe_notification(self, packet):
        match packet[const.SPECIFIC_KEY]:
            case const.MESSAGE:
                self._msg_history[packet[const.ARGS_KEY][const.SENDER]] = {
                    packet[const.ARGS_KEY][const.ID]: {
                        'status': 'other',
                        'message': packet[const.ARGS_KEY][const.MESSAGE],
                    }
                }
                # manda una rispsta: messaggio arrivato
                self._send(const.NOTIFYCATION, const.ARRIVEDE_MSG, {
                           const.RECIPIENT: packet[const.ARGS_KEY][const.SENDER],
                           const.ID: packet[const.ARGS_KEY][const.ID], const.OUTCOME: const.SUCCESS,
                           const.SENDER: self._name, })
                # chaimo l'evento messaggio
                self.new_message(packet[const.ARGS_KEY][const.ID],
                                 packet[const.ARGS_KEY][const.SENDER])
            case const.ARRIVEDE_MSG:
                self._msg_history[packet[const.ARGS_KEY][const.SENDER]][packet[const.ARGS_KEY]
                                                                        [const.ID]]['status'] = 'arrived'  # imposto lo stato del messaggio come arrivato
                self.message_arrived(
                    packet[const.ARGS_KEY][const.ID], const.NAME)
            case const.VISUALIZED_MSG:
                # cambi lo stato del messaggio in letto
                for id_ in self._msg_history[packet[const.ARGS_KEY][const.SENDER]].keys():
                    if self._msg_history[packet[const.ARGS_KEY][const.SENDER]][id_]['status'] == 'other':
                        continue
                    self._msg_history[packet[const.ARGS_KEY]
                                      [const.SENDER]][id_]['status'] = 'read'
                # chiamo l'evento messaggio visualizzato
                self.message_visualized(packet[const.ARGS_KEY][const.SENDER])

    # ?#### PUBLIC FUNCTION

    def start(self) -> bool:
        self._server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self._server.connect(const.ADDR)
            print('connesso')
            self._start_client = Thread(target=self._start).start()
            return True
        except socket.error:
            print('[ERRORE]: impossibile connettersi al server')
            return False

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

    def disconnect(self):
        self._send(const.COMMAND, const.DISCONNECT, {})

    def get_message(self, id_, friend_name) -> str:
        if friend_name in self._msg_history.keys():
            if id_ in self._msg_history[friend_name]:
                return self._msg_history[friend_name][id_]['message']
            else:
                pass  # todo: eccezione
        else:
            pass  # todo: sollevare eccezione

    def send_message(self, recipient, message):
        msg_hash = hash(message)
        self._msg_history[recipient] = {
            msg_hash: {  # TODO: controllo che il recipient esista
                'status': 'sended',
                'message': message,
            }
        }
        self._send(const.NOTIFYCATION, const.MESSAGE, {
                   const.SENDER: self._name, const.RECIPIENT: recipient, const.ID: msg_hash, const.MESSAGE: message, },)

    def visualized_message(self, friend_name):  # to call when user read message
        self._send(const.NOTIFYCATION, const.VISUALIZED_MSG, {
                   const.SENDER: self._name, const.RECIPIENT: friend_name})

    def send_friend_request(self, name):
        self._send(const.COMMAND, const.SEND_FRIEND_REQ, {})

    def debug_func(self, command):
        command = command.split('-')
        if command[0] == 'setn':  # set name-name
            if self.set_name(command[1]) == True:
                print(
                    f'[OUTPUT-SUCCESS]: impostazione nome <{command[1]}> eseguita con successo!'
                )
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

    # ? OVVERIDABLE FUNCTION

    def new_message(self, msg_id, sender_name):
        pass

    def message_visualized(self, sender_name):
        pass

    def message_arrived(self, msg_id, sender_name):
        pass


class gui(Client):
    def __init__(self) -> None:
        self.ar = 'nooo'
        super().__init__()
        self.start()
        self.cache = {'messages': []}  # {sender:str, message:str}

        self.menumap = '1 accetta richieste-2 manda richiesta-3 manda messaggio-4 mostra messaggi-5 close'
        self.menumap_s = self.menumap.split('-')
        self.main_menu = Multi_level_menu(menu_map=self.menumap)

        self.set_name_gui()
        self.input_()

    # GUI FUNCTION

    def set_name_gui(self):
        while True:
            name = input('inserisci un nome: ')
            if self.set_name(name) == True:
                break
        print('nome inserito')

    def input_(self):
        while True:
            clear()
            print(self._name)
            ret = self.main_menu.start_menu()
            if ret == self.menumap_s[0]:
                pass
            elif ret == self.menumap_s[1]:
                pass
            elif ret == self.menumap_s[2]:
                self.send_message_gui()
            elif ret == self.menumap_s[3]:
                self.show_messages()
            elif ret == self.menumap_s[4]:
                break

    def accept_friend_request(self):
        pass

    def send_friend_request(self):
        pass

    def send_message_gui(self):
        clear()
        recipient = input('inserisci il destinatario: ')
        msg = input('inserisci il messaggio: ')
        self.send_message(recipient, msg)

    def show_messages(self):  # ! DA CAMBIARE
        clear()
        b = True
        for key in self._msg_history.keys():
            if b:
                b = False
                continue
            self.visualized_message(key)
        const.print_dict(self._msg_history)
        print(self.ar)

        # for friend in self.cl._msg_history.keys():
        #     print('Friend: ' + friend)
        #     for id_ in self.cl._msg_history[friend].keys():
        #         print('Id: ' + str(id_) + '\nStatus: ' +
        #               self.cl._msg_history[friend][id_]['status'] + '\nMessage: ' + self.cl._msg_history[friend][id_]['message'])
        input()

    # CLIENT EVENT FUNCTION

    def new_message(self, msg_id, sender_name):
        pass

    def message_arrived(self, msg_id, sender_name):
        pass

    def message_visualized(self, sender_name):
        pass


def start():
    gui_obj = gui()


if __name__ == '__main__':
    gui_obj = gui()
    pass
