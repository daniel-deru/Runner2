# Python Imports
from  PyQt5.QtWidgets import QDialog, QFileDialog
from PyQt5.QtCore import pyqtSignal

# Import the URL Window UI
from uipy.add_File import Ui_Add_File_Dialog

# Import the message box
from MessageBox import Message


class FileWindow(QDialog, Ui_Add_File_Dialog):

    def __init__(self, *args, **kwargs):
        super(FileWindow, self).__init__(*args, **kwargs)

        self.setupUi(self)
        self.setWindowTitle("Add File")

        # Connect button click to function
        self.btn_discard.clicked.connect(self.discard_clicked)
        self.btn_save.clicked.connect(self.save_clicked)
        self.btn_add_file.clicked.connect(self.add_file_clicked)
        

    def discard_clicked(self):
        from Add_category import CategoryWindow
        make_category = CategoryWindow()
        make_category.exec()
        self.hide()

    def save_clicked(self):

        name = self.lnedit_filename.text()

        if (name and self.path):
            from Add_category import files
            from Add_category import CategoryWindow
            payload = {
                'name': name,
                'path': self.path
            }

            files.append(payload)
            
            make_category = CategoryWindow()
            make_category.exec()
            self.hide()
        else:
            Message("Please enter a name and add a file", "Empty fields")

    def add_file_clicked(self):
        self.path = QFileDialog.getOpenFileName(self, "Open a file", "", "All Files (*.*)")[0]
        short_path  = self.path[0:30]
        display_path = f"Path: {short_path}..."

        self.lbl_path.setText(display_path)
        

    # Create a new instance of the Category Window when the user closes the URL window
    def closeEvent(self, event):
        if (event):
            from Add_category import CategoryWindow
            make_category = CategoryWindow()
            make_category.exec()

       