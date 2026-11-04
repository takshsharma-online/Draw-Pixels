import sys
from PyQt6.QtWidgets import QApplication, QWidget
app = QApplication(sys.argv)

window = QWidget()

window.setWindowTitle("Draw Pixels")

window.resize(800, 600)

window.show()

sys.exit(app.exec())