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
from PyQt5.QtGui import QPixmap
from random import randrange
from time import monotonic
import sys
import time
import os



class Osuu(QWidget):
    i = 0

    def __init__(self):
        super().__init__()
        self.initUI()

    def get_windows(self, list_of_window1):
        self.list_of_window1 = list_of_window1

    def initUI(self):
        self.background_count = 1
        self.time_to_start = 3
        self.timer = 16
        self.x_pos = randrange(0, 700, 100)
        self.y_pos = randrange(100, 600, 100)
        self.count = 0
        self.timer_is_active = 0
        self.record = 0

        self.osu_window = QWidget()
        self.osu_window.setGeometry(100, 100, 1000, 700)
        self.osu_window.setWindowTitle('Osu')
        self.osu_window.setFixedSize(1000, 700)

        # создание фонов
        self.main_background = QLabel(self)
        main_background_1 = QPixmap('./texture/osu_texture/osu_map_2')
        self.main_background.setPixmap(main_background_1)
        self.main_background.move(0, 0)

        self.background1 = QLabel(self)
        background_p1 = QPixmap('./texture/osu_texture/osu_background1.png')
        self.background1.setPixmap(background_p1)
        self.background1.move(-5, 101)

        self.background2 = QLabel(self)
        background_p2 = QPixmap('./texture/osu_texture/osu_background2.png')
        self.background2.setPixmap(background_p2)
        self.background2.move(-5, 101)
        self.background2.hide()

        self.background3 = QLabel(self)
        background_p3 = QPixmap('./texture/osu_texture/osu_background3.png')
        self.background3.setPixmap(background_p3)
        self.background3.move(-5, 101)
        self.background3.hide()

        self.background4 = QLabel(self)
        background_p4 = QPixmap('./texture/osu_texture/osu_background4.png')
        self.background4.setPixmap(background_p4)
        self.background4.move(-5, 101)
        self.background4.hide()

        self.background5 = QLabel(self)
        background_p5 = QPixmap('./texture/osu_texture/osu_background5.png')
        self.background5.setPixmap(background_p5)
        self.background5.move(-5, 101)
        self.background5.hide()

        # Создание названия
        self.game_name = QLabel(self)
        self.game_name.move(150, 20)
        self.game_name.setText('<b>Поймай кнопку</b>')
        self.game_name.setStyleSheet("QLabel{font-size: 40pt;}")

        # создание счета и времени
        self.count_text = QLabel(self)
        self.count_text.move(810, 10)
        self.count_text.setText('<b>Счет:</b>')
        self.count_text.setStyleSheet("QLabel{font-size: 25pt;}")

        self.count_text_print = QLabel(self)
        self.count_text_print.move(930, 10)
        self.count_text_print.resize(100, 50)
        self.count_text_print.setText(str(self.count))
        self.count_text_print.setStyleSheet("QLabel{font-size: 25pt;}")

        self.time_text = QLabel(self)
        self.time_text.move(810, 70)
        self.time_text.setText('<b>Время:</b>')
        self.time_text.setStyleSheet("QLabel{font-size: 25pt;}")

        self.time_text_print = QLabel(self)
        self.time_text_print.move(965, 70)
        self.time_text_print.resize(100, 50)
        self.time_text_print.setText(str(self.count))
        self.time_text_print.setStyleSheet("QLabel{font-size: 25pt;}")

        self.record_text = QLabel(self)
        self.record_text.move(810, 130)
        self.record_text.setText('<b>Рекорд:</b>')
        self.record_text.setStyleSheet("QLabel{font-size: 23pt;}")

        self.record_text_print = QLabel(self)
        self.record_text_print.move(965, 130)
        self.record_text_print.resize(100, 50)
        self.record_text_print.setText(str(self.record))
        self.record_text_print.setStyleSheet("QLabel{font-size: 23pt;}")

        # рестарт
        self.new_game_text = QLabel(self)
        self.new_game_text.move(805, 210)
        self.new_game_text.setText('<b>Новая игра</b>')
        self.new_game_text.setStyleSheet("QLabel{font-size: 20pt;}")

        self.start_btn = QPushButton('Старт', self)
        self.start_btn.resize(100, 50)
        self.start_btn.move(850, 270)
        self.start_btn.clicked.connect(self.start)

        # смена фона
        self.chende_fon_text = QLabel(self)
        self.chende_fon_text.move(805, 370)
        self.chende_fon_text.setText('<b>Сменить фон</b>')
        self.chende_fon_text.setStyleSheet("QLabel{font-size: 17pt;}")

        self.change_btn = QPushButton('-->', self)
        self.change_btn.resize(50, 50)
        self.change_btn.move(910, 420)
        self.change_btn.clicked.connect(self.next_fon)

        self.change_btn_back = QPushButton('<--', self)
        self.change_btn_back.resize(50, 50)
        self.change_btn_back.move(850, 420)
        self.change_btn_back.clicked.connect(self.befor_fon)

        # выход
        self.exit_text = QLabel(self)
        self.exit_text.move(845, 550)
        self.exit_text.setText('<b>Выход</b>')
        self.exit_text.setStyleSheet("QLabel{font-size: 22pt;}")

        self.exit_text = QLabel(self)
        self.exit_text.move(810, 590)
        self.exit_text.setText('<b>(весь прогресс будет утерян)</b>')
        self.exit_text.setStyleSheet("QLabel{font-size: 7pt;}")

        self.exit_btn = QPushButton('Выход', self)
        self.exit_btn.resize(100, 50)
        self.exit_btn.move(855, 620)
        self.exit_btn.clicked.connect(self.exit)

        # Игральная кнопка
        self.button = QPushButton('', self)
        self.button.resize(100, 100)
        self.button.move(self.x_pos, self.y_pos)
        self.button.clicked.connect(self.next_btn)
        self.button.hide()

    def start(self):
        self.button.move(350, 350)
        self.button.show()
        self.timer = 16
        self.count = 0
        self.count_text_print.setText('0')
        self.tick_timer()

    def start_timer(self):
        if self.time_to_start > 0:
            self.time_to_start -= 1
            QTimer().singleShot(wait, self.start_timer)
        else:
            self.wait = 3

    def tick_timer(self):
        if self.timer > 0:
            self.timer -= 1  # Устанавливаем значение на 1 меньше

            self.time_text_print.setText(str(self.timer))
            self.change_btn.setEnabled(False)
            self.change_btn_back.setEnabled(False)
            self.start_btn.setEnabled(False)

            self.button.setEnabled(True)

            QTimer().singleShot(1000, self.tick_timer)  # Засекаем таймер - значение в милисекундах
        else:
            if self.count > self.record:
                self.record = self.count
                self.record_text_print.setText(str(self.record))
            self.change_btn.setEnabled(True)
            self.change_btn_back.setEnabled(True)
            self.start_btn.setEnabled(True)
            self.button.setEnabled(False)

    def next_btn(self):
        self.x_pos = randrange(0, 700, 100)
        self.y_pos = randrange(100, 600, 100)
        self.button.move(self.x_pos, self.y_pos)
        self.count += 1
        self.count_text_print.setText(str(self.count))

    def next_fon(self):
        if self.background_count == 1:
            self.background1.hide()
            self.background2.show()
        elif self.background_count == 2:
            self.background2.hide()
            self.background3.show()
        elif self.background_count == 3:
            self.background3.hide()
            self.background4.show()
        elif self.background_count == 4:
            self.background4.hide()
            self.background5.show()
        elif self.background_count == 5:
            self.background5.hide()
            self.background1.show()
            self.background_count = 0
        self.background_count += 1

    def befor_fon(self):
        if self.background_count == 1:
            self.background1.hide()
            self.background5.show()
            self.background_count = 6
        elif self.background_count == 5:
            self.background5.hide()
            self.background4.show()
        elif self.background_count == 4:
            self.background4.hide()
            self.background3.show()
        elif self.background_count == 3:
            self.background3.hide()
            self.background2.show()
        elif self.background_count == 2:
            self.background2.hide()
            self.background1.show()
        self.background_count -= 1

    def exit(self):
        self.count = 0
        self.count_text_print.setText('0')
        self.time_text_print.setText('0')
        self.button.hide()
        self.timer = 0
        self.list_of_window1.setCurrentIndex(0)
