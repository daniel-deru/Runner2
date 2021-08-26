from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout,QSpacerItem, QSizePolicy
from PyQt5.QtCore import Qt
# from db import DB


# class Note:
        

def make_note_container(data):
    note_container = QWidget()
    note_container.setObjectName("note_container")
    note_layout = QVBoxLayout()
    note_container.setLayout(note_layout)

    label_container = QHBoxLayout()
    date_container = QHBoxLayout()

    note = QLabel(data[1])
    note.setWordWrap(True)
    note.setObjectName("label")

    title = QLabel(data[0])
    priority = QLabel(data[2])
    date = QLabel(data[3])

    priority.setAlignment(Qt.AlignHCenter)
    date.setAlignment(Qt.AlignRight)

    label_container.addWidget(title)
    label_container.addWidget(priority)
    

    button_spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

    date_container.addItem(button_spacer)
    date_container.addWidget(date)
    

    note_layout.addLayout(label_container)
    note_layout.addWidget(note)
    note_layout.addLayout(date_container)

    note_container.setStyleSheet("""
        #note_container {
            background-color: white;
            min-height: 150px;
            font-size: 16px;
            border-radius: 10px;
        }
        QLabel {
            height: 10px;
            font-size: 20px;
            color: #007EA6;
        }

        #label {
            font-size: 16px;
            color: black;
            }

    """)
    return note_container

        
        