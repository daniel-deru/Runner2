from class_snippets.MessageBox import Message
import os
import sys
import json
import re
import subprocess

# get the database path in order to use the DB class
db_path = os.path.abspath(os.getcwd())
sys.path.insert(0, db_path)

from inspect import currentframe, getframeinfo

# This module is to access the font file
from fontTools.ttLib import TTFont

# PyQt5 imports
from PyQt5.QtWidgets import QApplication, QFileDialog, QWidget, QSpacerItem, QSizePolicy, QColorDialog
from PyQt5.QtGui import QFont, QFontDatabase, QIcon

# Import the main window UI
from uipy.mainUI import Ui_Runner

# Import Files Windows
from primary_windows.Add_category import CategoryWindow
from primary_windows.Notes import NotesWindow

# Import notes windows
from secondary_windows.Delete import DeleteWindow
from secondary_windows.SelectWindow import SelectWindow

# Import the database class
from database.db import DB

# Import functions that make the notes and file containers (sub widgets)
from class_snippets.NoteBox import make_note_container
from class_snippets.FileBox import make_file_container
from class_snippets.export import export_data
from class_snippets.importcsv import import_data

combo_box = """
    QComboBox::drop-down {
        border: 0px;
    }
    QComboBox::down-arrow {
        image: url(./images/dropdown.png);
        width: 15px;
        height: 15px;
        border: 0px;
        background-repeat: no-repeat;
        background-position: center center;
        border-image: none;
        padding-right: 5px;
    }
"""

radio_stylesheet = """
    QRadioButton::indicator:unchecked {
        image: url(images/radio-off.png);
        width: 25px;
        height: 25px;
    }

    QRadioButton::indicator:checked {
        image: url(images/radio-on.png);
        width: 25px;
        height: 25px;
    }
"""


