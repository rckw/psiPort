
""" This module provides the application widgets for the view to manage the 'serial app' application. """

from pathlib import Path

from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtWidgets import (
    QMenuBar, QMenu, QToolBar, QComboBox, QPushButton, QLabel, QGroupBox, QTextEdit, QLineEdit, QVBoxLayout
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


class SerialToolBar(QToolBar):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setMovable(False)

        self.cmb_ports = QComboBox()
        self.cmb_ports.setFixedSize(350, 30)
        self.cmb_ports.addItems(["COM1", "COM3", "COM4", "COM5"])  # # Items will be automatically filled in later !!!

        self.cmb_speed = QComboBox()
        self.cmb_speed.setFixedSize(350, 30)
        self.cmb_speed.addItems(["57600", "115200", "230400"])
        self.cmb_speed.setCurrentIndex(1)  # This will set the "115200" as default. Change to what you want.

        self.btn_connect = QPushButton("Connect")
        self.btn_connect.setFixedSize(100, 30)

        self.addWidget(QLabel(" Ports "))
        self.addWidget(self.cmb_ports)
        self.addSeparator()
        self.addWidget(QLabel(" Speed "))
        self.addWidget(self.cmb_speed)
        self.addSeparator()
        self.addWidget(self.btn_connect)

        self._connect_actions()

    def _connect_actions(self):
        self.btn_connect.clicked.connect(self.show_port_settings)

    def show_port_settings(self):
        print(f"Serial port: {self.cmb_ports.currentText()}")
        print(f"Serial speed: {self.cmb_speed.currentText()}")


class SerialBox(QGroupBox):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setTitle("Serial Box")

        self.terminal = QTextEdit()
        self.terminal.setReadOnly(True)

        self.command_line = QComboBox()
        self.command_line.setFixedHeight(30)
        self.command_line.setEditable(True)
        self.command_line.setInsertPolicy(QComboBox.InsertPolicy.InsertBeforeCurrent)
        self.command_line.addItem("")
        # self.command_line.setEnabled(False)

        layout = QVBoxLayout()
        layout.addWidget(self.terminal)
        layout.addWidget(self.command_line)
        self.setLayout(layout)
