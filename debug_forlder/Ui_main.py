# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dbg_main.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(652, 560)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self._frame_main = QtWidgets.QFrame(self.centralwidget)
        self._frame_main.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self._frame_main.setFrameShadow(QtWidgets.QFrame.Raised)
        self._frame_main.setObjectName("_frame_main")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self._frame_main)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self._frame_side_bar = QtWidgets.QFrame(self._frame_main)
        self._frame_side_bar.setMinimumSize(QtCore.QSize(160, 0))
        self._frame_side_bar.setMaximumSize(QtCore.QSize(160, 16777215))
        self._frame_side_bar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self._frame_side_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self._frame_side_bar.setObjectName("_frame_side_bar")
        self.verticalLayout = QtWidgets.QVBoxLayout(self._frame_side_bar)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self._frame_side_bar)
        self.frame.setMinimumSize(QtCore.QSize(0, 50))
        self.frame.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self._lbl_name = QtWidgets.QLabel(self.frame)
        self._lbl_name.setObjectName("_lbl_name")
        self.horizontalLayout_4.addWidget(self._lbl_name, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self._frame_side_bar)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self._btn_show_request = QtWidgets.QPushButton(self.frame_2)
        self._btn_show_request.setMinimumSize(QtCore.QSize(0, 40))
        self._btn_show_request.setObjectName("_btn_show_request")
        self.gridLayout.addWidget(self._btn_show_request, 0, 0, 1, 1)
        self._btn_add_friend = QtWidgets.QPushButton(self.frame_2)
        self._btn_add_friend.setMinimumSize(QtCore.QSize(0, 40))
        self._btn_add_friend.setObjectName("_btn_add_friend")
        self.gridLayout.addWidget(self._btn_add_friend, 0, 1, 1, 1)
        self.verticalLayout.addWidget(self.frame_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_2.addWidget(self._frame_side_bar)
        self._frame_chat = QtWidgets.QFrame(self._frame_main)
        self._frame_chat.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self._frame_chat.setFrameShadow(QtWidgets.QFrame.Raised)
        self._frame_chat.setObjectName("_frame_chat")
        self._layout_chat = QtWidgets.QVBoxLayout(self._frame_chat)
        self._layout_chat.setContentsMargins(0, 0, 0, 0)
        self._layout_chat.setObjectName("_layout_chat")
        self._frame_chat_text = QtWidgets.QFrame(self._frame_chat)
        self._frame_chat_text.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self._frame_chat_text.setFrameShadow(QtWidgets.QFrame.Raised)
        self._frame_chat_text.setObjectName("_frame_chat_text")
        self._layout_chat.addWidget(self._frame_chat_text)
        self._frame_write_msg = QtWidgets.QFrame(self._frame_chat)
        self._frame_write_msg.setMinimumSize(QtCore.QSize(0, 40))
        self._frame_write_msg.setMaximumSize(QtCore.QSize(16777215, 40))
        self._frame_write_msg.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self._frame_write_msg.setFrameShadow(QtWidgets.QFrame.Raised)
        self._frame_write_msg.setObjectName("_frame_write_msg")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self._frame_write_msg)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self._txt_write_msg = QtWidgets.QTextEdit(self._frame_write_msg)
        self._txt_write_msg.setMinimumSize(QtCore.QSize(245, 0))
        self._txt_write_msg.setMaximumSize(QtCore.QSize(245, 16777215))
        self._txt_write_msg.setObjectName("_txt_write_msg")
        self.horizontalLayout_5.addWidget(self._txt_write_msg)
        self._btn_send_msg = QtWidgets.QPushButton(self._frame_write_msg)
        self._btn_send_msg.setMaximumSize(QtCore.QSize(80, 16777215))
        self._btn_send_msg.setObjectName("_btn_send_msg")
        self.horizontalLayout_5.addWidget(self._btn_send_msg)
        self.horizontalLayout_5.setStretch(0, 2)
        self.horizontalLayout_5.setStretch(1, 1)
        self._layout_chat.addWidget(self._frame_write_msg)
        self.horizontalLayout_2.addWidget(self._frame_chat)
        self.horizontalLayout.addWidget(self._frame_main)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self._lbl_name.setText(_translate("MainWindow", "TextLabel"))
        self._btn_show_request.setText(_translate("MainWindow", "Request"))
        self._btn_add_friend.setText(_translate("MainWindow", "Add"))
        self._btn_send_msg.setText(_translate("MainWindow", "Send"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
