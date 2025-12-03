
""" This module provides the view for the 'serial app' application. """


from PyQt6.QtWidgets import (
    QMainWindow,
    QHBoxLayout,
    QWidget
)


class SerialWindow(QMainWindow):
    """Main Window."""
    def __init__(self, parent=None):
        """Initializer"""
        super().__init__(parent)
        self.setWindowTitle("Serial Port Application")
        self.resize(1000, 700)
        self.setStyleSheet("font-family: 'JetBrains Mono'; font-size: 13px;")

        # Assign a central widget and layout to the application.
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.window_layout = QHBoxLayout()
        self.central_widget.setLayout(self.window_layout)

