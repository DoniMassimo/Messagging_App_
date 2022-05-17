import socket
import constant as const
import json
from threading import Thread


class Client:
    def __init__(self, conn, addr) -> None:
        self._conn = conn
        self._addr = addr
        self._start_client = Thread(target=self._start).start()   
        self._name = ''     

    def _recive(self) -> dict:
        msg_lenght = self._conn.recv(const.HEADER).decode(const.FORMAT) # riceve prima la lunghezza del messaggio 
        if msg_lenght:
            msg_lenght = int(msg_lenght)
            message = self._conn.recv(msg_lenght).decode(const.FORMAT) # riceve il messaggio in base alla sua lunghezza
            message = json.loads(message) # lo ritrasformo in un dictionary
            return message

    def _send(self, type_, specific, arguments:dict) -> None:
        message = {const.TYPE_KEY:type_, const.SPECIFIC_KEY:specific, const.ARGS_KEY:arguments} # creo il pacchetto
        message = json.dumps(message) # lo trasform in un json
        message = message.encode(const.FORMAT)
        msg_lenght = len(message)
        send_lenght = str(msg_lenght).encode(const.FORMAT)
        send_lenght += b' ' * (const.HEADER - len(send_lenght))
        self._conn.send(send_lenght)
        self._conn.send(message)  

    def _start(self) -> None:
        while True:
            recv_mess = self._recive()
            print(recv_mess)
            # if recv_mess == None: 
            #     continue
            if (recv_mess[const.TYPE_KEY] == const.COMMAND) and (recv_mess[const.SPECIFIC_KEY] == const.DISCONNECT):
                Server._remove_client(self)
                self._send(const.OUTCOME, const.DISCONNECT, {})
                self._conn.close()
                self = None
                break
            elif recv_mess[const.TYPE_KEY] == const.COMMAND: # è un comando
                self._exe_command(recv_mess)
            elif recv_mess[const.TYPE_KEY] == const.OUTCOME: # todo: nel caso sia un risultato
                pass


    def _exe_command(self, packet:dict):
        match packet[const.SPECIFIC_KEY]:
            case const.DISCONNECT_TO:
                pass
            case _:
                Server.exe_command(self, packet)

    def disconnect():        
        pass

    def disconnect_to():
        pass
    
    def connect_to():
        pass

    def send_message():
        pass


class Server: 
    def init() -> None:
        Server._server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        Server._server.bind(const.ADDR)
        Server._clients_list = []        
        Server._start()

    def _start() -> None:
        Server._server.listen()
        print('[ADDRESS]: ' + str(const.ADDR))    
        while True:
            conn, addr = Server._server.accept()
            print('[NEW CONNECTION]:', addr)            
            Server._clients_list.append(Client(conn=conn, addr=addr))            

    def _remove_client(sender):
        Server._clients_list.remove(sender)
        if Server._clients_list:
            for client in Server._clients_list:
                print(client._name)
        else:
            print('NON CE NESSUNO!!!')

    def exe_command(sender, packet):
        match packet[const.SPECIFIC_KEY]:
            case const.SET_NAME:
                Server._set_name(sender, packet[const.ARGS_KEY][const.NAME])
            case const.SEND_MSG:
                Server._send_message(sender, packet)

    def _set_name(sender, name): # imposta il nome di un client se non è già utilizzato
        if name not in [client._name for client in Server._clients_list]: # nome non esiste ancora
            sender._name = name
            print('nome cambiato in ', name)
            sender._send(const.OUTCOME, const.SET_NAME, {const.OUTCOME:const.SUCCESS})
        else:
            sender._send(const.OUTCOME, const.SET_NAME, {const.OUTCOME:const.FAILED})

    def _send_message(sender, packet):
        for client in Server._clients_list:
            if client._name == packet[const.ARGS_KEY][const.RECIPIENT]:
                client._send(const.NOTIFYCATION, const.MESSAGE, packet[const.ARGS_KEY])
                break

if __name__ == '__main__':
    Server.init()

    pass 