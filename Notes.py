from PyQt5.QtWidgets import QDialog
from uipy.edit_notes import Ui_edit_notes


class NotesWindow(QDialog, Ui_edit_notes):
    def __init__(self, *args, **kwargs):
        super(NotesWindow, self).__init__(*args, **kwargs)

        self.setupUi(self)
        self.setModal(True)

        self.btn_discard.clicked.connect(self.notes_window_discard_clicked)
        self.btn_save.clicked.connect(self.notes_window_save_clicked)

        
    def notes_window_discard_clicked(self):
        self.hide()

    def notes_window_save_clicked(self):

        name = self.ldt_note_title.text()
        # body = self.txtedt_note_body.text()

        importance_container = self.hbox_importance

        for i in range(0, 3):
            priority = importance_container.itemAt(i).widget()
            if (priority.isChecked()):
                print(priority.text())
        self.hide()
