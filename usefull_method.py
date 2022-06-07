from PyQt5 import QtCore

def set_window_flag(window):
    window.setWindowFlags(
        QtCore.Qt.WindowTitleHint |
        QtCore.Qt.WindowCloseButtonHint             
    )  
    window.setWindowModality(QtCore.Qt.ApplicationModal)

def delete_layout_item(layout):
        if layout is not None:
            while layout.count() != 1:
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.setParent(None)
                else:
                    delete_layout_item(item.layout())