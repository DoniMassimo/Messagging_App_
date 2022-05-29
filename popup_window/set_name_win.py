import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal
import usefull_method

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
        self._txt_set_name = QtWidgets.QPlainTextEdit(self.frame)
        self._txt_set_name.setMinimumSize(QtCore.QSize(0, 40))
        self._txt_set_name.setMaximumSize(QtCore.QSize(16777215, 40))
        self._txt_set_name.setObjectName("_txt_set_name")
        self.gridLayout.addWidget(self._txt_set_name, 0, 0, 1, 2, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self._btn_ok = QtWidgets.QPushButton(self.frame)
        self._btn_ok.setObjectName("_btn_ok")
        self.gridLayout.addWidget(self._btn_ok, 1, 0, 1, 2)
        self.horizontalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self._btn_ok.setText(_translate("MainWindow", "OK"))

    #! ######## MY METHODS ########

    def __init__(self, mainwindow, name_set_signal) -> None:
        self._mainwindow = mainwindow
        self.setupUi(mainwindow)
        self._my_setup(name_set_signal)

    def _my_setup(self, name_set_signal):
        self._name_set_signal = name_set_signal
        self._signal = Signal()
        self._signal.name_setted_return.connect(self._name_setted_return)
        self._btn_ok.clicked.connect(self._btn_ok_clicked)

    def show() -> object:
        window = QtWidgets.QMainWindow()
        snw = Window(window)
        usefull_method.set_window_flag(window)
        window.show()
        return snw

    def _name_setted_return(self, ret: bool):
        pass

    def _btn_ok_clicked(self):
        self._name_set_signal.emit(self._txt_set_name.text())

def start():    
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Window(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    start()
