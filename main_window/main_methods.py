import sys
from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtCore import QThread, pyqtSignal

from client_server import client
from main_window import ui_main
from popup_window import set_name_win, handle_friend_request_win

def set_window_flag(window):
    window.setWindowFlags(
        QtCore.Qt.WindowTitleHint |
        QtCore.Qt.WindowCloseButtonHint             
    )  
    window.setWindowModality(QtCore.Qt.ApplicationModal)


class Signal(QThread):
    new_message = pyqtSignal(int, str)
    message_arrived = pyqtSignal(int, str)
    message_visualized = pyqtSignal(str)
    name_setted = pyqtSignal(str)


class MainWindow_Method(ui_main.Ui_MainWindow, client.Client):
    def __init__(self, MainWindow) -> None:
        client.Client.__init__(self)
        self.start()
        self.setupUi(MainWindow)
        self._main_window = MainWindow

        self.setup_connect_and_signal()
        self.set_name_win = set_name_win.Window.show(self._signal.name_setted)

    def setup_connect_and_signal(self):
        self._signal = Signal()
        self._signal.new_message.connect(self.new_message_)
        self._signal.message_arrived.connect(self.message_arrived_)
        self._signal.new_message.connect(self.new_message_)
        self._signal.name_setted.connect(self.set_name)

    # ?#
    # ?#### CLIENT OVERIDDEN METHODS
    def new_message(self, msg_id, sender_name):
        self._signal.new_message_signal.emit(msg_id, sender_name)

    def message_arrived(self, msg_id, sender_name):
        self._signal.message_arrived.emit(msg_id, sender_name)

    def message_visualized(self, sender_name):
        self._signal.message_visualized.emit(sender_name)
    
    # ?
    # ?#### EMIT SIGNAL FUNCTIOM
    def new_message_(self, msg_id, sender_name):
        self._lbl_name.setText(str(msg_id))

    def message_arrived_(self, msg_id, sender_name):
        pass

    def message_visualized_(self, sender_name):
        pass

    def name_setted(self, name):
        if self.set_name(name):
            pass
        else:
            pass


def start():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MainWindow_Method(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    start()
