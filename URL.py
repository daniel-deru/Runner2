from  PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import pyqtSignal

from uipy.add_url import Ui_add_url_window




from MessageBox import Message



class URLWindow(QDialog, Ui_add_url_window):

    def __init__(self, *args, **kwargs):
        super(URLWindow, self).__init__(*args, **kwargs)

        self.setupUi(self)
        # self.setModal(True)

        self.btn_discard.clicked.connect(self.discard_clicked)

        self.btn_save.clicked.connect(self.save_clicked)
        
    
    def discard_clicked(self):
        self.hide()
    
    def save_clicked(self):

        from Add_category import websites

        name = self.lnedit_name.text()
        url = self.lnedit_url.text()

        if (name and url):
            payload = {
                "name": name,
                "url": url
            }
    
            websites.append(payload)

            print(websites)

            from Add_category import CategoryWindow

            make_category = CategoryWindow()
            make_category.exec()
            self.hide()
        else:
            Message("Please fill in all the fields", "There are empty fields")
    
    def closeEvent(self, event):
        if (event):
            from Add_category import CategoryWindow
            make_category = CategoryWindow()
            make_category.exec()