from typing import Coroutine
from PyQt5.QtWidgets import  QCheckBox, QDialog
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QFont
from PyQt5.sip import delete


# Import Add Category UI
from uipy.add_categoryUI import Ui_add_category

# Import the Windows
from URL import URLWindow
from File import FileWindow
from Delete import DeleteWindow

# Import message box
from class_snippets.MessageBox import Message

# container to keep all the websites data in memory before the app category is
# created and saved in the database
files = []

class CategoryWindow(QDialog, Ui_add_category):
    def __init__(self, *args, **kwargs):
        super(CategoryWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.setModal(True)

        self.show_files()
        
        # Connections to button click events
        # Important Note the lbl is actually a button
        self.lbl_save.clicked.connect(self.add_category_save_clicked)
        self.lbl_discard.clicked.connect(self.add_category_discard_clicked)
        self.lbl_add_url.clicked.connect(self.add_url_clicked)
        self.lbl_add_file.clicked.connect(self.add_file)
        self.btn_delete.clicked.connect(self.delete_clicked)

    # Handle the Save button click
    def add_category_save_clicked(self):

        category_name = self.add_category_name_input.text()

        if (category_name):
            # Check if the category is in the database
            self.hide()
            print(files)
        else:
            Message( "Please enter the name of your category", "Please enter a name")
        
        for item in range(0, len(files)):
            files.pop()

    # Handle the Discard button click
    def add_category_discard_clicked(self):
        
        for item in range(0, len(files)):
            files.pop()

        self.hide()

    # Open the URL Window 
    def add_url_clicked(self):
        self.hide()
        url = URLWindow()
        url.exec_()

    # Remove the websites from memory if the user closes the window
    def closeEvent(self, event):
        if (event):
            for item in range(0, len(files)):
                files.pop()


    def add_file(self):
        self.hide()
        file_window = FileWindow()
        file_window.exec_()

    def delete_clicked(self):
        container = self.vbox_container
        # filtered = filter(lambda x: x["active"] == True, files)
        for i in range(0, container.count()):
            if container.itemAt(i).widget():
                print(container.itemAt(i).widget().isChecked())
        
        
        self.show_files()
        
    def show_files(self):
        container = self.vbox_container

        count = container.count()
        for i in range(count):
            if container.itemAt(i).widget():
                container.itemAt(i).widget().deleteLater()
        
        if len(files) > 0:
            for file in files:
                checkbox = QCheckBox()
                checkbox.setText(file['name'])
                checkbox.setChecked(True)
                container.addWidget(checkbox)
            