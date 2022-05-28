
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
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


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
