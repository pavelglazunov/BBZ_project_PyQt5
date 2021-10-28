import sys

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLabel, QLineEdit
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QAction
from PyQt5.QtGui import QPalette
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from time import sleep
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLCDNumber, QLabel
from PyQt5.QtGui import QPixmap, QTransform
from random import randrange
from time import monotonic
from PIL import Image
from PIL import *
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGraphicsScene, \
    QGraphicsView, QGraphicsLinearLayout, QGraphicsWidget, QHBoxLayout
from threading import Thread

import sys
import time
import os


class Tanks(QWidget):
    i = 0

    def __init__(self):
        super().__init__()
        self.initUI()

    # def get_windows(self, list_of_window1):
    #     self.list_of_window1 = list_of_window1

    def initUI(self):
        self.pumpking_speed = 10
        self.pumpking_player1_x = 390
        self.pumpking_player2_x = 795

        self.main_window = QWidget(self)
        self.main_window.resize(1000, 700)
        self.main_window.setWindowTitle('Catchers')

        self.main_background = QLabel(self)
        self.main_background.resize(1000, 700)
        self.main_background.setPixmap(QPixmap('./texture/catchers_texture/background.png'))

        self.pumpking_player1 = QLabel(self)
        self.pumpking_player1.resize(50, 40)
        self.pumpking_player1.move(self.pumpking_player1_x, 605)
        self.pumpking_player1.setPixmap(QPixmap('./texture/catchers_texture/pumpking_texure_1.png'))

        self.pumpking_player2 = QLabel(self)
        self.pumpking_player2.resize(50, 40)
        self.pumpking_player2.move(self.pumpking_player2_x, 605)
        self.pumpking_player2.setPixmap(QPixmap('./texture/catchers_texture/pumpking_texure_1.png'))


    def keyPressEvent(self, event):
        if (event.key() == QtCore.Qt.Key_D) and (self.pumpking_player1_x <= 530):
            self.pumpking_player1_x += self.pumpking_speed
            self.pumpking_player1.move(self.pumpking_player1_x, 605)

        if (event.key() == QtCore.Qt.Key_A) and (self.pumpking_player1_x >= 215):
            self.pumpking_player1_x -= self.pumpking_speed
            self.pumpking_player1.move(self.pumpking_player1_x, 605)

        if (event.key() == QtCore.Qt.Key_Right) and (self.pumpking_player1_x <= 940):
            self.pumpking_player2_x += self.pumpking_speed
            self.pumpking_player2.move(self.pumpking_player2_x, 605)

        if (event.key() == QtCore.Qt.Key_Left) and (self.pumpking_player2_x >= 616):
            self.pumpking_player2_x -= self.pumpking_speed
            self.pumpking_player2.move(self.pumpking_player2_x, 605)

    #     elif (event.key() == QtCore.Qt.Key_D) and (self.player1_x <= 900) and ((self.player1_x in self.L) and (self.player1_y in self.L2)):
    #         self.player1_x += self.player_speed
    #         self.player1.move(self.player1_x, self.player1_y)
    #
    #     elif (event.key() == QtCore.Qt.Key_A) and (self.player1_x >= 50):
    #         self.player1_x -= self.player_speed
    #         self.player1.move(self.player1_x, self.player1_y)
    #
    #
    #     elif (event.key() == QtCore.Qt.Key_Up) and (self.player2_y >= 435):
    #         self.player2_y -= self.player_speed
    #         self.player2.move(self.player2_x, self.player2_y)
    #
    #     elif (event.key() == QtCore.Qt.Key_Down) and (self.player2_y <= 600):
    #         self.player2_y += self.player_speed
    #         self.player2.move(self.player2_x, self.player2_y)
    #
    #     elif (event.key() == QtCore.Qt.Key_Right) and (self.player2_x <= 900):
    #         self.player2_x += self.player_speed
    #         self.player2.move(self.player2_x, self.player2_y)
    #
    #     elif (event.key() == QtCore.Qt.Key_Left) and (self.player2_x >= 50):
    #         self.player2_x -= self.player_speed
    #         self.player2.move(self.player2_x, self.player2_y)
    #     # if event.key() == QtCore.Qt.Key_A:


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Tanks()
    ex.show()
    sys.exit(app.exec())
