from PyQt5.QtCore import pyqtSignal
from uipy.selectNotesUI import Ui_SelectWindow
from PyQt5.QtWidgets import  QDialog, QRadioButton
from db import DB
from Notes import NotesWindow
from Add_category import CategoryWindow

class SelectWindow(QDialog, Ui_SelectWindow):
    edit_signal = pyqtSignal(str)
    def __init__(self, table):
        super(SelectWindow, self).__init__()
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
                    if self.table == "notes":
                        note = NotesWindow(self.table, name)
                        note.note_signal.connect(self.send_signal)
                        note.exec_()
                    elif self.table == "categories":
                        app = CategoryWindow(name)
                        app.category_signal.connect(self.send_signal)
                        app.exec_()

                    self.hide()

    def discard_clicked(self):
        self.hide()
    
    def send_signal(self):
            self.edit_signal.emit("note saved")
        


    
        