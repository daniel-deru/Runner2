from PyQt5.QtCore import QAbstractEventDispatcher
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QCheckBox, QLabel, QFrame


import os
import sys
import math
db_path = os.path.abspath(os.getcwd())
sys.path.insert(0, db_path)
from db import DB

def make_file_container(data):
    db = DB()
    files = db.read("files", "category_name", data[0])
    
    file_container = QWidget()
    file_container.setObjectName("file_container")

    file_layout = QVBoxLayout()
    file_container.setLayout(file_layout)

    frame = QFrame()
    frame.setObjectName("frame")
    title_hbox = QHBoxLayout()
    title_hbox.setObjectName("hbox_title")

    file_layout.addLayout(title_hbox)
    file_layout.addWidget(frame)

    title = QLabel()
    title.setObjectName("title")
    title.setText(data[0])
    active = QCheckBox()
    active.setObjectName("active")
    active.setText("Active")
    if data[1]:
        active.setChecked(True)
    
    title_hbox.addWidget(title)
    title_hbox.addWidget(active)

    frame_grid = QGridLayout()
    frame.setLayout(frame_grid)
    file_count = len(files)
    for i in range(0, file_count):
        
        checkbox = QCheckBox()
        checkbox.setObjectName("file")
        checkbox.setText(files[i][0])
        if files[i][2]:
            checkbox.setChecked(True)
        
        column = i % 2
        row = math.floor(i / 2)

        if column == 0:
            frame_grid.addWidget(checkbox, row, column)

        if column == 1:
            frame_grid.addWidget(checkbox, row, column)


    file_container.setStyleSheet("""
        #note_container {
            min-height: 100px;
        }
        #frame {
            border: 2px solid white;
            background-color: white;
            color: #007EA6;
            border-radius: 10px;
        }

        #title {
            font-size: 20px;
            color: white;
        }

        #active {
            font-size: 20px;
            color: white;
        }

        #file {
            color: black;
            background-color: white;
            font-size: 14px;
        }
    """)

    return file_container

# make_file_container(("test", 1))







