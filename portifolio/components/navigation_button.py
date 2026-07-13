from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QFrame ,QPushButton, QFrame


class NavigationButton(QWidget):
    def __init__(self):
        super().__init__()

        self.navigation_frame = QFrame()
        self.navigation_layout = QVBoxLayout(self.navigation_frame) 

        self.navigation_buttons = ['HOME', 'ABOUT', 'PROJECTS', 'CONTACT', 'SKILLS']
        for text in buttons:
            button = QPushButton(text)

        self.navigation_layout.addWidget(button)

        self.navigation_buttons.append(button)

        self.navigation_layout.addWidget(self.button_HOME)
        self.navigation_layout.addWidget(self.button_ABOUT)
        self.navigation_layout.addWidget(self.button_PROJECTS)
        self.navigation_layout.addWidget(self.button_CONTACT)
        self.navigation_layout.addWidget(self.button_SKILLS)

        self.layout.addWidget(self.navigation_frame)
