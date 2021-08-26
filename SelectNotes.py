from uipy.selectNotesUI import Ui_SelectWindow
from PyQt5.QtWidgets import  QDialog


class SelectNotesWindow(QDialog, Ui_SelectWindow):
    def __init__(self, *args, **kwargs):
        super(SelectNotesWindow, self).__init__(*args, **kwargs)

        self.setupUi(self)
        self.setModal(True)