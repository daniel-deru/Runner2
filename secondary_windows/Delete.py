import os
import sys
db_path = os.path.abspath(os.getcwd())
sys.path.insert(0, db_path)

from uipy.deleteNotes import Ui_DeleteWindow

from PyQt5.QtWidgets import QCheckBox, QDialog
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QFont, QFontDatabase, QIcon

from database.db import DB

checkbox_styles = """
     QCheckBox::indicator {
        width: 15px;
        height: 15px
    }
    QCheckBox::indicator:checked {
        image: url(images/tick.png);
        width: 15px;
        height: 15px
    }
    QCheckBox::indicator:unchecked {
        image: url(images/cross.png);
        width: 15px;
        height: 15px;
    }
"""

class DeleteWindow(QDialog, Ui_DeleteWindow):
    # signal to be sent when delete was successfull
    delete_signal = pyqtSignal(str)
    def __init__(self, window):
        super(DeleteWindow, self).__init__()
        # get the window name to determine what to delete
        self.window_name = window
        self.setupUi(self)
        self.setModal(True)

        self.setWindowIcon(QIcon("images/WorkMate.png"))
        self.setWindowTitle(f"Delete {window.capitalize()}")
        QFontDatabase.addApplicationFont("fonts/Nunito-SemiBoldItalic.ttf")
        app_font = QFont("Nunito SemiBold")

        self.btn_discard.setFont(app_font)
        self.btn_delete.setFont(app_font)

        # connect signals to slots
        self.btn_discard.clicked.connect(self.discard_clicked)
        self.btn_delete.clicked.connect(self.delete_clicked)

        
        db = DB()
        items = db.read(window)

        # show the items in the window
        for item in items:
            checkbox = QCheckBox(item[0])
            checkbox.setFont(app_font)
            checkbox.setStyleSheet(checkbox_styles)
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

