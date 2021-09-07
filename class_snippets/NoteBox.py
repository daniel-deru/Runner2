from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout,QSpacerItem, QSizePolicy
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QFontDatabase

        

def make_note_container(data):
    QFontDatabase.addApplicationFont("fonts/Nunito-SemiBoldItalic.ttf")
    app_font = QFont("Nunito SemiBold", 18)
    
    note_container = QWidget()
    note_container.setObjectName("note_container")
    note_layout = QVBoxLayout()
    note_container.setLayout(note_layout)
    note_container.setFont(app_font)

    label_container = QHBoxLayout()
    date_container = QHBoxLayout()

    title_text = data[0]
    note_text = data[1]
    priority_text = data[2]
    date_text = data[3]


    note = QLabel(note_text)
    note.setWordWrap(True)
    note.setObjectName("note")
    note.setFont(app_font)

    title = QLabel(title_text)
    title.setObjectName("title")
    title.setFont(app_font)

    low, medium, high = "90FA00", "FAE700", "D60025"
    priority_color = high if priority_text == "High" else medium if priority_text == "Medium" else low

    priority = QLabel(priority_text)
    priority.setObjectName("priority")
    priority.setAlignment(Qt.AlignRight)
    priority.setFont(app_font)
    priority.setStyleSheet(f"color: #{priority_color};")

    date = QLabel(date_text)
    date.setObjectName("date")
    date.setAlignment(Qt.AlignRight)
    date.setFont(app_font)


    label_container.addWidget(title)
    label_container.addWidget(priority)

    spacer = QSpacerItem(20, 10, QSizePolicy.Expanding, QSizePolicy.Minimum)
    date_container.addItem(spacer)
    date_container.addWidget(date)

    note_layout.addLayout(label_container)
    note_layout.addWidget(note)
    note_layout.addLayout(date_container)

    note_container.setStyleSheet("""
        #note_container {
            background-color: white;
            min-height: 50px;
            font-size: 16px;
            border-radius: 10px;
        }
        QLabel {
            font-size: 20px;
            color: #007EA6;
        }

        #note {
            font-size: 16px;
            color: black;
            }

        #date {
            font-size: 12px;
        }
    """)
    return note_container

        
        