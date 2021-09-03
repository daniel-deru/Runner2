from PyQt5.QtWidgets import  QCheckBox, QDialog
from PyQt5.QtCore import pyqtSignal

# Import Add Category UI
from uipy.add_categoryUI import Ui_add_category

# Import the Windows
from URL import URLWindow
from File import FileWindow

# Import Database
from db import DB

# Import message box
from class_snippets.MessageBox import Message

# container to keep all the websites data in memory before the app category is
# created and saved in the database
files = []

class CategoryWindow(QDialog, Ui_add_category):
    category_signal = pyqtSignal(str)
    def __init__(self, name=None):
        super(CategoryWindow, self).__init__()
        self.name = name
        self.setupUi(self)
        self.setModal(True)

        self.show_files()

        if name != None:
            self.load_data(name)
        
        # Connections to button click events
        # Important Note the lbl is actually a button
        self.lbl_save.clicked.connect(self.add_category_save_clicked)
        self.lbl_discard.clicked.connect(self.add_category_discard_clicked)
        self.lbl_add_url.clicked.connect(self.add_url_clicked)
        self.lbl_add_file.clicked.connect(self.add_file)
        self.btn_delete.clicked.connect(self.delete_clicked)
    
    # Handle the Save button click
    def add_category_save_clicked(self):
        
        category_name = self.add_category_name_input.text()

        if (category_name):
            
            # Check if the category is in the database
            db = DB()
            categories = db.read("categories")
            
            # if db is empty then just add the data
            if len(categories) == 0:
                print("if check is running")
                self.save_db(category_name)                
            # if the database isn't empty than do the following
            else:
                category_count = len(categories)
                for i in range(0, category_count):
                    # send a message that the category already exists and break out of the loop
                    if self.name == None:
                        if categories[i][0] == category_name:
                            Message("The category name you entered already exists. Please enter a unique category name", "Invalid Name")
                            break
                        # check to make sure the loop went through the whole database and add the data if the data doesn't exist 
                        elif i + 1 == category_count: 
                            self.save_db(category_name)
                    else:
                        self.save_db(category_name)

        else:
            Message( "Please enter the name of your category", "Please enter a name")
   

    # Handle the Discard button click
    def add_category_discard_clicked(self):
        
        for item in range(0, len(files)):
            files.pop()

        self.hide()

    # Open the URL Window 
    def add_url_clicked(self):
        url = URLWindow()
        url.url_signal.connect(self.updated)
        url.exec_()

    # Remove the websites from memory if the user closes the window
    def closeEvent(self, event):
        if (event):
            for item in range(0, len(files)):
                files.pop()


    def add_file(self):
        file_window = FileWindow()
        file_window.file_signal.connect(self.updated)
        file_window.exec_()

    def delete_clicked(self):
        container = self.vbox_container
        for i in range(0, container.count()):
            if container.itemAt(i).widget():
                if container.itemAt(i).widget().isChecked():
                    files.pop(i)
        
        self.show_files()
    
    def save_db(self, category_name):
        db_files = []
        
        for i in range(0, len(files)):

            # add file id
            file_id = self.make_id(category_name, files[i][0], files[i][1])
            files[i].append(category_name)
            files[i].append(file_id)
            db_file = tuple(files[i])
            db_files.append(db_file)
            self.hide()
        print(db_files)
        
        if self.name == None:
            db = DB()
            db.save("categories", (category_name, 1))

            
            db2 = DB()
            db2.save("files", db_files)
        else:
            db = DB()
            db.update("categories", self.name, (category_name, 1))

            db2 = DB()
            db2.update("files", self.name, db_files)

        for item in range(0, len(files)):
            files.pop()

        self.category_signal.emit("category saved")

    def updated(self, event):
        if event == "url added" or event == "file added":
            self.show_files()
    
    def make_id(self, category_name, file_name, file_path):
        category = 0
        name = 0
        path = 0

        for char in category_name:
            category += ord(char)

        for char in file_name:
            name += ord(char)

        for char in file_path:
            path += ord(char)
        
        file_id = str(category) + str(name) + str(path)
        return int(file_id) 
        
     
    def show_files(self):
        container = self.vbox_container

        count = container.count()
        for i in range(count):
            if container.itemAt(i).widget():
                container.itemAt(i).widget().deleteLater()
    
        if len(files) > 0:
            for file in files:
                checkbox = QCheckBox()
                checkbox.setText(file[0])
                checkbox.setChecked(file[2])
                checkbox.stateChanged.connect(lambda: self.checkbox_event_handler(checkbox.text(), checkbox.isChecked()))
                container.addWidget(checkbox)
    
    def load_data(self, name):
        db = DB()
        db_files = db.read("files", "category_name", name)

        self.add_category_name_input.setText(name)

        for file in db_files:
            file = file[0:3]
            files.append(list(file))

        self.show_files()
    
    def checkbox_event_handler(self, name, state):
        value = 1 if state == True else 0
        for file in files:
            if file[0] == name:
                file[2] = value       