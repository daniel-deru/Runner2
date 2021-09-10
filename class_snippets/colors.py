import re
styles = {
    "tabWidget": "#tabWidget {background-color: stylesheet;}QTabBar::tab {background-color: white;color: black;}QTabBar::tab:selected {background-color: stylesheet;color: white;}QTabWidget::pane {background-color: stylesheet;}QPushButton {color: white;border: 2px solid white;}QPushButton:pressed {color: stylesheet;background-color: white;border-color: stylesheet;}",
    "apps_tab": "#apps_tab {background-color: stylesheet;}",
    "btn_run" : "#btn_run {background-color: white;color: stylesheet;border: 2px solid white;min-width: 120px;}#btn_run:pressed {background-color: transparent;color: white;}",
    "main_add_category_btn": "QPushButton {color: white;background-color: transparent;}QPushButton:pressed{color: stylesheet;background-color: white;border-color: stylesheet;}",
    "apps_scroll_area": "background-color: stylesheet;",
    "notes_tab": "#notes_tab {background-color: stylesheet;}",
    "btn_notes_delete": "QPushButton {color: white;border: 2px solid white;background-color: transparent;}QPushButton:pressed {color: stylesheet;background-color: white;border-color: stylesheet;}"
}




def setColors(widget, color, stylesheet):
    result = re.sub("stylesheet", color, styles[stylesheet])
    widget.setStyleSheet(result)

