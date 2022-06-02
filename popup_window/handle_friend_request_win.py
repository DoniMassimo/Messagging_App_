from PyQt5 import QtCore, QtGui, QtWidgets

import usefull_method

class Window(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(420, 600)
        MainWindow.setMinimumSize(QtCore.QSize(420, 600))
        MainWindow.setMaximumSize(QtCore.QSize(420, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_widget = QtWidgets.QFrame(self.frame)
        self.frame_widget.setMinimumSize(QtCore.QSize(0, 40))
        self.frame_widget.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_widget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_widget.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_widget.setObjectName("frame_widget")
        self.horiz_friend_layout = QtWidgets.QHBoxLayout(self.frame_widget)
        self.horiz_friend_layout.setContentsMargins(0, 0, 0, 0)
        self.horiz_friend_layout.setObjectName("horiz_friend_layout")
        self._lbl_seder_name = QtWidgets.QLabel(self.frame_widget)
        self._lbl_seder_name.setObjectName("_lbl_seder_name")
        self.horiz_friend_layout.addWidget(self._lbl_seder_name)
        self._btn_yes = QtWidgets.QPushButton(self.frame_widget)
        self._btn_yes.setMinimumSize(QtCore.QSize(40, 40))
        self._btn_yes.setMaximumSize(QtCore.QSize(40, 40))
        self._btn_yes.setObjectName("_btn_yes")
        self.horiz_friend_layout.addWidget(self._btn_yes)
        self._btn_no = QtWidgets.QPushButton(self.frame_widget)
        self._btn_no.setMinimumSize(QtCore.QSize(40, 40))
        self._btn_no.setMaximumSize(QtCore.QSize(40, 40))
        self._btn_no.setObjectName("_btn_no")
        self.horiz_friend_layout.addWidget(self._btn_no)
        self.verticalLayout.addWidget(self.frame_widget)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self._lbl_seder_name.setText(_translate("MainWindow", "TextLabel"))
        self._btn_yes.setText(_translate("MainWindow", "YES"))
        self._btn_no.setText(_translate("MainWindow", "NO"))

    #! ######## MY METHODS ########

    def __init__(self, selfwindow, requests_list):
        self.selfwindow = selfwindow
        self.requests_list = requests_list
            
    def show(requests_list) -> object:
        q_window = QtWidgets.QMainWindow()
        window = Window(q_window, requests_list)
        usefull_method.set_window_flag(q_window)
        q_window.show()
        return window

    def set_window_style(self):
        for name in self.requests_list:
            frame_widget = QtWidgets.QFrame(self.frame)
            frame_widget.setMinimumSize(QtCore.QSize(0, 40))
            frame_widget.setMaximumSize(QtCore.QSize(16777215, 40))
            frame_widget.setFrameShape(QtWidgets.QFrame.StyledPanel)
            frame_widget.setFrameShadow(QtWidgets.QFrame.Raised)
            frame_widget.setObjectName("frame_widget")

            horizontal_widget = QtWidgets.QHBoxLayout(frame_widget)
            horizontal_widget.setContentsMargins(0, 0, 0, 0)
            horizontal_widget.setObjectName("horizontal_widget")

            lbl_name = QtWidgets.QLabel(frame_widget)
            lbl_name.setObjectName("_lbl_seder_name")

            _btn_yes = QtWidgets.QPushButton(frame_widget)
            _btn_yes.setMinimumSize(QtCore.QSize(40, 40))
            _btn_yes.setMaximumSize(QtCore.QSize(40, 40))
            _btn_yes.setObjectName("_btn_yes")
            horizontal_widget.addWidget(_btn_yes)

            _btn_no = QtWidgets.QPushButton(frame_widget)
            _btn_no.setMinimumSize(QtCore.QSize(40, 40))
            _btn_no.setMaximumSize(QtCore.QSize(40, 40))
            _btn_no.setObjectName("_btn_no")
            horizontal_widget.addWidget(_btn_no)

            self.verticalLayout.insertWidget(self.verticalLayout.count() - 1, frame_widget)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Window()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
