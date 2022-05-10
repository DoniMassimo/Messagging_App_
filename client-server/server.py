import socket
import constant as const
import json
import threading


class Client:
    def __init__(self, conn, addr) -> None:
        self._conn = conn
        self._addr = addr
        self.__start_client = threading.Thread(target=self._start).start()

    def _recive(self) -> dict:
        msg_lenght = self._conn.recv(const.HEADER).decode(const.FORMAT) # riceve prima la lunghezza del messaggio 
        if msg_lenght:
            msg_lenght = int(msg_lenght)
            message = self._conn.recv(msg_lenght).decode(const.FORMAT) # riceve il messaggio in base alla sua lunghezza
            message = json.loads(message) # lo ritrasformo in un dictionary
            return message

    def send(self, message:dict):
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
            # if recv_mess == None: 
            #     continue
            if (recv_mess[const.TYPE_KEY] == const.COMMAND_TYPE) and (recv_mess[const.SPECIFIC_KEY] == const.DISCONNECT):
                break
            elif recv_mess[const.TYPE_KEY] == const.COMMAND_TYPE: # è un comando
                self._exe_command(recv_mess)
            elif recv_mess[const.TYPE_KEY] == const.OUTCOME_TYPE: # todo: nel caso sia un risultato
                pass

            print(recv_mess)
        self._del_client()  

    def _exe_command(self, command:dict):
        match command[const.SPECIFIC_KEY]:
            case const.DISCONNECT_TO:
                pass

            case const.SEND_SRV:
                print('[MESSAGGIO SERVER]: ', command[const.ARGS_KEY][0])
            case _:
                Server.exe_command(command, self)

    def disconnect():
        print('MANNAGGIA')
        pass

    def disconnect_to():
        pass
    
    def connect_to():
        pass

    def send_message():
        pass

    def server_message(msg):
        print('[SERVER MESSAGE] ', msg)
        pass   


class Server: # base server, riutilizzabile
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
            print('[NEW CONNECTION]:', conn, addr)            
            Server._clients_list.append(Client(conn=conn, addr=addr))            

    def exe_command(command, sender):
        pass


if __name__ == '__main__':
    Server.init()
    pass