# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\SATRUST\OneDrive\Desktop\code\Runner2\ui files\Add Category.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_add_category(object):
    def setupUi(self, add_category):
        add_category.setObjectName("add_category")
        add_category.setEnabled(True)
        add_category.resize(552, 383)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(add_category.sizePolicy().hasHeightForWidth())
        add_category.setSizePolicy(sizePolicy)
        add_category.setMaximumSize(QtCore.QSize(16777215, 423))
        add_category.setFocusPolicy(QtCore.Qt.ClickFocus)
        add_category.setStyleSheet("#add_category {\n"
"    background-color: #007EA6;\n"
"\n"
"}\n"
"\n"
"QCheckBox {\n"
"    font-size: 16px;\n"
"}\n"
"\n"
"QPushButton {\n"
"    color: white;\n"
"    border: 2px solid white;\n"
"    background-color: transparent;\n"
"    padding: 5px;\n"
"    border-radius: 5px;\n"
"    font-size: 16px;\n"
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(add_category)
        self.verticalLayout.setObjectName("verticalLayout")
        self.hbox_name = QtWidgets.QHBoxLayout()
        self.hbox_name.setObjectName("hbox_name")
        self.lbl_name = QtWidgets.QLabel(add_category)
        self.lbl_name.setStyleSheet("color: white;\n"
"font-size: 16px;")
        self.lbl_name.setObjectName("lbl_name")
        self.hbox_name.addWidget(self.lbl_name)
        self.add_category_name_input = QtWidgets.QLineEdit(add_category)
        self.add_category_name_input.setStyleSheet("font-size: 16px;\n"
"border-radius: 10px;\n"
"padding: 10px;")
        self.add_category_name_input.setObjectName("add_category_name_input")
        self.hbox_name.addWidget(self.add_category_name_input)
        self.verticalLayout.addLayout(self.hbox_name)
        self.hbox_add_buttons_container = QtWidgets.QHBoxLayout()
        self.hbox_add_buttons_container.setObjectName("hbox_add_buttons_container")
        self.lbl_add_file = QtWidgets.QPushButton(add_category)
        self.lbl_add_file.setObjectName("lbl_add_file")
        self.hbox_add_buttons_container.addWidget(self.lbl_add_file)
        self.lbl_add_url = QtWidgets.QPushButton(add_category)
        self.lbl_add_url.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lbl_add_url.setObjectName("lbl_add_url")
        self.hbox_add_buttons_container.addWidget(self.lbl_add_url)
        self.verticalLayout.addLayout(self.hbox_add_buttons_container)
        self.vbox_container = QtWidgets.QVBoxLayout()
        self.vbox_container.setObjectName("vbox_container")
        self.verticalLayout.addLayout(self.vbox_container)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.hbox_buttons_container = QtWidgets.QHBoxLayout()
        self.hbox_buttons_container.setObjectName("hbox_buttons_container")
        self.lbl_discard = QtWidgets.QPushButton(add_category)
        self.lbl_discard.setObjectName("lbl_discard")
        self.hbox_buttons_container.addWidget(self.lbl_discard)
        self.lbl_save = QtWidgets.QPushButton(add_category)
        self.lbl_save.setObjectName("lbl_save")
        self.hbox_buttons_container.addWidget(self.lbl_save)
        self.verticalLayout.addLayout(self.hbox_buttons_container)

        self.retranslateUi(add_category)
        QtCore.QMetaObject.connectSlotsByName(add_category)

    def retranslateUi(self, add_category):
        _translate = QtCore.QCoreApplication.translate
        add_category.setWindowTitle(_translate("add_category", "Add Category"))
        self.lbl_name.setText(_translate("add_category", "Name"))
        self.lbl_add_file.setText(_translate("add_category", "Add File"))
        self.lbl_add_url.setText(_translate("add_category", "Add URL"))
        self.lbl_discard.setText(_translate("add_category", "Discard"))
        self.lbl_save.setText(_translate("add_category", "Save"))
