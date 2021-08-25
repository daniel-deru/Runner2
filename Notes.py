from class_snippets.MessageBox import Message
from PyQt5.QtWidgets import QDialog
from uipy.edit_notes import Ui_edit_notes
from db import DB
from datetime import date



class NotesWindow(QDialog, Ui_edit_notes):
    def __init__(self, *args, **kwargs):
        super(NotesWindow, self).__init__(*args, **kwargs)

        self.setupUi(self)
        self.setModal(True)

        self.hbox_importance.itemAt(0).widget().setChecked(True)

        self.btn_discard.clicked.connect(self.notes_window_discard_clicked)
        self.btn_save.clicked.connect(self.notes_window_save_clicked)

    def notes_window_discard_clicked(self):
        self.hide()

    def notes_window_save_clicked(self):

        name = self.ldt_note_title.text()
        body = self.txtedt_note_body.toPlainText()
        priority = self.hbox_importance.itemAt(0).widget().text()
        current_date = date.today().strftime("%B %d, %Y")

        importance_container = self.hbox_importance

        for i in range(0, 3):
            priority_box = importance_container.itemAt(i).widget()
            if priority_box.isChecked():
                priority = priority_box.text()

        if not name and body:
            Message("There are missing fields. Please make sure your note has a title and a body.", "Missing Fields")
        elif name and body:
            # Check the database if the not exists or not
            note = (
                name,
                body,
                priority,
                current_date
            )
            db = DB()
            db.save("notes", note)
            self.hide()