class Main(QWidget, Ui_Runner):
    def __init__(self):
        super(Main, self).__init__()  
        self.setupUi(self)
        self.add_tab_icons()
        self.tabWidget.setCurrentIndex(0)
        self.setWindowTitle("WorkMate")
        self.setWindowIcon(QIcon("images/WorkMate.png"))

        dropdown = self.cmb_font.styleSheet()
        self.cmb_font.setStyleSheet(dropdown+combo_box)

        for i in range(self.hbox_order.count()):
            self.hbox_order.itemAt(i).widget().setStyleSheet(radio_stylesheet)
        

        db = DB()
        db.first_state()

        # show the notes and files when the window loads
        self.show_notes()
        self.show_files()
        self.show_fonts()
        self.load_settings()
        
        
        # File connections
        self.main_add_category_btn.clicked.connect(self.add_category_clicked)
        self.apps_btn_delete.clicked.connect(self.delete_category_clicked)
        self.apps_btn_edit.clicked.connect(self.edit_category_clicked)
        self.btn_run.clicked.connect(self.run_clicked)

        # Note connections
        self.main_add_notes_btn.clicked.connect(self.add_notes_clicked)
        self.btn_notes_delete.clicked.connect(self.notes_delete_clicked)
        self.btn_notes_edit.clicked.connect(self.notes_edit_clicked)

        # Settings connections
        self.btn_save.clicked.connect(self.save_settings)
        self.cmb_font.activated.connect(self.select_font)
        self.btn_choose_color.clicked.connect(self.select_color)
        self.btn_reset.clicked.connect(self.reset_clicked)
        self.btn_export_apps.clicked.connect(lambda: self.export("categories"))
        self.btn_export_notes.clicked.connect(lambda: self.export("notes"))
        self.btn_import_apps.clicked.connect(lambda: self.import_("files"))
        self.btn_import_notes.clicked.connect(lambda: self.import_("notes"))


        self.tabWidget.currentChanged.connect(self.add_tab_icons)
        

    # open category window to add categories
    def add_category_clicked(self):
        make_category = CategoryWindow()
        make_category.category_signal.connect(self.update)
        make_category.exec_()
    
    
    # Open select window to select which window to edit
    def edit_category_clicked(self):
        apps = DB().read("categories")
        if len(apps) > 0:
            edit_category = SelectWindow("categories")
            edit_category.edit_signal.connect(self.update)
            edit_category.exec_()
        else:
            Message("There are no apps to edit. Please insert apps if you want to use this function.", "No Apps")
    
    # Open the delete window to delete categories
    def delete_category_clicked(self):
        apps = DB().read("categories")
        if len(apps) > 0:
            delete_category = DeleteWindow("categories")
            delete_category.delete_signal.connect(self.show_files)
            delete_category.exec_()
        else:
            Message("There are no apps to delete. Please insert apps if you want to use this function.", "No Apps")

    # run the selected categories and files
    def run_clicked(self):

        # get the number of categories
        category_container = self.verticalLayout_3
        item_count = len(category_container)

        run_list = set()

        for i in range(item_count):
            apps = DB().read("categories")
            if len(apps) > 0:
                # get category widget
                category = category_container.itemAt(i).widget()
                if category:
                    # get the category items
                    category_widget_item = category.children()
                    # category name
                    title = category_widget_item[2].text()
                    # category is active checkbox
                    checkbox = category_widget_item[3]
                    # files container
                    frame = category_widget_item[1]

                    # check if the category is active
                    if checkbox.isChecked():
                        files = frame.children()[1:]
                        # get the checked files
                        filtered_files = list(filter(lambda x: x.isChecked(), files))

                        for file in filtered_files:
                            db = DB()
                            paths = db.read("files", "name", file.text())

                            run_list.add(paths[0][1])
            
                for file in run_list:
                    os.startfile(file)
            else:
                Message("There are no apps to run. Please insert apps if you want to use this function", "No apps")
                        

    # open the notes window to add notes
    def add_notes_clicked(self):
        make_note = NotesWindow()
        make_note.note_signal.connect(self.update)
        make_note.exec_()

    # open the delete window to delete notes
    def notes_delete_clicked(self):
        notes = DB().read("notes")
        if len(notes) > 0:
            delete_notes = DeleteWindow("notes")
            delete_notes.delete_signal.connect(self.update)
            delete_notes.exec_()
        else:
            Message("There are no notes to delete. Please insert notes if you want to use this function", "No notes")

    # open the select window to select which note to edit
    def notes_edit_clicked(self):
        notes = DB().read("notes")
        if len(notes) > 0:
            select_notes = SelectWindow("notes")
            select_notes.edit_signal.connect(self.update)
            select_notes.exec_()
        else:
            Message("There are no notes to edit. Please insert notes if you want to use this function", "No notes")
    
    # Helper methods
    def update(self):
        self.show_files()
        self.show_notes()
    
    # function to paint the notes in the window
    def show_notes(self):

        self.clear_window(self.notes_scroll_layout)

        # get notes from the database
        db = DB()
        notes = db.read("notes")
        # add notes to the window
        for note in notes:
            n = make_note_container(note)
            self.notes_scroll_layout.addWidget(n)
        
        # add spacer to push widgets to the top
        spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.notes_scroll_layout.addItem(spacer)

    def show_files(self):
        # clear the window so it can be updated
        self.clear_window(self.verticalLayout_3)

        db = DB()
        categories = db.read("categories")

        # make the file container
        for category in categories:
            f = make_file_container(category, self.update_category)
            self.verticalLayout_3.addWidget(f)

        # add spacer at the bottom of the vboxlayout
        spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacer)
    
    # clears the window so it can be repainted
    @staticmethod
    def clear_window(container):
        # This is to remove the previous widgets that were painted so the widgets don't get added twice
        prevItems = container.count()
        # check if there are widgets
        if prevItems > 0:
            for i in range(container.count()):
                item = container.itemAt(i)
                if item.widget():
                    item.widget().deleteLater()
                elif item.spacerItem():
                    container.removeItem(item.spacerItem())
    
    # update the category active checkbox
    def update_category(self, name, state):
        value = 1 if state == True else 0
        db = DB()
        db.update_category_state(name, value)
    
    # add the tabicons and change them depending on which window is active
    def add_tab_icons(self): 
        self.tabWidget.setTabIcon(0, QIcon("images/AppsIconBlack.png"))
        self.tabWidget.setTabIcon(1, QIcon("images/NotesIconBlack.png"))
        self.tabWidget.setTabIcon(2, QIcon("images/SettingIconBlack.png"))
        active_tab_index = self.tabWidget.currentIndex()
        if active_tab_index == 0:
            self.tabWidget.setTabIcon(active_tab_index, QIcon("images/AppsIconWhite.png"))
        elif active_tab_index == 1:
            self.tabWidget.setTabIcon(active_tab_index, QIcon("images/NotesIconWhite.png"))
        else:
            self.tabWidget.setTabIcon(active_tab_index, QIcon("images/SettingsIconWhite.png"))
    
    # open color dialog and update the color example
    def select_color(self):
        color = QColorDialog().getColor().name()
        self.lbl_hex_color.setText(color)
        self.lbl_hex_color.setStyleSheet(f"color: {color};")

    def show_fonts(self):
        path = "fonts/"
        # get the fonts from the fonts dir
        fonts = list(os.scandir(path))

        # variables to keep track of the font names (to use in QFont class) and names to display to the user
        self.display_names = []
        self.font_names = []

        # loop over the fonts dir and add them to the font data base
        # add font names and display names to lists
        for font in fonts:
            QFontDatabase.addApplicationFont(f"{path}{font.name}")
            font_file = TTFont(f"{path}{font.name}")
            # get the name of the font to set the font name
            font_name = font_file["name"].getName(1, 3, 1).toUnicode()
            self.font_names.append(font_name)
        # add the display names to the combobox
        for name in self.font_names:
            self.cmb_font.addItem(name)

       
    # get font and update the example text
    def select_font(self):
        font_index = self.cmb_font.currentIndex()
        font = QFont(self.font_names[font_index], 18)
        self.lbl_font_example.setText("This Is Your Font")
        self.lbl_font_example.setFont(font)
    
    # save the current settings
    def save_settings(self):
        db = DB()
        old_color = db.read("settings")[0][1]
        new_color = self.lbl_hex_color.text()
        font = self.cmb_font.currentText().strip()
        note_order = ""
        for i in range(self.hbox_order.count()):
            if self.hbox_order.itemAt(i).widget().isChecked():
                note_order = self.hbox_order.itemAt(i).widget().text().lower()
        
        settings = (old_color, new_color, font, note_order)
        db2 = DB()
        db2.update_settings(settings)
        self.load_settings()
        self.update()


    # reset the settings
    def reset_clicked(self):
        color = self.lbl_hex_color.text()
        db = DB()
        db.first_state(True)
        self.update()
        self.load_settings(color)
        

    def load_settings(self, reset_color=False):
        db = DB()
        settings = db.read("settings")

        # set your current color
        self.load_color(settings[0][0], settings[0][1], reset_color)
        self.lbl_hex_color.setText(settings[0][1])
        self.lbl_hex_color.setStyleSheet("color: white;")

        #set the current font
        self.set_font(settings[0][2])
        font_index = self.cmb_font.findText(settings[0][2])
        self.cmb_font.setCurrentIndex(font_index)
        current_font = QFont(self.font_names[font_index], 18)
        self.lbl_font_example.setFont(current_font)
        

        # set current note order
        for i in range(len(self.hbox_order)):
            if self.hbox_order.itemAt(i).widget().text().lower() == settings[0][3]:
                self.hbox_order.itemAt(i).widget().setChecked(True)
        
       
    # set the color of the window
    def load_color(self, old_color, new_color, reset_color):
        #list pf widgets to apply the color to
        widgets = [self.tabWidget, self.apps_tab, self.notes_tab, self.settings_tab, self.notes_scroll_area_widget]
        # loop over the list and get the stylesheet for every widget change the stylesheet and update the widget
        for widget in widgets:
            stylesheet = widget.styleSheet()
            if reset_color:
                stylesheet_updated = re.sub(f"{reset_color}|#007EA6", new_color, stylesheet)
            elif not reset_color:
                stylesheet_updated = re.sub(f"{old_color}|#007EA6", new_color, stylesheet)
            widget.setStyleSheet(stylesheet_updated)

    # set the font of the window
    def set_font(self, font):
        # get the font filename
        font_index = self.font_names.index(font)
        # get the fontname to use with QFont
        if font_index:
            fontname = self.font_names[font_index]
            # create font
            font = QFont(fontname, 18)
            # list of everything the font needs to be applied to
            labels = [
                self.tabWidget,
                self.apps_btn_delete,
                self.apps_btn_edit,
                self.main_add_category_btn,
                self.btn_run,
                self.btn_notes_delete,
                self.btn_notes_edit,
                self.main_add_notes_btn,
                self.lbl_main_color,
                self.lbl_hex_color,
                self.lbl_font,
                self.btn_choose_color,
                self.btn_reset,
                self.btn_save,
                self.lbl_order,
                self.rbtn_date,
                self.rbtn_priority,
                self.rbtn_title,
                self.cmb_font
            ]
            # loop over the labels and set the font for each
            for label in labels:
                label.setFont(font)
            
    def export(self, table):
        return export_data(table)

    def import_(self, table):
        file = QFileDialog.getOpenFileName(self, "Open a file", "", "CSV Files (*.csv*)")[0]
        import_data(table, file)
        self.update()

        

        
       
    

            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = Main()
    main.setWindowTitle("WorkMate")
    main.show()
    sys.exit(app.exec_())
