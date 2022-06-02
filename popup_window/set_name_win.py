import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal
import usefull_method
from threading import Event

class Signal(QThread):
    name_setted_return = pyqtSignal(bool)


class Window(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(420, 200)
        MainWindow.setMinimumSize(QtCore.QSize(420, 200))
        MainWindow.setMaximumSize(QtCore.QSize(420, 200))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self._btn_ok = QtWidgets.QPushButton(self.frame)
        self._btn_ok.setObjectName("_btn_ok")
        self.gridLayout.addWidget(self._btn_ok, 1, 0, 1, 2)
        self._txt_set_name = QtWidgets.QLineEdit(self.frame)
        self._txt_set_name.setObjectName("_txt_set_name")
        self.gridLayout.addWidget(self._txt_set_name, 0, 0, 1, 1)
        self.horizontalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self._btn_ok.setText(_translate("MainWindow", "OK"))

    #! ######## MY METHODS ########

    def __init__(self, selfwindow, set_name_func) -> None:
        self._selfwindow = selfwindow
        self.set_name_func = set_name_func
        self.set_name_event = Event()
        self.setupUi(selfwindow)
        self.setup_connect_and_signal()
        self.name_event = Event() # viene settato quando il nome è giusto

    def setup_connect_and_signal(self):
        self._signal = Signal()
        self._btn_ok.clicked.connect(self._btn_ok_clicked)

    def show(set_name_func) -> object:
        window = QtWidgets.QMainWindow()
        window = Window(window, set_name_func)
        usefull_method.set_window_flag(window)
        window.show()
        return window

    def _btn_ok_clicked(self):
        self._selfwindow.setEnabled(False)
        if self.set_name_func(self._txt_set_name.text()) == True:
            self.set_name_event.set()
            self._selfwindow.close()
        else:
            pass

def start():    
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Window(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    start()
