# Python Imports
import os
import sys
import json
import re
import webbrowser
from os import path as file
from inspect import currentframe, getframeinfo

# PyQt5 imports
from PyQt5.QtWidgets import QApplication, QPushButton, QTabWidget, QWidget, QMainWindow
from PyQt5 import uic

# Import the main window UI
from uipy.mainUI import Ui_Runner

# Import windows
from Add_category import CategoryWindow
from Notes import NotesWindow


class Main(QWidget, Ui_Runner):
    def __init__(self):
        super(Main, self).__init__()
        
        self.setWindowTitle("Runner")
        self.setupUi(self)

        self.tabWidget.setCurrentIndex(0)

        # Handle Add Category Button Click
        self.main_add_category_btn.clicked.connect(self.add_category_clicked)

        #Handle Add Notes Button Click
        self.main_add_notes_btn.clicked.connect(self.add_notes_clicked)

        # Handle Add URL button Clicked
        
    
    def add_category_clicked(self):
        make_category = CategoryWindow()
        make_category.exec()

    def add_notes_clicked(self):
        make_note = NotesWindow()
        make_note.exec()

    

        
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())
