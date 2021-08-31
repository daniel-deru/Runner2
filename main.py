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
from PyQt5.QtCore import Qt, pyqtSignal

# Import the main window UI
from uipy.mainUI import Ui_Runner

# Import Files Windows
from Add_category import CategoryWindow

# Import notes windows
from Delete import DeleteWindow
from SelectWindow import SelectNotesWindow
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
        make_category.exec_()

    def add_notes_clicked(self):
        make_note = NotesWindow()
        make_note.note_signal.connect(self.update)
        make_note.exec_()
        

    def show_notes(self):

        # This is to remove the previous widgets that were painted so the widgets don't get added twice
        prevItems = self.notes_scroll_layout.count()
        # check if there are widgets
        if prevItems > 0:
            for i in range(self.notes_scroll_layout.count()):
                item = self.notes_scroll_layout.itemAt(i)
                if item.widget():
                    item.widget().deleteLater()
                elif item.spacerItem():
                    self.notes_scroll_layout.removeItem(item.spacerItem())

        # get notes from the database
        db = DB()
        notes = db.read("notes")

        # add notes to the window
        for note in notes:
            n = make_note_container(note)
            self.notes_scroll_layout.addWidget(n)
        
        # add spacer to push widgets to the top
        spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.notes_scroll_layout.addItem(spacer)

    def notes_delete_clicked(self):
        delete_notes = DeleteWindow("notes")
        delete_notes.delete_signal.connect(self.update)
        delete_notes.exec_()

    def notes_edit_clicked(self):
        select_notes = SelectNotesWindow("notes")
        select_notes.edit_signal.connect(self.update)
        select_notes.exec_()
    
    def update(self):
        self.show_notes()

    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())
