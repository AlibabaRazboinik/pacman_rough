"""
    1) Учимся рисовать квадраты / кружочки / картинки
    2) Учимся двигать "персонажа"
    3) Из геодаты рисуем уровень, не позволяя "персонажу" ходить вне геодаты.
"""

import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QPainter, QPixmap
from PyQt5.QtWidgets import QLabel


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(850, 700)
        self.draw_pacman()

    def draw_pacman(self):
        self.pacman = QLabel(self)
        picture = QPixmap("graphics\\pac.png")
        self.pacman.setPixmap(picture)
        self.pacman.resize(100, 100)
        self.pacman.move(100, 100)
        self.pacman.show()

    def keyPressEvent(self, QKeyEvent):
        ...


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec_())
