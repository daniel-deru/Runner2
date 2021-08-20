# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_url.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_add_url_window(object):
    def setupUi(self, add_url_window):
        add_url_window.setObjectName("add_url_window")
        add_url_window.resize(500, 129)
        add_url_window.setMinimumSize(QtCore.QSize(300, 0))
        add_url_window.setMaximumSize(QtCore.QSize(16777215, 129))
        add_url_window.setStyleSheet("QDialog {\n"
"    background-color: #007EA6;\n"
"}\n"
"\n"
"QLabel {\n"
"    color: white;\n"
"    font-size: 16px;\n"
"}\n"
"\n"
"QPushButton {\n"
"    color: white;\n"
"    border: 2px solid white;\n"
"    border-radius: 10px;\n"
"    padding: 5px;\n"
"    font-size: 16px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    color: #007EA6;\n"
"    background-color: white;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    font-size: 16px;\n"
"    padding: 5px;\n"
"    border-radius: 5px;\n"
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(add_url_window)
        self.verticalLayout.setObjectName("verticalLayout")
        self.grid_add_url = QtWidgets.QGridLayout()
        self.grid_add_url.setObjectName("grid_add_url")
        self.lbl_name = QtWidgets.QLabel(add_url_window)
        self.lbl_name.setObjectName("lbl_name")
        self.grid_add_url.addWidget(self.lbl_name, 0, 0, 1, 1)
        self.lbl_url = QtWidgets.QLabel(add_url_window)
        self.lbl_url.setObjectName("lbl_url")
        self.grid_add_url.addWidget(self.lbl_url, 1, 0, 1, 1)
        self.lnedit_name = QtWidgets.QLineEdit(add_url_window)
        self.lnedit_name.setObjectName("lnedit_name")
        self.grid_add_url.addWidget(self.lnedit_name, 0, 1, 1, 1)
        self.lnedit_url = QtWidgets.QLineEdit(add_url_window)
        self.lnedit_url.setObjectName("lnedit_url")
        self.grid_add_url.addWidget(self.lnedit_url, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.grid_add_url)
        self.hbox_button_container = QtWidgets.QHBoxLayout()
        self.hbox_button_container.setObjectName("hbox_button_container")
        self.btn_discard = QtWidgets.QPushButton(add_url_window)
        self.btn_discard.setObjectName("btn_discard")
        self.hbox_button_container.addWidget(self.btn_discard)
        self.btn_save = QtWidgets.QPushButton(add_url_window)
        self.btn_save.setObjectName("btn_save")
        self.hbox_button_container.addWidget(self.btn_save)
        self.verticalLayout.addLayout(self.hbox_button_container)

        self.retranslateUi(add_url_window)
        QtCore.QMetaObject.connectSlotsByName(add_url_window)

    def retranslateUi(self, add_url_window):
        _translate = QtCore.QCoreApplication.translate
        add_url_window.setWindowTitle(_translate("add_url_window", "Dialog"))
        self.lbl_name.setText(_translate("add_url_window", "Name"))
        self.lbl_url.setText(_translate("add_url_window", "URL"))
        self.btn_discard.setText(_translate("add_url_window", "Discard"))
        self.btn_save.setText(_translate("add_url_window", "Save"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    add_url_window = QtWidgets.QDialog()
    ui = Ui_add_url_window()
    ui.setupUi(add_url_window)
    add_url_window.show()
    sys.exit(app.exec_())
