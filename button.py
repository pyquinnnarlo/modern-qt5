# Your main application file

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout
from modern_qt.standard_button import RoundedButtonWarning

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QWidget()

    # Create a vertical layout for the window
    window_layout = QVBoxLayout(window)

    round_button = RoundedButtonWarning("Solid Click")
    window_layout.addWidget(round_button)

    window.show()
    sys.exit(app.exec_())
