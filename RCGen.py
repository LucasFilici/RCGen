"""
RCGen is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

RCGen is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with RCGen. If not, see <https://www.gnu.org/licenses/>. 
"""
import sys, os
import random
from PyQt5.QtWidgets import QMainWindow, QMenuBar, QDialog, QAction, QApplication, QComboBox, QLineEdit, QPushButton, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QScrollArea
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QIcon, QFont, QDesktopServices, QFontDatabase
from PyQt5 import QtGui

basedir = os.path.dirname(__file__)

try:
    from ctypes import windll  # Only exists on Windows.
    myappid = 'tk.LucasFilici.RCGen.0.02'
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
except ImportError:
    pass

font_preference = "Arial"

gender1 = {'male': 'his', 'female': 'her', 'gender': 'perse'}
gender2 = {'male': 'he', 'female': 'she', 'gender': 'perse'}
gender3 = {'male': 'He', 'female': 'She', 'gender': 'Perse'}
gender4 = {'male': 'himself', 'female': 'herself', 'gender': 'perself'}
gender5 = {'male': 'him', 'female': 'her', 'gender': 'perse'}

positive_feedback_dict = {
    "P&T 1: enter and exit": "",
    "P&T 1: readiness for submersion": "",
    "P&T 1: front floats": "",
    "P&T 1: back floats": "",
    "P&T 1: arms: splashing, reaching, paddling": "",
    "P&T 1: legs: tickling, splashing, kicking | front": "",
    "P&T 1: legs: tickling, splashing, kicking | back": "",
    "P&T 2: entry from sitting": "",
    "P&T 2: exit": "",
    "P&T 2: bubbles": "",
    "P&T 2: face wet and in water": "",
    "P&T 2: object recovery": "",
    "P&T 2: entry from sitting w/ PFD": "",
    "P&T 2: front floats": "",
    "P&T 2: back floats": "",
    "P&T 2: kicking on front": "",
    "P&T 2: kicking on back": "",
    "P&T 2: surface passes": "",
    "P&T 3: jumps": "",
    "P&T 3: entry and submerge": "",
    "P&T 3: hold breath": "",
    "P&T 3: object recovery": "",
    "P&T 3: swim to survive (jump+return to edge)": "",
    "P&T 3: swim to survive (jump+float)": "",
    "P&T 3: front starfish floats": "",
    "P&T 3: back starfish floats": "",
    "P&T 3: front pencil floats": "",
    "P&T 3: back pencil floats": "",
    "P&T 3: kicking on front": "",
    "P&T 3: kicking on back": "",
    "P&T 3: Underwater passes": "",
    "PS 1: enter and exit": "",
    "PS 1: jumps": "",
    "PS 1: face wet": "",
    "PS 1: bubbles": "",
    "PS 1: front floats": "",
    "PS 1: back floats": "",
    "PS 1: front+back floats": "",
    "PS 1: movement": "",
    "PS 1: front glides": "",
    "PS 1: back glides": "",
    "PS 2: enter and exit": "",
    "PS 2: jumps": "",
    "PS 2: submerge": "",
    "PS 2: submerge and exhale": "",
    "PS 2: front floats": "",
    "PS 2: back floats": "",
    "PS 2: front+back floats": "",
    "PS 2: lateral rolls": "",
    "PS 2: front glides": "",
    "PS 2: back glides": "",
    "PS 2: flutter kick": "",
    "PS 3: jumps": "",
    "PS 3: sideways entries": "",
    "PS 3: submerge and hold breath": "",
    "PS 3: submerge and exhale": "",
    "PS 3: object recovery": "",
    "PS 3: swim to survive": "",
    "PS 3: front floats": "",
    "PS 3: back floats": "",
    "PS 3: lateral rolls": "",
    "PS 3: front glides": "",
    "PS 3: back glides": "",
    "PS 3: flutter kick on front": "",
    "PS 3: flutter kick on back": "",
    "PS 4: jumps": "",
    "PS 4: sideways entries": "",
    "PS 4: treading": "",
    "PS 4: open eyes underwater": "",
    "PS 4: object recovery": "",
    "PS 4: swim to survive 6.(PFD+jump)": "",
    "PS 4: swim to survive 7.(no PFD or jump)": "",
    "PS 4: side glides": "",
    "PS 4: flutter kick on front": "",
    "PS 4: flutter kick on back": "",
    "PS 4: flutter kick on side": "",
    "PS 4: front crawl": "",
    "PS 5: forward rolls": "",
    "PS 5: treading": "",
    "PS 5: submerge and hold breath": "",
    "PS 5: object recovery": "",
    "PS 5: swim to survive": "",
    "PS 5: whip kick in vertical position": "",
    "PS 5: front crawl": "",
    "PS 5: back crawl": "",
    "PS 5: interval training": "",
}
constructive_feedback_dict = {
    "P&T 1: readiness for submersion": "",
    "P&T 1: front floats": "",
    "P&T 1: back floats": "",
    "P&T 1: legs: tickling, splashing, kicking | front": "",
    "P&T 1: legs: tickling, splashing, kicking | back": "",
    "P&T 2: bubbles": "",
    "P&T 2: face wet and in water": "",
    "P&T 2: object recovery": "",
    "P&T 2: kicking on front | position": "",
    "P&T 2: kicking on front | face in water": "",
    "P&T 2: kicking on back | position": "",
    "P&T 2: kicking on back | ears in water": "",
    "P&T 3: entry and submerge/hold breath/etc. | scared of submerging": "",
    "P&T 3: swim to survive (jump+float) | scared of jumping": "",
    "P&T 3: swim to survive (jump+float) | scared of floating": "",
    "P&T 3: front starfish floats": "",
    "P&T 3: back starfish floats": "",
    "P&T 3: front pencil floats": "",
    "P&T 3: back pencil floats": "",
    "P&T 3: kicking on front | position": "",
    "P&T 3: kicking on front | face in water": "",
    "P&T 3: kicking on back | position": "",
    "P&T 3: kicking on back | ears in water": "",
    "PS 1: face wet": "",
    "PS 1: bubbles": "",
    "PS 1: front floats": "",
    "PS 1: back floats": "",
    "PS 1: movement": "",
    "PS 1: front glides": "",
    "PS 1: back glides": "",
    "PS 2: submerge": "",
    "PS 2: submerge and exhale": "",
    "PS 2: front floats": "",
    "PS 2: back floats": "",
    "PS 2: lateral rolls": "",
    "PS 2: front glides": "",
    "PS 2: back glides": "",
    "PS 2: flutter kick": "",
    "PS 3: submerge and hold breath": "",
    "PS 3: submerge and exhale": "",
    "PS 3: object recovery": "",
    "PS 3: swim to survive | lateral rolls": "",
    "PS 3: swim to survive | swim 3m": "",
    "PS 3: front floats": "",
    "PS 3: back floats": "",
    "PS 3: lateral rolls": "",
    "PS 3: front glides": "",
    "PS 3: back glides": "",
    "PS 3: flutter kick on front": "",
    "PS 3: flutter kick on back": "",
    "PS 4: treading": "",
    "PS 4: object recovery": "",
    "PS 4: swim to survive 6.(PFD+jump) | treading": "",
    "PS 4: swim to survive 6.(PFD+jump) | kick 5m": "",
    "PS 4: swim to survive 7.(no PFD or jump) | lateral roll": "",
    "PS 4: swim to survive 7.(no PFD or jump) | swim 5m": "",
    "PS 4: side glides": "",
    "PS 4: flutter kick on front": "",
    "PS 4: flutter kick on back": "",
    "PS 4: flutter kick on side": "",
    "PS 4: front crawl": "",
    "PS 5: treading": "",
    "PS 5: swim to survive | treading": "",
    "PS 5: swim to survive | swim/kick 10m": "",
    "PS 5: whip kick": "",
    "PS 5: front crawl": "",
    "PS 5: back crawl": "",
    "PS 5: interval training": "",
}

