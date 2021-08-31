# Python Imports
from  PyQt5.QtWidgets import QDialog, QFileDialog
from PyQt5.QtCore import pyqtSignal

# Import the URL Window UI
from uipy.add_File import Ui_Add_File_Dialog

# Import the message box
from class_snippets.MessageBox import Message


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

        if ( not name and not self.path):
            Message("Please enter a name and add a file", "Empty fields")     
        elif (name and self.path):
            from Add_category import files
            from Add_category import CategoryWindow

            is_copy = False

            for file in files:
                if (name == file['name']):
                    Message("The name is already being used. Please use another name", "Name already exists.")
                    is_copy = True
                elif (self.path == file['path']):
                    Message("The file is already selected. Cannot add the same file.", "File already exists.")
                    is_copy = True
            
            if (not is_copy):
                payload = {
                    'name': name,
                    'path': self.path,
                    "active": True
                }

                files.append(payload)
                
                make_category = CategoryWindow()
                make_category.exec()
                self.hide()

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

       