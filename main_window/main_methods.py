import sys
from threading import Thread
from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtCore import QThread, pyqtSignal

from client_server import client
from main_window import ui_main
from popup_window import (send_friend_request_win,
                          set_name_win, handle_friend_request_win)


class Signal(QThread):
    new_message = pyqtSignal(int, str)
    message_arrived = pyqtSignal(int, str)
    message_visualized = pyqtSignal(str)
    set_name = pyqtSignal()


class MainWindow_Method(ui_main.Ui_MainWindow, client.Client):
    def __init__(self, MainWindow) -> None:
        client.Client.__init__(self)
        self.start()
        self.setupUi(MainWindow)
        self._main_window = MainWindow

        self.setup_connect_and_signal()

        # mostra la finestra pop up per settare il nome
        self.set_name_win = set_name_win.Window.show(self.set_name)
        # faccio partire il thread per impostare il messaggio cosi non si blocca l'interfaccia grafica
        self.set_name_thread = Thread(target=self.wait_set_name_win).start()

    def setup_connect_and_signal(self):
        self._signal = Signal()
        self._signal.new_message.connect(self.new_message_)
        self._signal.message_arrived.connect(self.message_arrived_)
        self._signal.new_message.connect(self.new_message_)
        self._signal.set_name.connect(self.set_lbl_name)

    def wait_set_name_win(self):
        self.set_name_win.set_name_event.wait()
        self._signal.set_name.emit()
    # ?#
    # ?#### CLIENT OVERIDDEN METHODS

    def new_message(self, msg_id, sender_name):
        self._signal.new_message_signal.emit(msg_id, sender_name)

    def message_arrived(self, msg_id, sender_name):
        self._signal.message_arrived.emit(msg_id, sender_name)

    def message_visualized(self, sender_name):
        self._signal.message_visualized.emit(sender_name)
    # ?#
    # ?#### EMIT SIGNAL FUNCTIOM

    def new_message_(self, msg_id, sender_name):
        self._lbl_name.setText(str(msg_id))

    def message_arrived_(self, msg_id, sender_name):
        pass

    def message_visualized_(self, sender_name):
        pass
    #?#
    # ?#### OTHER

    def set_lbl_name(self):
        self._lbl_name.setText(self._name)


def start():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MainWindow_Method(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    start()