# Create a new dictionary that maps the full names to the shorthand versions
level_map = {"Parent & Tot 1": "P&T 1", "Parent & Tot 2": "P&T 2", "Parent & Tot 3": "P&T 3", "Preschool 1": "PS 1", "Preschool 2": "PS 2", "Preschool 3": "PS 3", "Preschool 4": "PS 4", "Preschool 5": "PS 5"}

adjectives = ["amazing", "great", "fantastic", "fabulous", "wonderful", "incredible"]
last_adjective = ""
adjectives3 = ["exceptionally well", "remarkably well", "outstandingly well"]
last_adjective3 = ""

def get_adjective1():
    global last_adjective
    adjective = random.choice(adjectives)
    while adjective == last_adjective:
        adjective = random.choice(adjectives)
    last_adjective = adjective
    return f"{adjective}"

def get_adjective2():
    global last_adjective
    adjective = random.choice(adjectives)
    while adjective == last_adjective:
        adjective = random.choice(adjectives)
    last_adjective = adjective
    if adjective[0] in ['a','e','i','o','u']:
        return f"an {adjective}"
    else:
        return f"a {adjective}"

def get_adjective3():
    global last_adjective3
    adjective3 = random.choice(adjectives3)
    while adjective3 == last_adjective3:
        adjective3 = random.choice(adjectives3)
    last_adjective3 = adjective3
    return f"{adjective3}"

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'RCGen'
        self.left = 10
        self.top = 10
        self.width = int(QApplication.desktop().screenGeometry().width() * 0.5)
        self.height = int(QApplication.desktop().screenGeometry().height() * 0.5)
        #self.setWindowIcon(QIcon("./WindowIcon.png"))
        self.initUI()
        self.move(QApplication.desktop().screen().rect().center() - self.rect().center())
        self.web_view = None

    def initUI(self):
        font_db = QFontDatabase()
        if font_db.families().__contains__(font_preference):
            font = QFont(font_preference)
            self.setFont(font)
            font_results = QFont(font_preference)
        else:
            font = QApplication.font()
            font_results = QApplication.font()
        
        font_size = 12
        font.setPointSize(font_size)
        self.setFont(font)

        results_font_size = 15
        font_results.setPointSize(results_font_size)

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowIcon(QtGui.QIcon(os.path.join(basedir, 'WindowIcon.ico')))

        # Create the menu bar
        self.menu_bar = self.menuBar()

        # Create a central widget to hold the layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Create the Help menu and add it to the menu bar
        self.help_menu = self.menu_bar.addMenu("Help")

        # Create the Help and Info actions and add them to the Help menu
        self.help_action = QAction("Tutorial", self)
        self.info_action = QAction("Info", self)
        self.help_menu.addActions([self.help_action, self.info_action])

        # Connect the Help and Info actions to their corresponding functions
        self.help_action.triggered.connect(self.open_help)
        self.info_action.triggered.connect(self.open_info)

        #I don't know why the heck I can't get the placeholder text centered AND visible on focus.
        # Create the line edit and center it
        #self.name_line_edit = QLineEdit(self)
        self.name_line_edit = QLineEdit(central_widget, placeholderText="name")
        self.name_line_edit.setAlignment(Qt.AlignCenter)
        # Set the default text for the line edit
        #self.name_line_edit.setPlaceholderText("name")

        # Create the combo boxes
        self.gender_combo_box = QComboBox(central_widget)
        self.level_combo_box = QComboBox(central_widget)
        self.positive_feedback_combo_box_1 = QComboBox(central_widget)
        self.positive_feedback_combo_box_2 = QComboBox(central_widget)
        self.constructive_feedback_combo_box_1 = QComboBox(central_widget)
        self.constructive_feedback_combo_box_2 = QComboBox(central_widget)
        self.positive_feedback_combo_box_3 = QComboBox(central_widget)
        self.positive_feedback_combo_box_4 = QComboBox(central_widget)

        # Set the options for the combo boxes
        self.gender_combo_box.addItem("gender")
        self.gender_combo_box.addItem("male")
        self.gender_combo_box.addItem("female")

        self.level_combo_box.addItem("level")
        self.level_combo_box.addItem("Parent & Tot 1")
        self.level_combo_box.addItem("Parent & Tot 2")
        self.level_combo_box.addItem("Parent & Tot 3")
        self.level_combo_box.addItem("Preschool 1")
        self.level_combo_box.addItem("Preschool 2")
        self.level_combo_box.addItem("Preschool 3")
        self.level_combo_box.addItem("Preschool 4")
        self.level_combo_box.addItem("Preschool 5")

        self.positive_feedback_combo_box_1.addItem("intro positive feedback")
        self.positive_feedback_combo_box_2.addItem("optional intro positive feedback")
        self.constructive_feedback_combo_box_1.addItem("constructive feedback")
        self.constructive_feedback_combo_box_2.addItem("optional constructive feedback")
        self.positive_feedback_combo_box_3.addItem("outro positive feedback")
        self.positive_feedback_combo_box_4.addItem("optional outro positive feedback")

        # Create the result label
        self.result_label = QLabel(central_widget)
        # Set the font for the result label widget to 15
        self.result_label.setFont(font_results)
        # Set word wrapping and make the alignment of the result label as high as it'll go
        self.result_label.setWordWrap(True)
        self.result_label.setAlignment(Qt.AlignTop)

        # Create a scroll area and set the widgetResizable property to True
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidgetResizable(True)

        # Set the scroll area as the widget for the result label
        self.scroll_area.setWidget(self.result_label)

        # Create the Regenerate Report Card Button
        self.RegenerateRC = QPushButton("Adjectives Reroll", self)

        # Create the horizontal layout to hold the combo boxes
        h_box_0 = QHBoxLayout()
        h_box_0.addStretch()
        h_box_0.addWidget(self.name_line_edit)
        h_box_0.addStretch()

        # Create the horizontal layout to hold the combo boxes
        h_box_1 = QHBoxLayout()
        h_box_1.addWidget(self.gender_combo_box)

        # Create the horizontal layout to hold the combo boxes
        h_box_2 = QHBoxLayout()
        h_box_2.addWidget(self.level_combo_box)

        # Create a new horizontal layout to hold the positive and constructive feedback 1 combo boxes
        h_box_3 = QHBoxLayout()
        h_box_3.addWidget(self.positive_feedback_combo_box_1)
        h_box_3.addWidget(self.positive_feedback_combo_box_2)

        # Create a new horizontal layout to hold the positive and constructive feedback 2 combo boxes
        h_box_4 = QHBoxLayout()
        h_box_4.addWidget(self.constructive_feedback_combo_box_1)
        h_box_4.addWidget(self.constructive_feedback_combo_box_2)

        # Create a new horizontal layout to hold the positive and constructive feedback 2 combo boxes
        h_box_5 = QHBoxLayout()
        h_box_5.addWidget(self.positive_feedback_combo_box_3)
        h_box_5.addWidget(self.positive_feedback_combo_box_4)

        # Create the vertical layout to hold the line edit and horizontal layout
        central_layout = QVBoxLayout(central_widget)
        central_layout.addLayout(h_box_0)
        central_layout.addLayout(h_box_1)
        central_layout.addLayout(h_box_2)
        central_layout.addLayout(h_box_3)
        central_layout.addLayout(h_box_4)
        central_layout.addLayout(h_box_5)

        # Add the scroll area to the vertical layout
        central_layout.addWidget(self.scroll_area)

        central_layout.addWidget(self.RegenerateRC)

        # Connect the "textChanged" signal of the line edit to the updateResult function
        self.name_line_edit.textChanged.connect(self.updateResult)

        # Connect the "currentIndexChanged" signal of the level combo box to the updatePositiveFeedbackComboBox function
        self.level_combo_box.currentIndexChanged.connect(self.updatePositiveFeedbackComboBox)
        # Connect the "currentIndexChanged" signal of the level combo box to the updateConstructiveFeedbackComboBox function
        self.level_combo_box.currentIndexChanged.connect(self.updateConstructiveFeedbackComboBox)

        # Connect the "currentIndexChanged" signals of the combo boxes to the updateResult function
        self.gender_combo_box.currentIndexChanged.connect(self.updateResult)
        self.level_combo_box.currentIndexChanged.connect(self.updateResult)
        self.positive_feedback_combo_box_1.currentIndexChanged.connect(self.updateResult)
        self.positive_feedback_combo_box_2.currentIndexChanged.connect(self.updateResult)
        self.constructive_feedback_combo_box_1.currentIndexChanged.connect(self.updateResult)
        self.constructive_feedback_combo_box_2.currentIndexChanged.connect(self.updateResult)
        self.positive_feedback_combo_box_3.currentIndexChanged.connect(self.updateResult)
        self.positive_feedback_combo_box_4.currentIndexChanged.connect(self.updateResult)

        # Connect RegenerateRC button presses to the updateResult function
        self.RegenerateRC.clicked.connect(self.updateResult)

        #Make the result label highlightable
        self.result_label.setTextInteractionFlags(Qt.TextSelectableByMouse)

    def open_help(self):
        url = QUrl("https://www.youtube.com/watch?v=rpM_gD3d0_0")
        QDesktopServices.openUrl(url)

    def open_info(self):
        # Create a dialog box with information info the program
        info_box = QDialog(self)
        info_box.setWindowTitle("About RCGen")

        # Get the position and size of the main window
        main_window_geometry = self.geometry()

        # Create a QLabel with a hyperlink
        link = "<a href='https://rcgen.tk'>RCGen.tk</a>"
        self.info_label = QLabel("RCGen is FLOSS for generating swimming report cards.<br>" + link + "<br><br>Copyright © 2023 Lucas Filici<br>under GPL-3.0-or-later")
        self.info_label.setOpenExternalLinks(True)
        font_db = QFontDatabase()
        if font_preference in set(font_db.families()):
            label_font = QFont(font_preference)
        else:
            label_font = QFont("default")
        label_font_size = 9
        label_font.setPointSize(label_font_size)
        self.info_label.setAlignment(Qt.AlignCenter)
        self.info_label.setFont(label_font)

        # Add the label to the dialog box
        layout = QVBoxLayout()
        layout.addWidget(self.info_label)
        info_box.setLayout(layout)

        info_box.setWindowFlags(info_box.windowFlags() & ~Qt.WindowContextHelpButtonHint)
        info_box.adjustSize()
        info_box.setFixedWidth(info_box.sizeHint().width())
        info_box.setFixedHeight(info_box.sizeHint().height())

        info_box.exec_()

    def updatePositiveFeedbackComboBox(self, index):
        # Clear the current options in the positive feedback combo box
        self.positive_feedback_combo_box_1.clear()
        self.positive_feedback_combo_box_1.addItem("intro positive feedback")

        self.positive_feedback_combo_box_2.clear()
        self.positive_feedback_combo_box_2.addItem("optional intro positive feedback")

        self.positive_feedback_combo_box_3.clear()
        self.positive_feedback_combo_box_3.addItem("outro positive feedback")

        self.positive_feedback_combo_box_4.clear()
        self.positive_feedback_combo_box_4.addItem("optional outro positive feedback")

        # Get the current text of the level combo box
        level = self.level_combo_box.currentText()

        # Check if level is not equal to "level" or None
        if level != "level" and level is not None:
            # Add the options for the selected level
            for key in positive_feedback_dict.keys():
                if key.startswith(level_map.get(level, "")):
                    self.positive_feedback_combo_box_1.addItem(key)
                    self.positive_feedback_combo_box_2.addItem(key)
                    self.positive_feedback_combo_box_3.addItem(key)
                    self.positive_feedback_combo_box_4.addItem(key)

        # Set the current index of the positive feedback combo box to 0
        self.positive_feedback_combo_box_1.setCurrentIndex(0)
        self.positive_feedback_combo_box_2.setCurrentIndex(0)
        self.positive_feedback_combo_box_3.setCurrentIndex(0)
        self.positive_feedback_combo_box_4.setCurrentIndex(0)

    def updateConstructiveFeedbackComboBox(self, index):
        # Clear the current options in the positive feedback combo box
        self.constructive_feedback_combo_box_1.clear()
        self.constructive_feedback_combo_box_1.addItem("constructive feedback")

        self.constructive_feedback_combo_box_2.clear()
        self.constructive_feedback_combo_box_2.addItem("optional constructive feedback")

        # Get the current text of the level combo box
        level = self.level_combo_box.currentText()

        # Check if level is not equal to "level" or None
        if level != "level" and level is not None:
            # Add the options for the selected level
            for key in constructive_feedback_dict.keys():
                if key.startswith(level_map.get(level, "")):
                    self.constructive_feedback_combo_box_1.addItem(key)
                    self.constructive_feedback_combo_box_2.addItem(key)

        # Set the current index of the positive feedback combo box to 0
        self.constructive_feedback_combo_box_1.setCurrentIndex(0)
        self.constructive_feedback_combo_box_2.setCurrentIndex(0)

    def updateResult(self):
        name = self.name_line_edit.text()
        level = self.level_combo_box.currentText()
        gender = self.gender_combo_box.currentText()

        intros_dict = {
            "intro1": f"{name} did {get_adjective1()} this session!",
            "intro2": f"{name} was a pleasure to teach!",
        }

        conclusions_dict = {
            "conc1": f"I hope that {name} does well in {gender1[gender]} next session!",
            "conc2": f"I hope that {name} has a great time in {gender1[gender]} next session!"
        }

        def getintro():
            return intros_dict[random.choice(list(intros_dict.keys()))]

        def getconclusion():
            return conclusions_dict[random.choice(list(conclusions_dict.keys()))]

        positive_feedback_dict.update({
            "P&T 1: enter and exit": f" did {get_adjective2()} job of safely entering and exiting the water",
            "P&T 1: readiness for submersion": f" did {get_adjective2()} job of allowing {gender1[gender]} face to get wet",
            "P&T 1: front floats": f" was relaxed when {gender2[gender]} performed {gender1[gender]} front floats",
            "P&T 1: back floats": f" was relaxed when {gender2[gender]} performed {gender1[gender]} back floats",
            "P&T 1: arms: splashing, reaching, paddling": f" did {get_adjective2()} job of splashing, reaching, and paddling with {gender1[gender]} arms",
            "P&T 1: legs: tickling, splashing, kicking | front": f" did {get_adjective2()} job of kicking {gender1[gender]} legs with {gender1[gender]} chin in the water",
            "P&T 1: legs: tickling, splashing, kicking | back": f" did {get_adjective2()} job of kicking {gender1[gender]} legs with {gender1[gender]} ears in the water",
            "P&T 2: entry from sitting": f" did {get_adjective2()} job of entering the water from a sitting position in a controlled manner",
            "P&T 2: exit": f" did {get_adjective2()} job of safely exiting the water",
            "P&T 2: bubbles": f" did {get_adjective2()} job of blowing bubbles on and in the water",
            "P&T 2: face wet and in water": f" was comfortable fully submerging {gender1[gender]} face in the water",
            "P&T 2: object recovery": f" did {get_adjective2()} job of attempting to recover objects from below the surface of the water",
            "P&T 2: entry from sitting w/ PFD": f" did {get_adjective2()} job of entering the water from a sitting position after waiting for {gender1[gender]} parent to get into the water",
            "P&T 2: front floats": f" did {get_adjective2()} job staying relaxed when doing {gender1[gender]} floats on {gender1[gender]} front with {gender1[gender]} face in the water",
            "P&T 2: back floats": f" did {get_adjective2()} job staying relaxed when doing {gender1[gender]} floats on {gender1[gender]} back",
            "P&T 2: kicking on front": f" performed {get_adjective1()} flutter kicking on {gender1[gender]} front as {name} did {get_adjective2()} job of kicking while keeping {gender1[gender]} arms and legs straight (in rocketship position) with {gender1[gender]} face in the water",
            "P&T 2: kicking on back": f" performed {get_adjective1()} flutter kicking on {gender1[gender]} back as {name} did {get_adjective2()} job of kicking while keeping {gender1[gender]} arms to {gender1[gender]} sides and {gender1[gender]} legs straight (in pencil position) with {gender1[gender]} ears in the water",
            "P&T 2: surface passes": f" was relaxed while being passed between myself and {gender1[gender]} parent",
            "P&T 3: jumps": f" did {get_adjective2()} job of safely jumping into the water",
            "P&T 3: entry and submerge": f" did {get_adjective2()} job returning to surface of the water in a controlled manner during {gender1[gender]} jumps",
            "P&T 3: hold breath": f" was comfortable holding {gender1[gender]} breath underwater",
            "P&T 3: object recovery": f" did {get_adjective2()} job of grabbing objects from the bottom of the pool",
            "P&T 3: swim to survive (jump+return to edge)": f" did {get_adjective2()} job of safely entering the water and returning to the edge during {gender1[gender]} swim to survive sequence (skill 7)",
            "P&T 3: swim to survive (jump+float)": f" did {get_adjective2()} job of maneuvering into a float during {gender1[gender]} swim to survive sequence (skill 8)",
            "P&T 3: front starfish floats": f" did {get_adjective2()} job with {gender1[gender]} starfish floats on {gender1[gender]} front as {gender2[gender]} maintained starfish position",
            "P&T 3: back starfish floats": f" did {get_adjective2()} job with {gender1[gender]} starfish floats on {gender1[gender]} back as {gender2[gender]} maintained starfish position",
            "P&T 3: front pencil floats": f" did {get_adjective2()} job with {gender1[gender]} pencil floats on {gender1[gender]} front as {gender2[gender]} kept {gender1[gender]} arms to {gender1[gender]} sides and {gender1[gender]} legs straight",
            "P&T 3: back pencil floats": f" did {get_adjective2()} job with {gender1[gender]} floats on {gender1[gender]} back as {gender2[gender]} kept {gender1[gender]} arms to {gender1[gender]} sides and {gender1[gender]} legs straight",
            "P&T 3: kicking on front": f" performed {get_adjective1()} flutter kicking on {gender1[gender]} front as {name} did a great job of keeping {gender1[gender]} arms and legs straight (in rocketship position) with {gender1[gender]} face in the water while kicking",
            "P&T 3: kicking on back": f" performed {get_adjective1()} flutter kicking on {gender1[gender]} back as {name} did a great job of keeping {gender1[gender]} arms to {gender1[gender]} sides and {gender1[gender]} legs straight (in pencil position) while kicking with {gender1[gender]} ears in the water",
            "P&T 3: Underwater passes": f" did {get_adjective2()} job with underwater passes as {gender2[gender]} remained relaxed while being passed underwater",
            "PS 1: enter and exit": f" did {get_adjective2()} job of safely entering and exiting the water",
            "PS 1: jumps": f" did {get_adjective2()} job recovering of {gender1[gender]} balance after jumping into the water",
            "PS 1: face wet": f" was comfortable fully submerging {gender1[gender]} face in the water",
            "PS 1: bubbles": f" did {get_adjective2()} job of blowing bubbles underwater",
            "PS 1: front floats": f" did {get_adjective2()} job with {gender1[gender]} starfish floats on {gender1[gender]} front with assistance",
            "PS 1: back floats": f" did {get_adjective2()} job with {gender1[gender]} starfish floats on {gender1[gender]} back with assistance",
            "PS 1: front+back floats": f" did {get_adjective2()} job doing starfish floats on {gender1[gender]} front and back with assistance",
            "PS 1: movement": f" was comfortable moving through the water safely",
            "PS 1: front glides": f" performed {get_adjective1()} front glides with assistance as {name} did a {get_adjective1()} job of keeping {gender1[gender]} arms and legs straight (in rocketship position)",
            "PS 1: back glides": f" performed {get_adjective1()} back glides with assistance as {name} did a great job of keeping {gender1[gender]} arms to {gender1[gender]} sides and {gender1[gender]} legs straight (in pencil position)",
            "PS 2: enter and exit": f" did {get_adjective2()} job of safely entering and exiting the water with a lifejacket",
            "PS 2: jumps": f" did {get_adjective2()} job recovering of {gender1[gender]} balance after jumping into the water",
            "PS 2: submerge": f" was comfortable fully submerging underwater",
            "PS 2: submerge and exhale": f" did {get_adjective2()} job of fully submerging and blowing bubbles underwater",
            "PS 2: front floats": f" did {get_adjective2()} job with {gender1[gender]} starfish floats on {gender1[gender]} front with a lifejacket",
            "PS 2: back floats": f" did {get_adjective2()} job with {gender1[gender]} starfish floats on {gender1[gender]} back with a lifejacket",
            "PS 2: front+back floats": f" did {get_adjective2()} job doing starfish floats on {gender1[gender]} front and back with a lifejacket",
            "PS 2: lateral rolls": f" did {get_adjective2()} job with {gender1[gender]} lateral rollovers (rolling from front-to-back-to-front starfish floats) with a lifejacket",
            "PS 2: front glides": f" performed {get_adjective1()} front glides with a lifejacket as {name} did a great job of keeping {gender1[gender]} arms and legs straight (in rocketship position)",
            "PS 2: back glides": f" performed {get_adjective1()} front glides with a lifejacket as {name} did a great job of keeping {gender1[gender]} arms to {gender1[gender]} sides and {gender1[gender]} legs straight (in pencil position)",
            "PS 2: flutter kick": f" performed flutter kicking on {gender1[gender]} back {get_adjective3()} as {gender2[gender]} maintained steady and consistently-rhythmic kicking",
            "PS 3: jumps": f" did {get_adjective2()} job returning to surface of the water in a controlled manner during {gender1[gender]} jumps",
            "PS 3: sideways entries": f" did {get_adjective2()} job returning to surface of the water in a controlled manner during {gender1[gender]} sideways entries",
            "PS 3: submerge and hold breath": f" was comfortable holding {gender1[gender]} breath underwater for three seconds",
            "PS 3: submerge and exhale": f" did {get_adjective2()} job of fully submerging and blowing bubbles underwater",
            "PS 3: object recovery": f" did {get_adjective2()} job of grabbing objects from the bottom of the pool",
            "PS 3: swim to survive": f" did {get_adjective2()} job with {gender1[gender]} swim to survive sequence",
            "PS 3: front floats": f" did {get_adjective2()} job with {gender1[gender]} floats on {gender1[gender]} front as {gender2[gender]} kept {gender1[gender]} face in the water and maintained starfish position",
            "PS 3: back floats": f" did {get_adjective2()} job with {gender1[gender]} floats on {gender1[gender]} back as {gender2[gender]} kept {gender1[gender]} ears in the water and maintained starfish position",
            "PS 3: lateral rolls": f" did {get_adjective2()} job with {gender1[gender]} lateral rollovers (rolling from front-to-back-to-front-starfish floats) as {gender1[gender]} rollovers were controlled and {gender2[gender]} remained horizontal throughout",
            "PS 3: front glides": f" performed {get_adjective1()} front glides as {name} put {gender1[gender]} face in the water and kept {gender1[gender]} arms and legs straight (in a rocketship position)",
            "PS 3: back glides": f" performed {get_adjective1()} back glides as {name} put {gender1[gender]} ears in the water, kept {gender1[gender]} arms to {gender1[gender]} sides, and kept {gender1[gender]} legs straight (pencil position)",
            "PS 3: flutter kick on front": f" performed flutter kicking on {gender1[gender]} front {get_adjective3()} as {gender2[gender]} maintained steady and consistently-rhythmic kicking",
            "PS 3: flutter kick on back": f" performed flutter kicking on {gender1[gender]} back {get_adjective3()} as {gender2[gender]} maintained steady and consistently-rhythmic kicking",
            "PS 4: jumps": f" did {get_adjective2()} job returning to surface of the water in a controlled manner during {gender1[gender]} jumps",
            "PS 4: sideways entries": f" did {get_adjective2()} job returning to surface of the water in a controlled manner during {gender1[gender]} sideways entries",
            "PS 4: treading": f" did a great job treading as {gender2[gender]} kept {gender1[gender]} mouth and nose above water and supported {gender4[gender]} with strong kicking and sculling action",
            "PS 4: open eyes underwater": f" did {get_adjective2()} job of fully submerging and opening {gender1[gender]} eyes underwater",
            "PS 4: object recovery": f" did {get_adjective2()} job of grabbing objects from the bottom of the pool",
            "PS 4: swim to survive 6.(PFD+jump)": f" did {get_adjective2()} job with {gender1[gender]} swim to survive sequence with a PFD as {gender2[gender]} performed a controlled sideways entry, kept {gender4[gender]} afloat when treading with strong sculling, and used a rhythmic flutter kick to swim",
            "PS 4: swim to survive 7.(no PFD or jump)": f" did {get_adjective2()} job with {gender1[gender]} swim to survive sequence as {gender2[gender]} performed {get_adjective2()} front float, rolled over to {gender1[gender]} back, and used a rhythmic flutter kick to swim",
            "PS 4: side glides": f" performed {get_adjective1()} side glides as {name} put {gender1[gender]} bottom arm's shoulder to {gender1[gender]} ear, kept {gender1[gender]} top arm to {gender1[gender]} side, and kept {gender1[gender]} legs straight",
            "PS 4: flutter kick on front": f" performed flutter kicking on {gender1[gender]} front {get_adjective3()} as {gender2[gender]} maintained steady and consistently-rhythmic kicking",
            "PS 4: flutter kick on back": f" performed flutter kicking on {gender1[gender]} back {get_adjective3()} as {gender2[gender]} maintained steady and consistently-rhythmic kicking",
            "PS 4: flutter kick on side": f" performed flutter kicking on {gender1[gender]} side {get_adjective3()} as {gender2[gender]} maintained steady and consistently-rhythmic kicking",
            "PS 4: front crawl": f" performed {gender1[gender]} front crawl {get_adjective3()} as {gender2[gender]} maintained alternate arm action and a propulsive, rhythmic flutter kick",
            "PS 5: forward rolls": f" did {get_adjective2()} job returning to surface of the water in a controlled manner during {gender1[gender]} forward rolls",
            "PS 5: treading": f" did a great job treading as {gender2[gender]} kept {gender1[gender]} mouth and nose above water, remained vertical, and supported {gender4[gender]} with strong kicking and sculling action",
            "PS 5: submerge and hold breath": f" was comfortable holding {gender1[gender]} breath underwater for five seconds",
            "PS 5: object recovery": f" did {get_adjective2()} job of grabbing objects from the bottom of the pool without {gender1[gender]} feet touching the bottom",
            "PS 5: swim to survive": f" did {get_adjective2()} job with {gender1[gender]} swim to survive sequence as {gender2[gender]} performed a controlled sideways entry, kept {gender4[gender]} afloat when treading with strong sculling, and used a rhythmic flutter kick while swimming",
            "PS 5: whip kick in vertical position": f" remained vertical when performing symmetrical whip kicks, keeping {gender1[gender]} knees apart during {gender1[gender]} simultaneous and symmetrical kicks",
            "PS 5: front crawl": f" performed {gender1[gender]} front crawl {get_adjective3()} as {gender2[gender]} maintained alternate arm action and a propulsive, rhythmic flutter kick with a slight knee bend",
            "PS 5: back crawl": f" performed {gender1[gender]} back crawl {get_adjective3()} as {gender2[gender]} maintained alternate arm action and a propulsive, rhythmic flutter kick",
            "PS 5: interval training": f" performed interval training {get_adjective3()} as {gender2[gender]} maintained steady and consistently-rhythmic kicking during every set of flutter kick on {gender1[gender]} back",
        })
        constructive_feedback_dict.update({
            "P&T 1: readiness for submersion": f" try to become more comfortable with getting {gender1[gender]} face wet; one way to help {gender1[gender]} achieve this would be to sprinkle water on {gender1[gender]} face during bath time",
            "P&T 1: front floats": f" should try to relax more during {gender1[gender]} front floats; this just comes with time, but coming to parent & tot swims could help {gender1[gender]} feel more comfortable quicker",
            "P&T 1: back floats": f" should try to relax more during {gender1[gender]} back floats; this just comes with time, but coming to parent & tot swims could help {gender1[gender]} feel more comfortable quicker",
            "P&T 1: legs: tickling, splashing, kicking | front": f" work on becoming more comfortable putting {gender1[gender]} chin in the water; splashing water on {gender1[gender]} chin during bath time or parent & tot swims could help with this",
            "P&T 1: legs: tickling, splashing, kicking | back": f" work on becoming more comfortable putting {gender1[gender]} ears in the water; splashing water on {gender1[gender]} ears during bath time or parent & tot swims could help with this",
            "P&T 2: bubbles": f" try to improve on blowing bubbles on and in the water; {gender2[gender]} can do this by pretending to blow out a candle outside of the water before doing this same action with {gender1[gender]} mouth on and in the water",
            "P&T 2: face wet and in water": f" try to become more comfortable with submerging {gender1[gender]} face in the water; one way to help {gender1[gender]} achieve this would be to sprinkle water on {gender1[gender]} face during bath time", 
            "P&T 2: object recovery": f" try to become more comfortable with going underwater to grab objects; {gender2[gender]} can do this by dipping {gender1[gender]} cheeks in the water before progressing to submerging {gender1[gender]} mouth, ears, nose, and eyes",
            "P&T 2: kicking on front | position": f" When kicking on {gender1[gender]} front, {name} should remember to keep {gender1[gender]} arms and legs straight (in rocketship position)",
            "P&T 2: kicking on front | face in water": f" When kicking on {gender1[gender]} front, {name} should try to put {gender1[gender]} face in the water; one way to help {gender5[gender]} be more comfortable with this would be to sprinkle water on {gender1[gender]} face during bath time or parent & tot swims",
            "P&T 2: kicking on back | position": f" work on keeping {gender1[gender]} arms to {gender1[gender]} sides and {gender1[gender]} legs straight (pencil position) when kicking on {gender1[gender]} back",
            "P&T 2: kicking on back | ears in water": f" When kicking on {gender1[gender]} back, {name} should try to put {gender1[gender]} ears in the water; one way to help {gender5[gender]} be more comfortable with this would be to sprinkle water on {gender1[gender]} ears during bath time or parent & tot swims",
            "P&T 3: entry and submerge/hold breath/etc. | scared of submerging": f" try to become more comfortable with going underwater; {gender2[gender]} can become more used to this by dipping {gender1[gender]} cheeks in the water before progressing to submerging {gender1[gender]} mouth, ears, nose, and eyes",
            "P&T 3: swim to survive (jump+float) | scared of jumping": f" get more practice with jumping into the water and re-orienting {gender4[gender]} so {gender2[gender]} can better perform {gender1[gender]} swim to survive skill (skill 8); holding onto {name} less and less with every jump can help {gender5[gender]} gain more confidence in this regard",
            "P&T 3: swim to survive (jump+float) | scared of floating": f" get more practice with floating on the water by {gender4[gender]} so {gender2[gender]} can better perform {gender1[gender]} swim to survive skill (skill 8); holding onto {name} less and less every float can help {gender5[gender]} gain more confidence in this regard",
            "P&T 3: front starfish floats": f" make sure to keep {gender1[gender]} arms and legs out in a starfish position while doing {gender1[gender]} front starfish floats",
            "P&T 3: back starfish floats": f" make sure to keep {gender1[gender]} arms and legs out in a starfish position while doing {gender1[gender]} back starfish floats",
            "P&T 3: front pencil floats": f" make sure to keep {gender1[gender]} arms to {gender1[gender]} sides and {gender1[gender]} legs straight when performing {gender1[gender]} front pencil floats",
            "P&T 3: back pencil floats": f" make sure to keep {gender1[gender]} arms to {gender1[gender]} sides and {gender1[gender]} legs straight when performing {gender1[gender]} back pencil floats",
            "P&T 3: kicking on front | position": f" When kicking on {gender1[gender]} front, {name} should remember to keep {gender1[gender]} arms and legs straight (in rocketship position)",
            "P&T 3: kicking on front | face in water": f" When kicking on {gender1[gender]} front, {name} should try to put {gender1[gender]} face in the water; one way to help {gender5[gender]} be more comfortable with this would be to sprinkle water on {gender1[gender]} face during bath time or parent & tot swims",
            "P&T 3: kicking on back | position": f" work on keeping {gender1[gender]} arms to {gender1[gender]} sides and {gender1[gender]} legs straight (pencil position) when kicking on {gender1[gender]} back",
            "P&T 3: kicking on back | ears in water": f" When kicking on {gender1[gender]} back, {name} should try to put {gender1[gender]} ears in the water; one way to help {gender5[gender]} be more comfortable with this would be to sprinkle water on {gender1[gender]} ears during bath time or parent & tot swims",
            "PS 1: face wet": f" try to become more comfortable with submerging {gender1[gender]} face in the water; {gender2[gender]} can do this by dipping {gender1[gender]} cheeks in the water before progressing to submerging {gender1[gender]} mouth, ears, nose, and eyes",
            "PS 1: bubbles": f" try to improve on blowing bubbles in the water; {gender2[gender]} can do this by pretending to blow out a candle outside of the water before doing this same action with {gender1[gender]} mouth in the water",
            "PS 1: front floats": f" make sure to keep {gender1[gender]} arms and legs out in a starfish position while doing {gender1[gender]} front floats",
            "PS 1: back floats": f" make sure to keep {gender1[gender]} arms and legs out in a starfish position while doing {gender1[gender]} back floats",
            "PS 1: movement": f" work on comfortably moving through the water in a lifejacket; this just comes with more practice walking around in the water and coming to parent & tot swims can help",
            "PS 1: front glides": f" work on keeping {gender1[gender]} arms and legs straight (in rocketship position) during {gender1[gender]} front glides",
            "PS 1: back glides": f" work on keeping {gender1[gender]} arms to {gender1[gender]} sides and {gender1[gender]} legs straight (pencil position) during {gender1[gender]} back glides",
            "PS 2: submerge": f" try to become more comfortable with going underwater; {gender2[gender]} can do this by dipping {gender1[gender]} cheeks in the water before progressing to submerging {gender1[gender]} mouth, ears, nose, and eyes",
            "PS 2: submerge and exhale": f" try to improve on blowing bubbles while submerged underwater; {gender2[gender]} can do this by pretending to blow out a candle outside of the water before doing this same action with {gender1[gender]} mouth in the water before progressing to doing it while fully submerged",
            "PS 2: front floats": f" make sure to keep {gender1[gender]} arms and legs out in a starfish position while doing {gender1[gender]} front floats",
            "PS 2: back floats": f" make sure to keep {gender1[gender]} arms and legs out in a starfish position while doing {gender1[gender]} back floats",
            "PS 2: lateral rolls": f" When performing {gender1[gender]} lateral rolls starting from a front float position, {name} should try to high five one hand with {gender1[gender]} other hand to help {gender5[gender]} flip onto {gender1[gender]} back, perform a starfish float, and repeat the same high five maneuver to get back onto {gender1[gender]} front",
            "PS 2: front glides": f" work on keeping {gender1[gender]} arms and legs straight (in rocketship position) during {gender1[gender]} front glides",
            "PS 2: back glides": f" work on keeping {gender1[gender]} arms to {gender1[gender]} sides and {gender1[gender]} legs straight (pencil position) during {gender1[gender]} back glides",
            "PS 2: flutter kick": f" make sure to keep {gender1[gender]} legs kicking straight and in a rhythmic way when {gender1[gender]} performs {gender1[gender]} flutter kicking on back",
            "PS 3: submerge and hold breath": f" try to become more comfortable with going underwater; {gender2[gender]} can do this by dipping {gender1[gender]} cheeks in the water before progressing to submerging {gender1[gender]} mouth, ears, nose, and eyes",
            "PS 3: submerge and exhale": f" try to improve on blowing bubbles while submerged underwater; {gender2[gender]} can do this by pretending to blow out a candle outside of the water before doing this same action with {gender1[gender]} mouth in the water before progressing to doing it while fully submerged",
            "PS 3: object recovery": f" try to become more comfortable with going underwater to grab objects; {gender2[gender]} can do this by dipping {gender1[gender]} cheeks in the water before progressing to submerging {gender1[gender]} mouth, ears, nose, and eyes",
            "PS 3: swim to survive | lateral rolls": f" aim to improve {gender1[gender]} lateral rolls in order to better perform {gender1[gender]} swim to survive sequence. When performing lateral rolls starting from a back float position, {name} should try to high five one hand with {gender1[gender]} other hand to help {gender5[gender]} flip onto {gender1[gender]} front",
            "PS 3: swim to survive | swim 3m": f" aim to improve {gender1[gender]} kicking on {gender1[gender]} front in order to better perform {gender1[gender]} swim to survive sequence. When flutter kicking on {gender1[gender]} front, {name} should make sure to keep {gender1[gender]} legs kicking straight and in a rhythmic pattern",
            "PS 3: front floats": f" make sure to keep {gender1[gender]} arms and legs out in a starfish position while doing {gender1[gender]} front floats",
            "PS 3: back floats": f" make sure to keep {gender1[gender]} arms and legs out in a starfish position while doing {gender1[gender]} back floats",
            "PS 3: lateral rolls": f" When performing {gender1[gender]} lateral rolls starting from a front float position, {name} should try to high five one hand with {gender1[gender]} other hand to help {gender5[gender]} flip onto {gender1[gender]} back, perform a starfish float, and repeat the same high five maneuver to get back onto {gender1[gender]} front",
            "PS 3: front glides": f" work on keeping {gender1[gender]} arms and legs straight (in rocketship position) during {gender1[gender]} front glides",
            "PS 3: back glides": f" work on keeping {gender1[gender]} arms to {gender1[gender]} sides and {gender1[gender]} legs straight (pencil position) during {gender1[gender]} back glides",
            "PS 3: flutter kick on front": f" make sure to keep {gender1[gender]} legs kicking straight and in a rhythmic pattern when {gender1[gender]} performs {gender1[gender]} flutter kicking on front",
            "PS 3: flutter kick on back": f" make sure to keep {gender1[gender]} legs kicking straight and in a rhythmic pattern when {gender1[gender]} performs {gender1[gender]} flutter kicking on back",
            "PS 4: treading": f" aim to improve {gender1[gender]} treading by keeping {gender1[gender]} kicking consistent and by pushing the water in an out in a controlled manner with as much strength as {gender2[gender]} can muster using {gender1[gender]} hands",
            "PS 4: object recovery": f" try to become more comfortable with going underwater to grab objects; {gender2[gender]} can do this by dipping {gender1[gender]} cheeks in the water before progressing to submerging {gender1[gender]} mouth, ears, nose, and eyes",
            "PS 4: swim to survive 6.(PFD+jump) | treading": f" aim to improve {gender1[gender]} treading in order to better perform {gender1[gender]} swim to survive sequence (skill 6). {gender3[gender]} can do this by keeping {gender1[gender]} kicking consistent and by pushing the water in an out in a controlled manner with as much strength as {gender2[gender]} can muster using {gender1[gender]} hands",
            "PS 4: swim to survive 6.(PFD+jump) | kick 5m": f" aim to improve {gender1[gender]} flutter kick in order to better perform {gender1[gender]} swim to survive sequence (skill 6). {gender3[gender]} can do this by making sure to keep {gender1[gender]} legs kicking straight and in a rhythmic pattern",
            "PS 4: swim to survive 7.(no PFD or jump) | lateral roll": f" aim to improve {gender1[gender]} lateral rolls in order to better perform {gender1[gender]} swim to survive sequence (skill 7). When performing lateral rolls starting from a front float position, {name} should try to high five one hand with {gender1[gender]} other hand to help {gender5[gender]} flip onto {gender1[gender]} back",
            "PS 4: swim to survive 7.(no PFD or jump) | swim 5m": f" aim to improve {gender1[gender]} flutter kick in order to better perform {gender1[gender]} swim to survive sequence (skill 7). {gender3[gender]} can do this by making sure to keep {gender1[gender]} legs kicking straight and in a rhythmic pattern",
            "PS 4: side glides": f" When performing {gender1[gender]} side glides, should work to keep {gender1[gender]} bottom arm's shoulder glued to {gender1[gender]} head and {gender1[gender]} legs straight",
            "PS 4: flutter kick on front": f" make sure to keep {gender1[gender]} body streamlined (arms in a rocketship position) and {gender1[gender]} legs kicking straight and in a rhythmic pattern when {gender2[gender]} performs {gender1[gender]} flutter kicking on front",
            "PS 4: flutter kick on back": f" make sure to keep {gender1[gender]} body streamlined (arms to {gender1[gender]} sides) and {gender1[gender]} legs kicking straight and in a rhythmic pattern when {gender2[gender]} performs {gender1[gender]} flutter kicking on back",
            "PS 4: flutter kick on side": f" When performing {gender1[gender]} flutter kicking on side, {name} should make sure to keep {gender1[gender]} body streamlined (bottom arm glued to {gender1[gender]} shoulder) and {gender1[gender]} legs kicking straight and in a rhythmic pattern",
            "PS 4: front crawl": f" When performing {gender1[gender]} front crawl, {name} should make sure to keep {gender1[gender]} arms moving in alternate action and to keep {gender1[gender]} legs kicking strong and rhythmically",
            "PS 5: treading": f" aim to improve {gender1[gender]} treading by keeping {gender1[gender]} kicking consistent and by pushing the water in an out in a controlled manner with as much strength as {gender2[gender]} can muster using {gender1[gender]} hands",
            "PS 5: swim to survive | treading": f" aim to improve {gender1[gender]} treading in order to better perform {gender1[gender]} swim to survive sequence. {gender3[gender]} can do this by keeping {gender1[gender]} kicking consistent and by pushing the water in an out in a controlled manner with as much strength as {gender2[gender]} can muster using {gender1[gender]} hands",
            "PS 5: swim to survive | swim/kick 10m": f" aim to improve {gender1[gender]} flutter kick in order to better perform {gender1[gender]} swim to survive sequence. {gender3[gender]} can do this by making sure to keep {gender1[gender]} legs kicking straight and in a rhythmic pattern",
            "PS 5: whip kick": f" When performing {gender1[gender]} whip kick, {name} should work to keep {gender1[gender]} kick simultaneous and symmetrical and {gender1[gender]} knees apart (but {gender1[gender]} feet further apart than {gender1[gender]} knees) during said kick. After the kick, {gender1[gender]} heels should recover toward {gender1[gender]} buttocks.",
            "PS 5: front crawl": f" When performing {gender1[gender]} front crawl, {name} should make sure to keep {gender1[gender]} alternate arm action consistent and to keep {gender1[gender]} legs kicking strong and rhythmically with a slight knee bend",
            "PS 5: back crawl": f" When performing {gender1[gender]} back crawl, {name} should make sure to keep {gender1[gender]} alternate arm action consistent and to keep {gender1[gender]} legs kicking strong and rhythmically",
            "PS 5: interval training": f" make sure to keep {gender1[gender]} body streamlined (arms to {gender1[gender]} sides) and {gender1[gender]} legs kicking straight and in a rhythmic pattern when {gender2[gender]} performs {gender1[gender]} flutter kicking on back during interval training",
        })

        positive_feedback1 = self.positive_feedback_combo_box_1.currentText()
        positive_feedback_var1 = positive_feedback_dict.get(positive_feedback1, "")

        positive_feedback2 = self.positive_feedback_combo_box_2.currentText()
        positive_feedback_var2 = positive_feedback_dict.get(positive_feedback2, "")

        constructive_feedback1 = self.constructive_feedback_combo_box_1.currentText()
        constructive_feedback_var1 = constructive_feedback_dict.get(constructive_feedback1, "")

        constructive_feedback2 = self.constructive_feedback_combo_box_2.currentText()
        constructive_feedback_var2 = constructive_feedback_dict.get(constructive_feedback2, "")

        positive_feedback3 = self.positive_feedback_combo_box_3.currentText()
        positive_feedback_var3 = positive_feedback_dict.get(positive_feedback3, "")

        positive_feedback4 = self.positive_feedback_combo_box_4.currentText()
        positive_feedback_var4 = positive_feedback_dict.get(positive_feedback4, "")

        # Update the result label
        intro = getintro()
        positive_feedback_intro = ""
        if positive_feedback_var1:
            positive_feedback_intro += f" {name}{positive_feedback_var1}"
        if positive_feedback_var2:
            if positive_feedback_var2.startswith("'s"):
                positive_feedback_intro += f" and {name}{positive_feedback_var2}!"
            else:
                positive_feedback_intro += f" and {name}{positive_feedback_var2}!"
        else:
            positive_feedback_intro += "!" if positive_feedback_var1 else ""

        constructive_feedback = ""
        if constructive_feedback_var1:
            if constructive_feedback_var1.startswith(" When"):
                constructive_feedback += f"{constructive_feedback_var1}"
            else:
                constructive_feedback += f" {name} should{constructive_feedback_var1}"
        if constructive_feedback_var2:
            if constructive_feedback_var2.startswith(" When"):
                constructive_feedback += f".{constructive_feedback_var2}."
            else:
                constructive_feedback += f". {gender3[gender]} should also{constructive_feedback_var2}."
        else:
            constructive_feedback += "." if constructive_feedback_var1 else ""

        positive_feedback_conclusion = ""
        if positive_feedback_var3:
            positive_feedback_conclusion += f" {name}{positive_feedback_var3}"
        if positive_feedback_var4:
            if positive_feedback_var4.startswith("'s"):
                positive_feedback_conclusion += f" and {name}{positive_feedback_var4}!"
            else:
                positive_feedback_conclusion += f" and {name}{positive_feedback_var4}!"
        else:
            positive_feedback_conclusion += "!" if positive_feedback_var3 else ""

        result = f"{intro}{positive_feedback_intro}{constructive_feedback}{positive_feedback_conclusion} {getconclusion()}"
        self.result_label.setText(result)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())
