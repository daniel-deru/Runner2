import re
styles = {}
styles["Runner"] = """#Runner {
	background-color: white;

}"""

styles["tabWidget"] = """#tabWidget {
	background-color: stylesheet;
}

QTabBar::tab {
	background-color: white;
	font-size: 16px;
	height: 30px;
	width: 120px;
	color: black;
}

QTabBar::tab:selected {
	background-color: stylesheet;
	color: white;
}

 QTabWidget::pane {
	background-color: #007EA6;
}

QPushButton {
	color: white;
	border: 2px solid white;
	background-color: transparent;
	padding: 5px;
	font-size: 16px;
	border-radius: 10px;
}

QPushButton:pressed {
	color: #007EA6;
	background-color: white;
	border-color: #007EA6;
}
"""



def setColors(widget, color, stylesheet):
    result = re.sub("stylesheet", color, styles[stylesheet])
    widget.setStyleSheet(result)

