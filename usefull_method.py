from PyQt5 import QtCore

def set_window_flag(window):
    window.setWindowFlags(
        QtCore.Qt.WindowTitleHint |
        QtCore.Qt.WindowCloseButtonHint             
    )  
    window.setWindowModality(QtCore.Qt.ApplicationModal)