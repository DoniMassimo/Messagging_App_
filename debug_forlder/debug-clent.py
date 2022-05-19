import constant as const
#import constant as const

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

    def _input(self):
        while True:
            m = input('inserisci: ')
            self._send(const.COMMAND, const.MESSAGE, {'mess':m})

    def _start(self):
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
        print(packet)
