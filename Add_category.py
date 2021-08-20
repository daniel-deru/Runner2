from PyQt5.QtWidgets import  QCheckBox, QDialog, QFileDialog
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QFont


# Import Add Category UI
from uipy.add_categoryUI import Ui_add_category

# Import the URL Window
from URL import URLWindow

from File import FileWindow

# container to keep all the websites data in memory before the app category is
# created and saved in the database
files = []

class CategoryWindow(QDialog, Ui_add_category):
    def __init__(self, *args, **kwargs):
        super(CategoryWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.setModal(True)

        self.show_websites()
        
        # Connections to button click events
        # Important Note the lbl is actually a button
        self.lbl_save.clicked.connect(self.add_category_save_clicked)
        self.lbl_discard.clicked.connect(self.add_category_discard_clicked)
        self.lbl_add_url.clicked.connect(self.add_url_clicked)
        self.lbl_add_file.clicked.connect(self.add_file)

    # Handle the Save button click
    def add_category_save_clicked(self):

        for item in range(0, len(files)):
            files.pop()
        
        category_name = self.lbl_name.text()

        if (category_name):
            
            self.hide()

    # Handle the Discard button click
    def add_category_discard_clicked(self):
        
        for item in range(0, len(files)):
            files.pop()

        self.hide()

    # Open the URL Window 
    def add_url_clicked(self):
        self.hide()
        url = URLWindow()
        url.exec()

    # Remove the websites from memory if the user closes the window
    def closeEvent(self, event):
        if (event):
            for item in range(0, len(files)):
                files.pop()


    def add_file(self):
        self.hide()
        file_window = FileWindow()
        file_window.exec()
        
    
    def show_websites(self):
        container = self.vbox_container
        
        if (len(files) > 0):
            for website in files:
                checkbox = QCheckBox()
                checkbox.setText(website['name'])
                container.addWidget(checkbox)
            
   