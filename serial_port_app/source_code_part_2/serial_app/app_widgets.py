
""" This module provides the application widgets for the view to manage the 'serial app' application. """

from pathlib import Path

from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtWidgets import (
    QMenuBar, QMenu
)


class SerialMenuBar(QMenuBar):
    def __init__(self, parent=None):
        super().__init__(parent)

        file_menu = QMenu("&File", self)
        command_menu = QMenu("&Commands", self)

        self.addMenu(file_menu)
        self.addMenu(command_menu)

        # Define the path to the 'icons' folder (we should replace to somewhere else. We just leave it here for now.)
        self.icon_folder = Path.cwd() / 'icons'

        self._create_actions()

        file_menu.addAction(self.exit_action)

    def _create_actions(self):
        self.exit_action = QAction(QIcon(f"{self.icon_folder / 'file-exit.svg'}"), "&Exit", self)

