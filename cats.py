import sys

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLabel, QLineEdit
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QAction
from PyQt5.QtGui import QPalette
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import *
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import *
from time import sleep
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLCDNumber, QLabel
from PyQt5.QtGui import QPixmap
from random import *
from time import monotonic
import sys
import time
import os
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget
from PyQt5.QtCore import QSize


class Cat(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def get_windows(self, list_of_windows2):
        self.list_of_windows2 = list_of_windows2

    def initUI(self):
        self.time_animacion_polayer1 = 0.5
        self.time_animacion_polayer2 = 0.5
        self.time_fish_is_active = 1
        self.wait_fish = 3

        self.count_player_1 = 0
        self.count_player_2 = 0

        self.end_game = True

        self.fish_list = [-2, -2, 1, 1, 1, 1, 1]
        self.fish_here = 1

        self.win_count = 0

        self.cat_window = QWidget()
        self.cat_window.setGeometry(100, 100, 1000, 700)
        self.cat_window.setWindowTitle('cats')
        self.cat_window.setFixedSize(1000, 700)

        self.background1 = QLabel(self)
        fon_p1 = QPixmap('./texture/cats_texture/cats_fon')
        self.background1.setPixmap(fon_p1)
        self.background1.move(0, 0)

        # Создание рыбы
        self.fish = QLabel(self)
        self.fish.move(450, 320)
        self.fish.show()
        self.fish.hide()

        # игроки
        self.player1 = QLabel(self)
        player_1 = QPixmap('./texture/cats_texture/player_1.png')
        self.player1.setPixmap(player_1)
        self.player1.move(230, 450)

        self.player2 = QLabel(self)
        player_2 = QPixmap('./texture/cats_texture/player_2.png')
        self.player2.setPixmap(player_2)
        self.player2.move(550, 110)

        self.player1_animatoin = QLabel(self)
        player_1_animation = QPixmap('./texture/cats_texture/player1_animation.png')
        self.player1_animatoin.setPixmap(player_1_animation)
        self.player1_animatoin.move(230, 370)
        self.player1_animatoin.hide()

        self.player2_animatoin = QLabel(self)
        player_2_animation = QPixmap('./texture/cats_texture/player2_animation.png')
        self.player2_animatoin.setPixmap(player_2_animation)
        self.player2_animatoin.move(465, 110)
        self.player2_animatoin.hide()

        # Счет на экране
        self.count_player_1_text = QLabel(self)
        self.count_player_1_text.move(207, 641)
        self.count_player_1_text.resize(100, 50)
        self.count_player_1_text.setText('<b>00</b>')
        self.count_player_1_text.setStyleSheet("QLabel{font-size: 20pt;}")

        self.count_player_2_text = QLabel(self)
        self.count_player_2_text.move(881, 126)
        self.count_player_2_text.resize(100, 50)
        self.count_player_2_text.setText('<b>00</b>')
        self.count_player_2_text.setStyleSheet("QLabel{font-size: 20pt;}")

        # Определение победных очков
        self.new_game_text = QLabel(self)
        self.new_game_text.move(7, 250)
        self.new_game_text.setText('<b>Играть до:</b>')
        self.new_game_text.setStyleSheet("QLabel{font-size: 12pt;}")

        self.count_need_btn_5 = QPushButton('5 очков', self)
        self.count_need_btn_5.resize(100, 30)
        self.count_need_btn_5.move(7, 290)
        self.count_need_btn_5.clicked.connect(self.win_5)
        self.count_need_btn_5.setStyleSheet('background: rgb(255, 255, 255);')

        self.count_need_btn_10 = QPushButton('10 очков', self)
        self.count_need_btn_10.resize(100, 30)
        self.count_need_btn_10.move(7, 330)
        self.count_need_btn_10.clicked.connect(self.win_10)
        self.count_need_btn_10.setStyleSheet('background: rgb(255, 255, 255);')

        self.count_need_btn_15 = QPushButton('15 очков', self)
        self.count_need_btn_15.resize(100, 30)
        self.count_need_btn_15.move(7, 370)
        self.count_need_btn_15.clicked.connect(self.win_15)
        self.count_need_btn_15.setStyleSheet('background: rgb(255, 255, 255);')

        self.start_btn = QPushButton('Новая игра', self)
        self.start_btn.resize(100, 70)
        self.start_btn.move(10, 120)
        self.start_btn.clicked.connect(self.start)
        self.start_btn.setToolTip('Сначало необходимо выбрать кол-во очков')
        self.start_btn.setStyleSheet('background: rgb(255, 255, 255);')
        self.start_btn.setEnabled(False)

        self.game_name = QLabel(self)
        self.game_name.move(150, -2)
        self.game_name.setText('<b>Голодные кошки</b>')
        self.game_name.setStyleSheet("QLabel{font-size: 50pt;}")

        self.exit_btn = QPushButton('Exit', self)
        self.exit_btn.resize(100, 50)
        self.exit_btn.move(7, 620)
        self.exit_btn.clicked.connect(self.exit)

        # Создание победного текста
        self.red_win_text = QLabel(self)
        # red_win = QPixmap('./texture/cats_texture/red_win_text.png')
        self.red_win_text.setPixmap(QPixmap('./texture/cats_texture/red_win_text.png'))
        self.red_win_text.move(150, 350)
        self.red_win_text.hide()

        self.blue_win_text = QLabel(self)
        blue_win = QPixmap('./texture/cats_texture/blue_win_text.png')
        self.blue_win_text.setPixmap(blue_win)
        self.blue_win_text.move(150, 350)
        self.blue_win_text.hide()

    def start(self):
        self.time_animacion_polayer1 = 0.5
        self.time_animacion_polayer2 = 0.5
        self.time_fish_is_active = 1
        self.wait_fish = 1

        self.count_player_1 = 0
        self.count_player_2 = 0
        self.count_player_1_text.setText('<b>' + str(self.count_player_1) + '</b>')
        self.count_player_2_text.setText('<b>' + str(self.count_player_2) + '</b>')

        self.red_win_text.hide()
        self.blue_win_text.hide()

        self.end_game = True

        self.all_block()
        self.fish_create()

        self.fish.show()

    def fish_create(self):
        if self.end_game:
            self.count_fish = choice(self.fish_list)

            if self.count_fish == -2:
                fish_p1 = QPixmap('./texture/cats_texture/bad_fish.png')
            elif self.count_fish == 1:
                fish_p1 = QPixmap('./texture/cats_texture/good_fish.png')

            self.fish.setPixmap(fish_p1)
            self.fish.show()
            self.spawn_fish()

    def spawn_fish(self):
        if self.end_game:
            self.fish_here = 1
            if self.time_fish_is_active > 0:
                self.time_fish_is_active -= 1
                QTimer().singleShot(1000, self.spawn_fish)
                if not self.end_game:
                    self.fish.hide()
            else:
                self.time_fish_is_active = 1
                self.fish_active()

    def fish_active(self):
        if self.end_game:
            wait_fish_shag = randrange(300, 1000, 100)
            if self.wait_fish > 0:
                self.fish.hide()
                self.fish_here = 0
                self.wait_fish -= 1
                QTimer().singleShot(wait_fish_shag, self.fish_active)
            else:
                self.wait_fish = 3
                self.fish_create()

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_D:
            if self.end_game == True:
                if self.fish_here == 1:
                    self.fish_here = 0
                    self.count_player_1 += self.count_fish
                    if self.count_player_1 == self.win_count:
                        self.win(1)
                    print('player1:', self.count_player_1)
                    self.count_player_1_text.setText('<b>' + str(self.count_player_1) + '</b>')
                    self.time_fish_is_active = 0
                self.player1.hide()
                self.player1_animatoin.show()
                self.tick_timer_player1()
        event.accept()

        if event.key() == QtCore.Qt.Key_K:
            if self.end_game == True:
                if self.fish_here == 1:
                    self.fish_here = 0
                    self.count_player_2 += self.count_fish
                    if self.count_player_2 == self.win_count:
                        self.win(2)
                    print('player2:', self.count_player_2)
                    self.count_player_2_text.setText('<b>' + str(self.count_player_2) + '</b>')
                    self.time_fish_is_active = 0
                self.player2.hide()
                self.player2_animatoin.show()
                self.tick_timer_player2()
        event.accept()

    def tick_timer_player1(self):
        if self.time_animacion_polayer1 > 0:
            self.fish.hide()
            self.time_animacion_polayer1 -= 1  # Устанавливаем значение на 1 меньше
            QTimer().singleShot(100, self.tick_timer_player1)
        else:
            self.player1_animatoin.hide()
            self.player1.show()
            self.time_animacion_polayer1 = 0.5

    def tick_timer_player2(self):
        if self.time_animacion_polayer2 > 0:
            self.fish.hide()
            self.time_animacion_polayer2 -= 1  # Устанавливаем значение на 1 меньше
            QTimer().singleShot(100, self.tick_timer_player2)
        else:
            self.player2_animatoin.hide()
            self.player2.show()
            self.time_animacion_polayer2 = 0.5

    def win_5(self):
        self.win_count = 5 # задает количесто очков для победы - 5
        self.start_btn.setEnabled(True) # делает кнопку "старт" активной
        self.count_need_btn_5.setStyleSheet('background: rgb(117, 255, 53);') # устанавливает цвет кнопки (зеленый)
        self.count_need_btn_10.setStyleSheet('background: rgb(255, 255, 255);') # устанавливает цвет кнопки (белый)
        self.count_need_btn_15.setStyleSheet('background: rgb(255, 255, 255);') # устанавливает цвет кнопки (белый)

    def win_10(self):
        self.win_count = 10 # задает количесто очков для победы - 10
        self.start_btn.setEnabled(True) # делает кнопку "старт" активной
        self.count_need_btn_5.setStyleSheet('background: rgb(255, 255, 255);') # устанавливает цвет кнопки (белый)
        self.count_need_btn_10.setStyleSheet('background: rgb(117, 255, 53);') # устанавливает цвет кнопки (зеленый)
        self.count_need_btn_15.setStyleSheet('background: rgb(255, 255, 255);') # устанавливает цвет кнопки (белый)

    def win_15(self):
        self.win_count = 15 # задает количесто очков для победы - 15
        self.start_btn.setEnabled(True) # делает кнопку "старт" активной
        self.count_need_btn_5.setStyleSheet('background: rgb(255, 255, 255);') # устанавливает цвет кнопки (белый)
        self.count_need_btn_10.setStyleSheet('background: rgb(255, 255, 255);') # устанавливает цвет кнопки (белый)
        self.count_need_btn_15.setStyleSheet('background: rgb(117, 255, 53);') # устанавливает цвет кнопки (зеленый)

    def all_block(self):
        self.count_need_btn_5.setEnabled(False) # делает кнопку не активной
        self.count_need_btn_10.setEnabled(False) # делает кнопку не активной
        self.count_need_btn_15.setEnabled(False) # делает кнопку не активной
        self.start_btn.hide() # прячет кнопку "старт"

    def not_all_block(self):
        self.count_need_btn_5.setEnabled(True) # делает кнопку активной
        self.count_need_btn_10.setEnabled(True) # делает кнопку активной
        self.count_need_btn_15.setEnabled(True) # делает кнопку активной
        self.count_need_btn_5.setStyleSheet('background: rgb(255, 255, 255);') # устанавливает цвет кнопки (белый)
        self.count_need_btn_10.setStyleSheet('background: rgb(255, 255, 255);') # устанавливает цвет кнопки (белый)
        self.count_need_btn_15.setStyleSheet('background: rgb(255, 255, 255);') # устанавливает цвет кнопки (белый)
        self.start_btn.show() # Показывает кнопку "старт"
        self.fish.hide() # прячет рыбу рыбу
        self.start_btn.setEnabled(False) # делает кнопку "старт" не активной

    def win(self, name):
        self.end_game = False # казывает что игра закончилась и отключает фунцкии до начала следующей игры
        self.not_all_block() # возращает кнопки к начальному сосотоянию
        if name == 1: # определяет какой игрок победил
            self.blue_win_text.show() # показывает текст о победе игрока 1
        elif name == 2: # определяет какой игрок победил
            self.red_win_text.show() # оказывает текст о победе игрока 2

    def exit(self):
        self.not_all_block() # возращает кнопки к начальному сосотоянию
        self.time_fish_is_active = 1 # обнуление таймера
        self.end_game = False # указывает что игра закончилась и отключает фунцкии до начала следующей игры
        self.list_of_windows2.setCurrentIndex(0) # устанавливает окно с индексом 0
        # print(exit_from_cats)
