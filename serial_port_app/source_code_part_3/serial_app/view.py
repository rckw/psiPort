
""" This module provides the view to manage the 'serial app' application. """


from PyQt6.QtWidgets import (
    QMainWindow,
    QHBoxLayout,
    QWidget
)

from .app_widgets import SerialMenuBar, SerialToolBar


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

        # Set the menubar defined in the app_widgets module.
        self.menu_bar = SerialMenuBar()
        self.setMenuBar(self.menu_bar)

        # Set the toolbar defined in the app_widgets module.
        self.tool_bar = SerialToolBar()
        self.addToolBar(self.tool_bar)

        self._connect_actions()

    def _connect_actions(self):
        self.menu_bar.exit_action.triggered.connect(self.close)

    def closeEvent(self, a0):
        print("Application will exit...! Bye bye!")
