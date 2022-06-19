import sys
from threading import Thread
from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtCore import QThread, pyqtSignal

from client_server import client
from main_window import ui_main
import usefull_method
from popup_window import (send_friend_request_win,
                          set_name_win, handle_friend_request_win)


class Signal(QThread):
    new_message = pyqtSignal(int, str)
    message_arrived = pyqtSignal(int, str)
    message_visualized = pyqtSignal(str)
    new_friend_request = pyqtSignal(str)
    friend_request_reply = pyqtSignal(bool, str)
    # segnali emessi da classi esterne
    set_name = pyqtSignal()
    friend_request_accepted = pyqtSignal(str)


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

        # indica con quale amico hai aperto la chat in questo momento
        self.focus_friend_chat = None

    def setup_connect_and_signal(self):
        self._signal = Signal()
        self._signal.new_message.connect(self.new_message_)
        self._signal.message_arrived.connect(self.message_arrived_)
        self._signal.new_message.connect(self.new_message_)
        self._signal.new_friend_request.connect(self.new_friend_request_)
        self._signal.friend_request_reply.connect(self.friend_request_reply_)

        self._signal.set_name.connect(self.set_lbl_name)
        self._signal.friend_request_accepted.connect(self.add_friend_widget)

        self._btn_send_msg.clicked.connect(self._btn_send_message_clicked)
        self._btn_add_friend.clicked.connect(self._btn_send_friend_req_clicked)
        self._btn_show_request.clicked.connect(
            self._btn_show_friend_req_clicked)

    def wait_set_name_win(self):
        self.set_name_win.set_name_event.wait()
        self._signal.set_name.emit()

    # ?#
    # ?#### CLIENT OVERIDDEN METHODS

    def new_message(self, msg_id, sender_name):
        self._signal.new_message.emit(msg_id, sender_name)

    def message_arrived(self, msg_id, sender_name):
        self._signal.message_arrived.emit(msg_id, sender_name)

    def message_visualized(self, sender_name):
        self._signal.message_visualized.emit(sender_name)

    def new_friend_request(self, sender_name):
        self._signal.new_friend_request.emit(sender_name)

    def friend_request_reply(self, reply, sender_name):
        self._signal.friend_request_reply.emit(reply, sender_name)
    # ?#
    # ?#### EMIT SIGNAL FUNCTIOM

    def new_message_(self, msg_id, sender_name):
        if sender_name == self.focus_friend_chat:
            self.show_chat_widget(self.focus_friend_chat)

    def message_arrived_(self, msg_id, sender_name):
        pass

    def message_visualized_(self, sender_name):
        pass

    def new_friend_request_(self, sender_name: str):
        pass

    def friend_request_reply_(self, reply, sender_name):
        if reply:
            self.add_friend_widget(sender_name)

    def _btn_send_message_clicked(self):
        if self.focus_friend_chat:  # se il focus attualmente è su un amico
            self.send_message(self.focus_friend_chat, self._txt_message.text())
            self.show_chat_widget(self.focus_friend_chat)

    def _btn_send_friend_req_clicked(self):
        self.send_friend_request_win = send_friend_request_win.Window.show(
            self.send_friend_request)

    def _btn_show_friend_req_clicked(self):
        self.handle_friend_req_win = handle_friend_request_win.Window.show(
            reply_to_request=self.reply_friend_request,
            get_requests_list=self.get_friend_req_arrived_list,
            friend_accepted_signal=self._signal.friend_request_accepted)
    #?#
    # ?#### OTHER

    def set_lbl_name(self):
        self._lbl_name.setText(self._name)

    def add_friend_widget(self, friend_name):
        _btn_open_chat = QtWidgets.QPushButton(self._frame_side_bar)
        _btn_open_chat.setMinimumSize(QtCore.QSize(0, 40))
        _btn_open_chat.setObjectName("_btn_open_chat")
        _btn_open_chat.setText(friend_name)
        _btn_open_chat.clicked.connect(
            lambda: self.show_chat_widget(_btn_open_chat.text()))
        self.verticalLayout.addWidget(self._btn_open_chat)

        self.verticalLayout.insertWidget(
            self.verticalLayout.count() - 2, _btn_open_chat)

    def show_chat_widget(self, friend_name):  # mostra la chat
        self.focus_friend_chat = friend_name
        msgs = self.get_messages(friend_name)
        usefull_method.delete_layout_item(self.vertical_chat_layout)
        spacerItem1 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.vertical_chat_layout.addItem(spacerItem1)
        if msgs != None:
            for id_ in msgs.keys():
                sizePolicy = QtWidgets.QSizePolicy(
                    QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                if msgs[id_]['status'] == 'other':  # messaggio ricevutoa
                    _lbl_friend_msg = QtWidgets.QLabel(self._frame_chat_text)
                    sizePolicy.setHeightForWidth(
                        _lbl_friend_msg.sizePolicy().hasHeightForWidth())
                    _lbl_friend_msg.setSizePolicy(sizePolicy)
                    _lbl_friend_msg.setStyleSheet("border:  3px solid rgb(255, 151, 151); border-width: 2px; border-radius: 10px; "
                                                  "border-top-left-radius:0px;")
                    _lbl_friend_msg.setObjectName(str(id_))
                    _lbl_friend_msg.setText(msgs[id_]['message'])
                    self.vertical_chat_layout.addWidget(_lbl_friend_msg)
                else:  # messaggio inviato
                    _lbl_my_msg = QtWidgets.QLabel(self._frame_chat_text)
                    sizePolicy.setHeightForWidth(
                        _lbl_my_msg.sizePolicy().hasHeightForWidth())
                    _lbl_my_msg.setSizePolicy(sizePolicy)
                    _lbl_my_msg.setStyleSheet("border:  3px solid rgb(0, 255, 8); "
                                              "border-width: 2px; border-radius: 10px; border-top-right-radius:0px;")
                    _lbl_my_msg.setObjectName(str(id_))
                    _lbl_my_msg.setText(msgs[id_]['message'])
                    self.vertical_chat_layout.addWidget(
                        _lbl_my_msg, 0, QtCore.Qt.AlignRight)
        elif msgs == None:
            pass  # todo: mettere un messaggio che ti dica che la chat è vuota


def start():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MainWindow_Method(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    start()
