# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'delete_notes.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DeleteWindow(object):
    def setupUi(self, DeleteWindow):
        DeleteWindow.setObjectName("DeleteWindow")
        DeleteWindow.resize(400, 300)
        DeleteWindow.setStyleSheet("")
        self.verticalLayout = QtWidgets.QVBoxLayout(DeleteWindow)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrl_area_delete_notes = QtWidgets.QScrollArea(DeleteWindow)
        self.scrl_area_delete_notes.setStyleSheet("")
        self.scrl_area_delete_notes.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrl_area_delete_notes.setWidgetResizable(True)
        self.scrl_area_delete_notes.setObjectName("scrl_area_delete_notes")
        self.scrl_area_widget = QtWidgets.QWidget()
        self.scrl_area_widget.setGeometry(QtCore.QRect(0, 0, 400, 247))
        self.scrl_area_widget.setObjectName("scrl_area_widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrl_area_widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.scrl_area_delete_notes.setWidget(self.scrl_area_widget)
        self.verticalLayout.addWidget(self.scrl_area_delete_notes)
        self.hbox_btn_container = QtWidgets.QHBoxLayout()
        self.hbox_btn_container.setContentsMargins(25, 15, 25, 15)
        self.hbox_btn_container.setSpacing(25)
        self.hbox_btn_container.setObjectName("hbox_btn_container")
        self.btn_discard = QtWidgets.QPushButton(DeleteWindow)
        self.btn_discard.setObjectName("btn_discard")
        self.hbox_btn_container.addWidget(self.btn_discard)
        self.btn_delete = QtWidgets.QPushButton(DeleteWindow)
        self.btn_delete.setObjectName("btn_delete")
        self.hbox_btn_container.addWidget(self.btn_delete)
        self.verticalLayout.addLayout(self.hbox_btn_container)

        self.retranslateUi(DeleteWindow)
        QtCore.QMetaObject.connectSlotsByName(DeleteWindow)

    def retranslateUi(self, DeleteWindow):
        _translate = QtCore.QCoreApplication.translate
        DeleteWindow.setWindowTitle(_translate("DeleteWindow", "Delete Notes"))
        self.btn_discard.setText(_translate("DeleteWindow", "Exit"))
        self.btn_delete.setText(_translate("DeleteWindow", "Delete"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DeleteWindow = QtWidgets.QDialog()
    ui = Ui_DeleteWindow()
    ui.setupUi(DeleteWindow)
    DeleteWindow.show()
    sys.exit(app.exec_())
