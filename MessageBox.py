from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QFont

class Message:
    def __init__(self, text, title):
        font = QFont("Roboto", 16)
        message = QMessageBox()
        message.setIcon(QMessageBox.Warning)
        message.setText(text)
        message.setWindowTitle(title)
        message.setFont(font)
        message.exec_()