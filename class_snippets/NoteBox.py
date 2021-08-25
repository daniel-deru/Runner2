from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout,QSpacerItem, QSizePolicy
from PyQt5.QtCore import Qt


class Note(QWidget):
    def __init__(self):
        super(Note)

    def make_note_container(self):
        note_container = QWidget()
        note_container.setObjectName("note_container")
        note_layout = QVBoxLayout()
        note_container.setLayout(note_layout)

        label_container = QHBoxLayout()
        button_container = QHBoxLayout()

        note = QLabel("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Feugiat odio lectus sagittis convallis amet, tortor arcu. Pellentesque bibendum sem dolor lacus urna, orci, pellentesque. Rhoncus ut mauris cras elit nisi, tellus. Augue bibendum faucibus at porttitor nullam adipiscing tincidunt.")
        note.setWordWrap(True)
        note.setObjectName("label")

        title = QLabel("Title")
        priority = QLabel("Priority")
        date = QLabel("25 Aug 2021")

        priority.setAlignment(Qt.AlignHCenter)
        date.setAlignment(Qt.AlignRight)

        label_container.addWidget(title)
        label_container.addWidget(priority)
        label_container.addWidget(date)

        edit_btn = QPushButton("Edit")
        delete_btn = QPushButton("Delete")
        button_spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        edit_btn.setMaximumSize(100, 100)
        delete_btn.setMaximumSize(100, 100)
        edit_btn.setMinimumSize(100, 0)
        delete_btn.setMinimumSize(100, 0)

        button_container.addWidget(edit_btn)
        button_container.addItem(button_spacer)
        button_container.addWidget(delete_btn)

        note_layout.addLayout(label_container)
        note_layout.addWidget(note)
        note_layout.addLayout(button_container)

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

            QPushButton {
                font-size: 16px;
                background-color: transparent;
                border: 2px solid #007EA6;
                border-radius: 10px;
                padding: 5px;
                color: #007EA6;
            }

            QPushButton:pressed {
                color: white;
                background-color: #007EA6;
            }

        """)
    
        return note_container
        
        