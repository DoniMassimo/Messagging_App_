import sys
from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtCore import QThread, pyqtSignal

from client_server import client
from main import ui_main


class Signal(QThread):
    new_message_signal = pyqtSignal()
    message_arrived_signal = pyqtSignal()
    message_visualized_signal = pyqtSignal()
    

class MainWindow_Method(ui_main.Ui_MainWindow, client.Client):
    def __init__(self, MainWindow) -> None:
        client.Client.__init__(self)
        self.start()
        self.setupUi(MainWindow)
        self._main_window = MainWindow

        self._signal_args = {'new_mess': {'id': None, 'sender_name': None}}
        self.setup_connect_and_signal()

        self.set_name(input('inserisci un nome: '))
        rec = input('inserisci il destinatario: ')
        msg = input('inserisci il messaggio: ')
        self.send_message(rec, msg)

    def setup_connect_and_signal(self):
        self._signal = Signal()
        self._signal.new_message_signal.connect(lambda: self.new_message_(
            self._signal_args['new_mess']['id'], self._signal_args['new_mess']['sender_name']))

    # ?#
    # ?#### CLIENT OVERIDDEN METHODS
    def new_message(self, msg_id, sender_name):
        self._signal_args['new_mess']['id'] = msg_id
        self._signal_args['new_mess']['sender_name'] = sender_name
        self._signal.new_message_signal.emit()

    def message_arrived(self, msg_id, sender_name):
        pass

    def message_visualized(self, sender_name):
        pass

    def new_message_(self, msg_id, sender_name):
        self._lbl_name.setText(str(msg_id))
        


def start():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MainWindow_Method(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    start()
