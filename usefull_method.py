from PyQt5 import QtCore
import jsbeautifier
import json

def set_window_flag(window):
    window.setWindowFlags(
        QtCore.Qt.WindowTitleHint |
        QtCore.Qt.WindowCloseButtonHint
    )
    window.setWindowModality(QtCore.Qt.ApplicationModal)


def delete_layout_item(layout):
    if layout is not None:
        while layout.count() != 0:
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.setParent(None)
            else:
                delete_layout_item(item.layout())


def print_dict(dict_, info=''):
    print('\n')
    opts = jsbeautifier.default_options()
    opts.indent_size = 2
    print(info + '\n' + jsbeautifier.beautify(json.dumps(dict_), opts=opts))



_msg_history = {
    '((<friend>))': {
        '((<msg_id>))': {
            'status': 'other-fail-sended-arrived-read',
            'message': 'str',
        }
    }
}  # message history

