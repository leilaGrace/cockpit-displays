import sys
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtGui import QPainter, QColor
from PySide6.QtCore import QRectF


class Horizon(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cockpit Display")
        self.resize(800, 800)

    def paintEvent(self, event):
        p = QPainter(self)
        w, h = self.width(), self.height()
        p.fillRect(QRectF(0, 0, w, h / 2), QColor(70, 140, 220))     # sky
        p.fillRect(QRectF(0, h / 2, w, h / 2), QColor(140, 90, 40))  # ground


app = QApplication(sys.argv)
window = Horizon()
window.show()
sys.exit(app.exec())