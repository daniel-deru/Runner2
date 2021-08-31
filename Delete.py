from uipy.deleteNotes import Ui_DeleteWindow
from PyQt5.QtWidgets import QCheckBox, QDialog
from PyQt5.QtCore import pyqtSignal

from db import DB

class DeleteWindow(QDialog, Ui_DeleteWindow):
    delete_signal = pyqtSignal(str)
    def __init__(self, window):
        super(DeleteWindow, self).__init__()

        self.setupUi(self)
        self.setModal(True)

        self.btn_discard.clicked.connect(self.discard_clicked)
        self.btn_delete.clicked.connect(self.delete_clicked)

        if window == "notes":
            db = DB()
            notes = db.read("notes")

            for note in notes:
                checkbox = QCheckBox(note[0])
                self.verticalLayout_2.addWidget(checkbox)
        
        else:
            from Add_category import files
            print(files)
    
    def discard_clicked(self):
        self.hide()

    def delete_clicked(self):
        items = self.verticalLayout_2.count()

        
        for index in range(0, items):
            item = self.verticalLayout_2.itemAt(index).widget()
            if item.isChecked():
                note = item.text()
                db = DB()
                db.delete("notes", note)
        self.delete_signal.emit("delete completed")
        self.close()

