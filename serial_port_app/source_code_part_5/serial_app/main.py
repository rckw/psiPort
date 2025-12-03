
""" This module provides the serial application loop """

import sys

from PyQt6.QtWidgets import QApplication

from .view import SerialWindow

def main():
    """Serial App main function"""
    # Create the application
    app = QApplication([])
    # Create the main window
    win = SerialWindow()
    win.show()
    # Run the event loop
    sys.exit(app.exec())
