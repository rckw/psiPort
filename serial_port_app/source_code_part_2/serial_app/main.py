
""" This module provides the serial application loop """

# Standard library imports
import sys

# Third-party library imports
from PyQt6.QtWidgets import QApplication

# Local application imports
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