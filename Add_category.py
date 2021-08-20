from PyQt5.QtWidgets import  QDialog
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QFont


# Import Add Category UI
from uipy.add_categoryUI import Ui_add_category

# Import URL window UI
from uipy.add_url import Ui_add_url_window

from MessageBox import Message

from URL import URLWindow

websites = []

class CategoryWindow(QDialog, Ui_add_category):
    def __init__(self, *args, **kwargs):
        super(CategoryWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.setModal(True)
        self.url = URLWindow()
        # Handle Save Button Clicked
        self.add_category_save_btn.clicked.connect(self.add_category_save_clicked)

        # Handle discard button clicked
        self.add_category_discard_btn.clicked.connect(self.add_category_discard_clicked)

        # Handle Add URL clicked
        self.add_category_add_url_btn.clicked.connect(self.add_url_clicked)

    def add_category_save_clicked(self):

        for item in range(0, len(websites)):
            websites.pop()

        self.hide()

    def add_category_discard_clicked(self):
        
        for item in range(0, len(websites)):
            websites.pop()

        self.hide()

    def add_url_clicked(self):
        self.hide()
        self.url.exec()

    def closeEvent(self, event):
        if (event):
            for item in range(0, len(websites)):
                websites.pop()
        



# class URLWindow(QDialog, Ui_add_url_window):

#     send_signal = pyqtSignal(str)
#     def __init__(self, *args, **kwargs):
#         super(URLWindow, self).__init__(*args, **kwargs)

#         self.setupUi(self)
#         # self.setModal(True)

#         self.btn_discard.clicked.connect(self.discard_clicked)

#         self.btn_save.clicked.connect(self.save_clicked)
        
    
#     def discard_clicked(self):
#         self.hide()
    
#     def save_clicked(self):

#         name = self.lnedit_name.text()
#         url = self.lnedit_url.text()

#         if (name and url):
#             payload = {
#                 "name": name,
#                 "url": url
#             }
#             websites.append(payload)

#             print(websites)

#             make_category = CategoryWindow()
#             make_category.exec()
#             self.hide()
#         else:
#             Message("Please fill in all the fields", "There are empty fields")
        
       


