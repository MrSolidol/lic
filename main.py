import sys, random
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import uic


class MyWidget(QMainWindow):
    def __init__(self):
        self.kek = []
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton_2.clicked.connect(self.run)
    def run(self):
        self.kek.append((random.randint(-50, 400), random.randint(0, 400),
                         random.randint(5, 200)))
        self.update()

    def paintEvent(self, event):
        self.painter = QPainter()
        self.painter.begin(self)
        self.painter.setBrush(QColor(255, 255, 20))
        for i in self.kek:
           self.painter.drawEllipse(i[0], i[1], i[2], i[2])
        self.painter.end()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())