# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'select_notes.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SelectWindow(object):
    def setupUi(self, SelectWindow):
        SelectWindow.setObjectName("SelectWindow")
        SelectWindow.resize(400, 275)
        SelectWindow.setStyleSheet("QDialog {\n"
"    background-color: #007ea6;\n"
"}\n"
"\n"
" QPushButton {\n"
"                    font-size: 16px;\n"
"                    color: white;\n"
"                    border: 2px solid white;\n"
"                    border-radius: 10px;\n"
"                    padding: 5px;\n"
"                    background-color: transparent;\n"
"                }\n"
"\n"
"QPushButton:pressed {\n"
"            color: #007ea6;\n"
"            background-color: white;\n"
" }\n"
"\n"
"QRadioButton {\n"
"    color: white;\n"
"    font-size: 16px;\n"
"}\n"
"\n"
"QWidget {\n"
"    background-color: #007ea6;\n"
"}\n"
"")
        self.SelectNoteLayout = QtWidgets.QVBoxLayout(SelectWindow)
        self.SelectNoteLayout.setContentsMargins(0, 0, 0, 0)
        self.SelectNoteLayout.setSpacing(0)
        self.SelectNoteLayout.setObjectName("SelectNoteLayout")
        self.scrl_area_select_notes = QtWidgets.QScrollArea(SelectWindow)
        self.scrl_area_select_notes.setStyleSheet("")
        self.scrl_area_select_notes.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrl_area_select_notes.setWidgetResizable(True)
        self.scrl_area_select_notes.setObjectName("scrl_area_select_notes")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 400, 212))
        self.scrollAreaWidgetContents.setStyleSheet("")
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrl_area_select_notes.setWidget(self.scrollAreaWidgetContents)
        self.SelectNoteLayout.addWidget(self.scrl_area_select_notes)
        self.hbox_btn_container = QtWidgets.QHBoxLayout()
        self.hbox_btn_container.setContentsMargins(15, 15, 15, 15)
        self.hbox_btn_container.setSpacing(20)
        self.hbox_btn_container.setObjectName("hbox_btn_container")
        self.btn_discard = QtWidgets.QPushButton(SelectWindow)
        self.btn_discard.setObjectName("btn_discard")
        self.hbox_btn_container.addWidget(self.btn_discard)
        self.btn_edit = QtWidgets.QPushButton(SelectWindow)
        self.btn_edit.setObjectName("btn_edit")
        self.hbox_btn_container.addWidget(self.btn_edit)
        self.SelectNoteLayout.addLayout(self.hbox_btn_container)

        self.retranslateUi(SelectWindow)
        QtCore.QMetaObject.connectSlotsByName(SelectWindow)

    def retranslateUi(self, SelectWindow):
        _translate = QtCore.QCoreApplication.translate
        SelectWindow.setWindowTitle(_translate("SelectWindow", "Select Notes"))
        self.btn_discard.setText(_translate("SelectWindow", "Exit"))
        self.btn_edit.setText(_translate("SelectWindow", "Edit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SelectWindow = QtWidgets.QDialog()
    ui = Ui_SelectWindow()
    ui.setupUi(SelectWindow)
    SelectWindow.show()
    sys.exit(app.exec_())
