# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Edit Notes.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_edit_notes(object):
    def setupUi(self, edit_notes):
        edit_notes.setObjectName("edit_notes")
        edit_notes.resize(398, 323)
        edit_notes.setStyleSheet("#edit_notes {\n"
"    background-color: #007EA6;\n"
"\n"
"}\n"
"\n"
"QLabel {\n"
"    color: white;\n"
"    font-size: 20px;\n"
"}\n"
"\n"
"QRadioButton {\n"
"    color: white;\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton {\n"
"    color: white;\n"
"    border: 2px solid white;\n"
"    border-radius: 10px;\n"
"    background-color: transparent;\n"
"    padding: 5px;\n"
"    font-size: 16px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    color: #007EA6;\n"
"    background-color: white;\n"
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(edit_notes)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lbl_note_title = QtWidgets.QLabel(edit_notes)
        self.lbl_note_title.setObjectName("lbl_note_title")
        self.verticalLayout.addWidget(self.lbl_note_title)
        self.ldt_note_title = QtWidgets.QLineEdit(edit_notes)
        self.ldt_note_title.setStyleSheet("font-size: 16px;\n"
"border-radius: 10px;\n"
"padding:5px;")
        self.ldt_note_title.setObjectName("ldt_note_title")
        self.verticalLayout.addWidget(self.ldt_note_title)
        self.lbl_note_body = QtWidgets.QLabel(edit_notes)
        self.lbl_note_body.setObjectName("lbl_note_body")
        self.verticalLayout.addWidget(self.lbl_note_body)
        self.txtedt_note_body = QtWidgets.QTextEdit(edit_notes)
        self.txtedt_note_body.setStyleSheet("font-size: 16px;\n"
"border-radius: 10px;\n"
"padding:5px;\n"
"background-color: palette(base);")
        self.txtedt_note_body.setObjectName("txtedt_note_body")
        self.verticalLayout.addWidget(self.txtedt_note_body)
        self.lbl_importance = QtWidgets.QLabel(edit_notes)
        self.lbl_importance.setStyleSheet("font-size: 18px;")
        self.lbl_importance.setObjectName("lbl_importance")
        self.verticalLayout.addWidget(self.lbl_importance)
        self.hbox_importance = QtWidgets.QHBoxLayout()
        self.hbox_importance.setObjectName("hbox_importance")
        self.rbtn_low = QtWidgets.QRadioButton(edit_notes)
        self.rbtn_low.setStyleSheet("color: #90FA00;")
        self.rbtn_low.setObjectName("rbtn_low")
        self.hbox_importance.addWidget(self.rbtn_low)
        self.rbtn_medium = QtWidgets.QRadioButton(edit_notes)
        self.rbtn_medium.setStyleSheet("color: #FAE700;")
        self.rbtn_medium.setObjectName("rbtn_medium")
        self.hbox_importance.addWidget(self.rbtn_medium)
        self.rbtn_high = QtWidgets.QRadioButton(edit_notes)
        self.rbtn_high.setStyleSheet("color: #D60025;")
        self.rbtn_high.setObjectName("rbtn_high")
        self.hbox_importance.addWidget(self.rbtn_high)
        self.verticalLayout.addLayout(self.hbox_importance)
        self.hbox_notes_buttons = QtWidgets.QHBoxLayout()
        self.hbox_notes_buttons.setObjectName("hbox_notes_buttons")
        self.btn_discard = QtWidgets.QPushButton(edit_notes)
        self.btn_discard.setStyleSheet("QpushButton {\n"
"    color: white;\n"
"    border: 2px solid white;\n"
"    border-radius: 10px;\n"
"    background-color: transparent;\n"
"}")
        self.btn_discard.setObjectName("btn_discard")
        self.hbox_notes_buttons.addWidget(self.btn_discard)
        self.btn_save = QtWidgets.QPushButton(edit_notes)
        self.btn_save.setObjectName("btn_save")
        self.hbox_notes_buttons.addWidget(self.btn_save)
        self.verticalLayout.addLayout(self.hbox_notes_buttons)

        self.retranslateUi(edit_notes)
        QtCore.QMetaObject.connectSlotsByName(edit_notes)

    def retranslateUi(self, edit_notes):
        _translate = QtCore.QCoreApplication.translate
        edit_notes.setWindowTitle(_translate("edit_notes", "Add / Edit Notes"))
        self.lbl_note_title.setText(_translate("edit_notes", "Title"))
        self.lbl_note_body.setText(_translate("edit_notes", "Note"))
        self.lbl_importance.setText(_translate("edit_notes", "Importance"))
        self.rbtn_low.setText(_translate("edit_notes", "Low"))
        self.rbtn_medium.setText(_translate("edit_notes", "Medium"))
        self.rbtn_high.setText(_translate("edit_notes", "High"))
        self.btn_discard.setText(_translate("edit_notes", "Exit"))
        self.btn_save.setText(_translate("edit_notes", "Save"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    edit_notes = QtWidgets.QDialog()
    ui = Ui_edit_notes()
    ui.setupUi(edit_notes)
    edit_notes.show()
    sys.exit(app.exec_())
