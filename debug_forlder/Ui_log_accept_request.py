# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dbg_send_friend_req.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
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
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 40))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self._lbl_seder_name = QtWidgets.QLabel(self.frame_2)
        self._lbl_seder_name.setObjectName("_lbl_seder_name")
        self.horizontalLayout_2.addWidget(self._lbl_seder_name)
        self._btn_yes = QtWidgets.QPushButton(self.frame_2)
        self._btn_yes.setMinimumSize(QtCore.QSize(40, 40))
        self._btn_yes.setMaximumSize(QtCore.QSize(40, 40))
        self._btn_yes.setObjectName("_btn_yes")
        self.horizontalLayout_2.addWidget(self._btn_yes)
        self._btn_no = QtWidgets.QPushButton(self.frame_2)
        self._btn_no.setMinimumSize(QtCore.QSize(40, 40))
        self._btn_no.setMaximumSize(QtCore.QSize(40, 40))
        self._btn_no.setObjectName("_btn_no")
        self.horizontalLayout_2.addWidget(self._btn_no)
        self.verticalLayout.addWidget(self.frame_2)
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


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
