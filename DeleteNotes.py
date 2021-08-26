from uipy.deleteNotes import Ui_DeleteWindow
from PyQt5.QtWidgets import QDialog


class DeleteNotesWindow(QDialog, Ui_DeleteWindow):
    def __init__(self, *args, **kwargs):
        super(DeleteNotesWindow, self).__init__(*args, **kwargs)

        self.setupUi(self)
        self.setModal(True)