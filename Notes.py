from PyQt5.QtCore import pyqtSignal
from class_snippets.MessageBox import Message
from PyQt5.QtWidgets import QDialog
from uipy.edit_notes import Ui_edit_notes
from db import DB
from datetime import date



class NotesWindow(QDialog, Ui_edit_notes):
    # signal to show note was handled successfully
    note_signal = pyqtSignal(str)
    def __init__(self, table = None, name = None):
        super(NotesWindow, self).__init__()
        self.table = table
        self.name = name
        self.setupUi(self)
        self.setModal(True)

        # check the first radiobutton
        self.hbox_importance.itemAt(0).widget().setChecked(True)

        # handle the slot connections
        self.btn_discard.clicked.connect(self.notes_window_discard_clicked)
        self.btn_save.clicked.connect(self.notes_window_save_clicked)

        if table is not None and name is not None:
            self.load_data(table, name)

    def notes_window_discard_clicked(self):
        self.hide()

    # handle save click
    def notes_window_save_clicked(self):

        # Get the values from the form
        name = self.ldt_note_title.text()
        body = self.txtedt_note_body.toPlainText()
        priority = self.hbox_importance.itemAt(0).widget().text()
        current_date = date.today().strftime("%B %d, %Y")

        importance_container = self.hbox_importance

        # get the priority from the note window
        for i in range(0, 3):
            priority_box = importance_container.itemAt(i).widget()
            if priority_box.isChecked():
                priority = priority_box.text()
        
        # make the note tuple to send to database
        note = (
            name,
            body,
            priority,
            current_date
        )

        # Send a Message if there is missing data
        if not name or not body:
            Message("There are missing fields. Please make sure your note has a title and a body.", "Missing Fields")

        # Check if there is a title and body
        else:
            if self.table == None and self.name == None:
                
                # Check if name is already in database
                db = DB()
                items = db.read("notes")

                # save the notes if there are no notes
                if  len(items) == 0:
                    db = DB()
                    db.save("notes", note)
                    self.note_signal.emit("note saved")
                    self.hide()
                
                # save if there are already notes and check if the note doesn't already exist
                for i in range(0, len(items)):
                    if items[i][0] == name:
                        Message("The title you entered is already being used. Please Choose a different title", "title already used.")
                        break
                    # Make sure it's not an edit
                    elif i + 1 == len(items):
                        db = DB()
                        db.save("notes", note)
                        self.note_signal.emit("note saved")
                        self.hide()           
            # Update the existing note in the database
            else:
                db = DB()
                db.update(self.table, self.name, note)
                self.note_signal.emit("note saved")
                self.hide()
    
    # load the data if the window is opened in edit mode
    def load_data(self, table, name):
        db = DB()
        
        # get the data from database
        item = db.get_item(table, name)
        title = item[0]
        body = item[1]
        priority = item[2]

        # put the data in the window
        self.ldt_note_title.setText(title)
        self.txtedt_note_body.setText(body)
        count = self.hbox_importance.count()

        for i in range(count):
            widget = self.hbox_importance.itemAt(i).widget()
            if priority == widget.text():
                widget.setChecked(True)
