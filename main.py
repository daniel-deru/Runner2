# Python Imports
import os
import sys
import json
import re
import webbrowser
from os import path as file
from inspect import currentframe, getframeinfo

# PyQt5 imports
from PyQt5.QtWidgets import QApplication, QCheckBox, QHBoxLayout, QLabel, QPushButton, QVBoxLayout, QWidget, QSpacerItem, QSizePolicy
from PyQt5.QtCore import Qt

# Import the main window UI
from uipy.mainUI import Ui_Runner

# Import Files Windows
from Add_category import CategoryWindow

# Import notes windows
from DeleteNotes import DeleteNotesWindow
from SelectNotes import SelectNotesWindow
from Notes import NotesWindow

from db import DB

from class_snippets.NoteBox import make_note_container


class Main(QWidget, Ui_Runner):
    def __init__(self):
        super(Main, self).__init__()
        
        self.setWindowTitle("Runner")
        self.setupUi(self)
        
        self.tabWidget.setCurrentIndex(0)

        # Handle Button Click
        self.main_add_category_btn.clicked.connect(self.add_category_clicked)
        self.main_add_notes_btn.clicked.connect(self.add_notes_clicked)
        self.btn_notes_delete.clicked.connect(self.notes_delete_clicked)
        self.btn_notes_edit.clicked.connect(self.notes_edit_clicked)
 
        self.show_notes()
    @staticmethod
    def add_category_clicked():
        make_category = CategoryWindow()
        make_category.exec()

    def add_notes_clicked(self):
        make_note = NotesWindow()
        make_note.exec()
        

    def show_notes(self):

        db = DB()
        notes = db.read("notes")

        for note in notes:
            print(note)
            n = make_note_container(note)
            self.notes_scroll_layout.addWidget(n)
        
        spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.notes_scroll_layout.addItem(spacer)

    def notes_delete_clicked(self):
        delete_notes = DeleteNotesWindow()
        delete_notes.exec()

    def notes_edit_clicked(self):
        select_notes = SelectNotesWindow()
        select_notes.exec()
      
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())
