from PyQt5 import QtCore, QtGui, QtWidgets

import usefull_method

class Window(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(420, 200)
        MainWindow.setMinimumSize(QtCore.QSize(420, 200))
        MainWindow.setMaximumSize(QtCore.QSize(420, 200))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self._txn_friend_name = QtWidgets.QLineEdit(self.frame)
        self._txn_friend_name.setObjectName("_txn_friend_name")
        self.verticalLayout.addWidget(self._txn_friend_name)
        self._btn_send = QtWidgets.QPushButton(self.frame)
        self._btn_send.setObjectName("_btn_send")
        self.verticalLayout.addWidget(self._btn_send)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self._btn_send.setText(_translate("MainWindow", "Send"))

    #! ######## MY METHODS ########

    def show(set_name_func) -> object:
        window = QtWidgets.QMainWindow()
        window = Window(window, set_name_func)
        usefull_method.set_window_flag(window)
        window.show()
        return window

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Window()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
