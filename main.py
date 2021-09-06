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
from SelectWindow import SelectWindow
from Notes import NotesWindow

from db import DB

# Import functions that make the notes and file containers (sub widgets)
from class_snippets.NoteBox import make_note_container
from class_snippets.FileBox import make_file_container


class Main(QWidget, Ui_Runner):
    def __init__(self):
        super(Main, self).__init__()
        
        self.setWindowTitle("Runner")
        self.setupUi(self)
        
        self.tabWidget.setCurrentIndex(0)

        # File connections
        self.main_add_category_btn.clicked.connect(self.add_category_clicked)
        self.apps_btn_delete.clicked.connect(self.delete_category_clicked)
        self.apps_btn_edit.clicked.connect(self.edit_category_clicked)
        self.btn_run.clicked.connect(self.run_clicked)

        # Note connections
        self.main_add_notes_btn.clicked.connect(self.add_notes_clicked)
        self.btn_notes_delete.clicked.connect(self.notes_delete_clicked)
        self.btn_notes_edit.clicked.connect(self.notes_edit_clicked)
 
        # show the notes and files when the window loads
        self.show_notes()
        self.show_files()

    # open category window to add categories
    def add_category_clicked(self):
        make_category = CategoryWindow()
        make_category.category_signal.connect(self.update)
        make_category.exec_()
    
    
    # Open select window to select which window to edit
    def edit_category_clicked(self):
        edit_category = SelectWindow("categories")
        edit_category.edit_signal.connect(self.update)
        edit_category.exec_()
    
    # Open the delete window to delete categories
    def delete_category_clicked(self):
        delete_category = DeleteWindow("categories")
        delete_category.delete_signal.connect(self.show_files)
        delete_category.exec_()

    # run the selected categories and files
    def run_clicked(self):
        category_container = self.verticalLayout_3
        item_count = len(category_container)
        for i in range(item_count):
            category = category_container.itemAt(i)
            if category.widget():
                category_widget_item = category.widget().children()
                title = category_widget_item[2].text()
                checkbox = category_widget_item[3]
                frame = category_widget_item[1]
                if checkbox.isChecked():
                    files = frame.children()[1:]
                    filtered_files = filter(lambda x: x.isChecked(), files)
                    for file in filtered_files:
                        db = DB()
                        paths = db.read("files", "name", file.text())
                        filtered_paths = list(filter(lambda x: x[3] == title, paths))
                        path = filtered_paths[0][1]
                        print(path)
                        

                

    # open the notes window to add notes
    def add_notes_clicked(self):
        make_note = NotesWindow()
        make_note.note_signal.connect(self.update)
        make_note.exec_()

    # open the delete window to delete notes
    def notes_delete_clicked(self):
        delete_notes = DeleteWindow("notes")
        delete_notes.delete_signal.connect(self.update)
        delete_notes.exec_()

    # open the select window to select which note to edit
    def notes_edit_clicked(self):
        select_notes = SelectWindow("notes")
        select_notes.edit_signal.connect(self.update)
        select_notes.exec_()
    
    # Helper methods
    def update(self, signal):
        self.show_files()
        self.show_notes()
    
    # function to paint the notes in the window
    def show_notes(self):

        self.clear_window(self.notes_scroll_layout)

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

    def show_files(self):
        # clear the window so it can be updated
        self.clear_window(self.verticalLayout_3)

        db = DB()
        categories = db.read("categories")

        # make the file container
        for category in categories:
            f = make_file_container(category, self.update_category)
            self.verticalLayout_3.addWidget(f)

        # add spacer at the bottom of the vboxlayout
        spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacer)
    
    # clears the window so it can be repainted
    @staticmethod
    def clear_window(container):
        # This is to remove the previous widgets that were painted so the widgets don't get added twice
        prevItems = container.count()
        # check if there are widgets
        if prevItems > 0:
            for i in range(container.count()):
                item = container.itemAt(i)
                if item.widget():
                    item.widget().deleteLater()
                elif item.spacerItem():
                    container.removeItem(item.spacerItem())
    
    # update the category active checkbox
    def update_category(self, name, state):
        value = 1 if state == True else 0
        db = DB()
        db.update_category_state(name, value)
        

    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())
