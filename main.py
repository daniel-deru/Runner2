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

# Import windows
from Add_category import CategoryWindow
from Notes import NotesWindow

from class_snippets.NoteBox import Note

from db import DB


class Main(QWidget, Ui_Runner):
    def __init__(self):
        super(Main, self).__init__()
        
        self.setWindowTitle("Runner")
        self.setupUi(self)

        self.tabWidget.setCurrentIndex(0)

        # Handle Add Category Button Click
        self.main_add_category_btn.clicked.connect(self.add_category_clicked)

        # Handle Add Notes Button Click
        self.main_add_notes_btn.clicked.connect(self.add_notes_clicked)

        note_container = Note().make_note_container()
        
        spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        
        self.notes_scroll_layout.addWidget(note_container)
        self.notes_scroll_layout.addItem(spacer)
        db = DB()
        note_data = db.read("notes")
        print(note_data)
        
        
    @staticmethod
    def add_category_clicked():
        make_category = CategoryWindow()
        make_category.exec()

    @staticmethod
    def add_notes_clicked():
        make_note = NotesWindow()
        make_note.exec()

    # def make_note_container(self):
        # note_container = QWidget()
        # note_container.setObjectName("note_container")
        # note_layout = QVBoxLayout()
        # note_container.setLayout(note_layout)

        # label_container = QHBoxLayout()
        # button_container = QHBoxLayout()

        # note = QLabel("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Feugiat odio lectus sagittis convallis amet, tortor arcu. Pellentesque bibendum sem dolor lacus urna, orci, pellentesque. Rhoncus ut mauris cras elit nisi, tellus. Augue bibendum faucibus at porttitor nullam adipiscing tincidunt.")
        # note.setWordWrap(True)
        # note.setObjectName("label")

        # title = QLabel("Title")
        # priority = QLabel("Priority")
        # date = QLabel("25 Aug 2021")

        # priority.setAlignment(Qt.AlignHCenter)
        # date.setAlignment(Qt.AlignRight)

        # label_container.addWidget(title)
        # label_container.addWidget(priority)
        # label_container.addWidget(date)

        # edit_btn = QPushButton("Edit")
        # delete_btn = QPushButton("Delete")
        # button_spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        # edit_btn.setMaximumSize(100, 100)
        # delete_btn.setMaximumSize(100, 100)
        # edit_btn.setMinimumSize(100, 0)
        # delete_btn.setMinimumSize(100, 0)

        # button_container.addWidget(edit_btn)
        # button_container.addItem(button_spacer)
        # button_container.addWidget(delete_btn)

        # note_layout.addLayout(label_container)
        # note_layout.addWidget(note)
        # note_layout.addLayout(button_container)

        # note_container.setStyleSheet("""
        #     #note_container {
        #         background-color: white;
        #         min-height: 150px;
        #         font-size: 16px;
        #         border-radius: 10px;
        #     }
        #     QLabel {
        #         height: 10px;
        #         font-size: 20px;
        #         color: #007EA6;
        #     }

        #     #label {
        #         font-size: 16px;
        #         color: black;
        #      }

        #     QPushButton {
        #         font-size: 16px;
        #         background-color: transparent;
        #         border: 2px solid #007EA6;
        #         border-radius: 10px;
        #         padding: 5px;
        #         color: #007EA6;
        #     }

        #     QPushButton:pressed {
        #         color: white;
        #         background-color: #007EA6;
        #     }

        # """)
    
        # return note_container
        
 

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())
