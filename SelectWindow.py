from PyQt5.QtCore import pyqtSignal
from uipy.selectNotesUI import Ui_SelectWindow
from PyQt5.QtWidgets import  QDialog, QRadioButton
from db import DB
from Notes import NotesWindow

class SelectNotesWindow(QDialog, Ui_SelectWindow):
    def __init__(self, table):
        super(SelectNotesWindow, self).__init__()
        self.table = table
        self.setupUi(self)
        self.setModal(True)
        self.show(table)

        self.btn_discard.clicked.connect(self.discard_clicked)
        self.btn_edit.clicked.connect(self.edit_clicked)
    

    def show(self, table):
        db = DB()
        items = db.read(table)
        self.make_buttons(items)

    def make_buttons(self, items):
        for item in items:
            name = item[0]
            self.radio = QRadioButton(name)
            self.radio.setStyleSheet("""
                QPushButton {
                    font-size: 16px;
                    color: white;
                    border: 2px solid white;
                    border-radius: 10px;
                    padding: 5px;
                    background-color: transparent;
                }

                QPushButton:pressed {
                    color: #007ea6;
                    background-color: white;
                }
            """)
            self.verticalLayout.addWidget(self.radio)

    def edit_clicked(self):
        items = self.verticalLayout.count()

        name = ""
        for i in range(items):
            item = self.verticalLayout.itemAt(i)
            if item.widget():
                if item.widget().isChecked():
                    name = item.widget().text()
                    self.hide()
                    note = NotesWindow(self.table, name)
                    note.exec_()

    def discard_clicked(self):
        self.hide()


    
        