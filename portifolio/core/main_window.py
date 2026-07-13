from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setup_window()
        self.setup_ui()

        def setup_window(self):
            self.setWindowTitle("Lili Portfolio")
            self.resize(1200, 800)
            self.setMinimumSize(900, 600)
        def setup_ui(self):
            self.central_widget = QWidget()

            self.setCentralWidget(self.central_widget)

            self.main_layout = QVBoxLayout(self.central_widget)

            self.sidebar = Sidebar()

            self.main_layout.addWidget(self.sidebar)