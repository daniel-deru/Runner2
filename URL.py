# Python Imports
from  PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import pyqtSignal

# Import the URL Window UI
from uipy.add_url import Ui_add_url_window

# Import the message box
from class_snippets.MessageBox import Message


class URLWindow(QDialog, Ui_add_url_window):

    def __init__(self, *args, **kwargs):
        super(URLWindow, self).__init__(*args, **kwargs)

        self.setupUi(self)
        self.setWindowTitle("Add Website")

        # Connections to button click events
        self.btn_discard.clicked.connect(self.discard_clicked)
        self.btn_save.clicked.connect(self.save_clicked)
        
    # Handle the Discard button click
    def discard_clicked(self):
        # Import the Category window to create a new instance
        # Important!!!! the reason why it is imported here is to avoid the circular import error
        from Add_category import CategoryWindow

        # Make the Category window and move to it
        make_category = CategoryWindow()
        make_category.exec()
        self.hide()
    
    # Handle the Save Button click
    def save_clicked(self):
        

        # Get the info from URL Window
        name = self.lnedit_name.text()
        path = self.lnedit_url.text()

        # If there is a name and url create a payload to store in website variable
        if ( not name and not path):
            # If the user didn't enter all the required information show a message
            Message("Please fill in all the fields", "There are empty fields")
        elif (name and path):
            # Import the Category window to create a new instance
            # Important!!!! the reason why it is imported here is to avoid the circular import error
            from Add_category import CategoryWindow
            # Import the websites from the category window to add the websites
            from Add_category import files

            is_copy = False

            for file in files:
                if (name == file['name']):
                    Message("The name is already being used. Please use another name", "Name already exists.")
                    is_copy = True
                elif (path == file['path']):
                    Message("The website is already being used. Cannot add the same website.", "Website already exists.")
                    is_copy = True
            
            if (not is_copy):
                payload = {
                    "name": name,
                    "path": path
                }
        
                files.append(payload)

                # Make the Category window and move to it
                make_category = CategoryWindow()
                make_category.exec()
                self.hide()
            
    
    # Create a new instance of the Category Window when the user closes the URL window
    def closeEvent(self, event):
        if (event):
            from Add_category import CategoryWindow
            make_category = CategoryWindow()
            make_category.exec()