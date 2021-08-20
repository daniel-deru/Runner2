# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addUrl.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_add_url_window(object):
    def setupUi(self, add_url_window):
        add_url_window.setObjectName("add_url_window")
        add_url_window.resize(412, 150)
        add_url_window.setStyleSheet("QDialog {\n"
"    background-color: #007EA6;\n"
"    color: white;\n"
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(add_url_window)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frm_add_url = QtWidgets.QFormLayout()
        self.frm_add_url.setObjectName("frm_add_url")
        self.lbl_name = QtWidgets.QLabel(add_url_window)
        self.lbl_name.setStyleSheet("color: white;\n"
"font-size: 20px;")
        self.lbl_name.setObjectName("lbl_name")
        self.frm_add_url.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lbl_name)
        self.lnedit_name = QtWidgets.QLineEdit(add_url_window)
        self.lnedit_name.setStyleSheet("border-radius: 10px;\n"
"font-size: 20px;\n"
"padding: 5px;")
        self.lnedit_name.setObjectName("lnedit_name")
        self.frm_add_url.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lnedit_name)
        self.lbl_url = QtWidgets.QLabel(add_url_window)
        self.lbl_url.setStyleSheet("color: white;\n"
"font-size: 20px;")
        self.lbl_url.setObjectName("lbl_url")
        self.frm_add_url.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lbl_url)
        self.lnedit_url = QtWidgets.QLineEdit(add_url_window)
        self.lnedit_url.setStyleSheet("border-radius: 10px;\n"
"font-size: 20px;\n"
"padding: 5px;")
        self.lnedit_url.setObjectName("lnedit_url")
        self.frm_add_url.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lnedit_url)
        self.verticalLayout.addLayout(self.frm_add_url)
        self.hbox_url_buttons = QtWidgets.QHBoxLayout()
        self.hbox_url_buttons.setObjectName("hbox_url_buttons")
        self.btn_discard = QtWidgets.QPushButton(add_url_window)
        self.btn_discard.setStyleSheet("color: white;\n"
"border: 2px solid white;\n"
"background-color: transparent;\n"
"font-size: 20px;\n"
"border-radius: 10px;\n"
"padding: 5px;")
        self.btn_discard.setObjectName("btn_discard")
        self.hbox_url_buttons.addWidget(self.btn_discard)
        self.btn_save = QtWidgets.QPushButton(add_url_window)
        self.btn_save.setStyleSheet("color: white;\n"
"border: 2px solid white;\n"
"background-color: transparent;\n"
"font-size: 20px;\n"
"border-radius: 10px;\n"
"padding: 5px;")
        self.btn_save.setObjectName("btn_save")
        self.hbox_url_buttons.addWidget(self.btn_save)
        self.verticalLayout.addLayout(self.hbox_url_buttons)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.retranslateUi(add_url_window)
        QtCore.QMetaObject.connectSlotsByName(add_url_window)

    def retranslateUi(self, add_url_window):
        _translate = QtCore.QCoreApplication.translate
        add_url_window.setWindowTitle(_translate("add_url_window", "Add URL"))
        self.lbl_name.setText(_translate("add_url_window", "Name:"))
        self.lbl_url.setText(_translate("add_url_window", "URL:"))
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
