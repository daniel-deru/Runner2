from uipy.deleteNotes import Ui_DeleteWindow
from PyQt5.QtWidgets import QCheckBox, QDialog
from PyQt5.QtCore import pyqtSignal

from db import DB

class DeleteWindow(QDialog, Ui_DeleteWindow):
    delete_signal = pyqtSignal(str)
    def __init__(self, window):
        super(DeleteWindow, self).__init__()
        self.window_name = window
        self.setupUi(self)
        self.setModal(True)

        self.btn_discard.clicked.connect(self.discard_clicked)
        self.btn_delete.clicked.connect(self.delete_clicked)

        
        db = DB()
        items = db.read(window)

        for item in items:
            checkbox = QCheckBox(item[0])
            self.verticalLayout_2.addWidget(checkbox)
        
       
    
    def discard_clicked(self):
        self.hide()

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

