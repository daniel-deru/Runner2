from uipy.deleteNotes import Ui_DeleteWindow
from PyQt5.QtWidgets import QCheckBox, QDialog
from PyQt5.QtCore import pyqtSignal
import os
import sys
db_path = os.path.abspath(os.getcwd())
sys.path.insert(0, db_path)

from database.db import DB

class DeleteWindow(QDialog, Ui_DeleteWindow):
    # signal to be sent when delete was successfull
    delete_signal = pyqtSignal(str)
    def __init__(self, window):
        super(DeleteWindow, self).__init__()
        # get the window name to determine what to delete
        self.window_name = window
        self.setupUi(self)
        self.setModal(True)

        # connect signals to slots
        self.btn_discard.clicked.connect(self.discard_clicked)
        self.btn_delete.clicked.connect(self.delete_clicked)

        
        db = DB()
        items = db.read(window)

        # show the items in the window
        for item in items:
            checkbox = QCheckBox(item[0])
            self.verticalLayout_2.addWidget(checkbox)
        
       
    
    def discard_clicked(self):
        self.hide()

    # delete the selected items
    def delete_clicked(self):
        items = self.verticalLayout_2.count()

        
        for index in range(0, items):
            checkbox = self.verticalLayout_2.itemAt(index).widget()
            if checkbox.isChecked():
                item = checkbox.text()
                db = DB()
                db.delete(self.window_name, item)
          
        self.delete_signal.emit("delete completed")
        self.close()

