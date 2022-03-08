# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'final.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
from asyncio.windows_events import NULL
import imghdr
from re import X
from turtle import pen, pencolor, rt
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog, QInputDialog, QAction, QTextEdit, QFontDialog, QColorDialog, QGridLayout,QLineEdit,QHBoxLayout
from PyQt5.uic import loadUi
from PyQt5.QtGui import QIcon, QGuiApplication
from PyQt5.QtPrintSupport import QPrintDialog, QPrinter, QPrintPreviewDialog
from PyQt5.QtCore import QFileInfo, QTimer
import sys
from fpdf import FPDF
import matplotlib
from matplotlib import pyplot as plt
from matplotlib import image
from matplotlib.axis import XAxis, YAxis
import pyqtgraph
import numpy as np
from collections import namedtuple
import pyqtgraph.exporters
import scipy.io
from scipy import signal
import h5py
import time
from matplotlib.animation import FuncAnimation
from random import randint

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
        
    def setupUi(self, MainWindow): 
        self.int=0
        self.scaling_factor= 1000
        self.scaling_factor_i= 0
        self.k = 0
        self.zoom = 1
        self.fin = 700
        self.size=0
        self.ChannelOneSelected = False
        self.ChannelTwoSelected = False
        self.ChannelThreeSelected = False
        pyqtgraph.setConfigOptions(antialias=True)
        self.fig1 , self.ax = plt.subplots()
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1094, 666)
        font = QtGui.QFont()
        font.setFamily("Myanmar Text")
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("/*Copyright (c) DevSec Studio. All rights reserved.\n"
"\n"
"MIT License\n"
"\n"
"Permission is hereby granted, free of charge, to any person obtaining a copy\n"
"of this software and associated documentation files (the \"Software\"), to deal\n"
"in the Software without restriction, including without limitation the rights\n"
"to use, copy, modify, merge, publish, distribute, sublicense, and/or sell\n"
"copies of the Software, and to permit persons to whom the Software is\n"
"furnished to do so, subject to the following conditions:\n"
"\n"
"The above copyright notice and this permission notice shall be included in all\n"
"copies or substantial portions of the Software.\n"
"\n"
"THE SOFTWARE IS PROVIDED *AS IS*, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\n"
"IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\n"
"FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE\n"
"AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER\n"
"LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,\n"
"OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.\n"
"*/\n"
"\n"
"/*-----QWidget-----*/\n"
"QWidget\n"
"{\n"
"    background-color: #3a3a3a;\n"
"    color: #fff;\n"
"    selection-background-color: #b78620;\n"
"    selection-color: #000;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QLabel-----*/\n"
"QLabel\n"
"{\n"
"    background-color: transparent;\n"
"    color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QMenuBar-----*/\n"
"QMenuBar \n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(57, 57, 57, 255),stop:1 rgba(50, 50, 50, 255));\n"
"    border: 1px solid #000;\n"
"    color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenuBar::item \n"
"{\n"
"    background-color: transparent;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenuBar::item:selected \n"
"{\n"
"    background-color: rgba(183, 134, 32, 20%);\n"
"    border: 1px solid #b78620;\n"
"    color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenuBar::item:pressed \n"
"{\n"
"    background-color: rgb(183, 134, 32);\n"
"    border: 1px solid #b78620;\n"
"    color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QMenu-----*/\n"
"QMenu\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(57, 57, 57, 255),stop:1 rgba(50, 50, 50, 255));\n"
"    border: 1px solid #222;\n"
"    padding: 4px;\n"
"    color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenu::item\n"
"{\n"
"    background-color: transparent;\n"
"    padding: 2px 20px 2px 20px;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenu::separator\n"
"{\n"
"       background-color: rgb(183, 134, 32);\n"
"    height: 1px;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenu::item:disabled\n"
"{\n"
"    color: #555;\n"
"    background-color: transparent;\n"
"    padding: 2px 20px 2px 20px;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenu::item:selected\n"
"{\n"
"    background-color: rgba(183, 134, 32, 20%);\n"
"    border: 1px solid #b78620;\n"
"    color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QToolBar-----*/\n"
"QToolBar\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(69, 69, 69, 255),stop:1 rgba(58, 58, 58, 255));\n"
"    border-top: none;\n"
"    border-bottom: 1px solid #4f4f4f;\n"
"    border-left: 1px solid #4f4f4f;\n"
"    border-right: 1px solid #4f4f4f;\n"
"\n"
"}\n"
"\n"
"\n"
"QToolBar::separator\n"
"{\n"
"    background-color: #2e2e2e;\n"
"    width: 1px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QToolButton-----*/\n"
"QToolButton \n"
"{\n"
"    background-color: transparent;\n"
"    color: #fff;\n"
"    padding: 5px;\n"
"    padding-left: 8px;\n"
"    padding-right: 8px;\n"
"    margin-left: 1px;\n"
"}\n"
"\n"
"\n"
"QToolButton:hover\n"
"{\n"
"    background-color: rgba(183, 134, 32, 20%);\n"
"    border: 1px solid #b78620;\n"
"    color: #fff;\n"
"    \n"
"}\n"
"\n"
"\n"
"QToolButton:pressed\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(57, 57, 57, 255),stop:1 rgba(50, 50, 50, 255));\n"
"    border: 1px solid #b78620;\n"
"\n"
"}\n"
"\n"
"\n"
"QToolButton:checked\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(57, 57, 57, 255),stop:1 rgba(50, 50, 50, 255));\n"
"    border: 1px solid #222;\n"
"}\n"
"\n"
"\n"
"/*-----QPushButton-----*/\n"
"QPushButton\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(84, 84, 84, 255),stop:1 rgba(59, 59, 59, 255));\n"
"    color: #ffffff;\n"
"    min-width: 80px;\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-radius: 3px;\n"
"    border-color: #051a39;\n"
"    padding: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::flat\n"
"{\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::disabled\n"
"{\n"
"    background-color: #404040;\n"
"    color: #656565;\n"
"    border-color: #051a39;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::hover\n"
"{\n"
"    background-color: rgba(183, 134, 32, 20%);\n"
"    border: 1px solid #b78620;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(74, 74, 74, 255),stop:1 rgba(49, 49, 49, 255));\n"
"    border: 1px solid #b78620;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::checked\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(74, 74, 74, 255),stop:1 rgba(49, 49, 49, 255));\n"
"    border: 1px solid #222;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QLineEdit-----*/\n"
"QLineEdit\n"
"{\n"
"    background-color: #131313;\n"
"    color : #eee;\n"
"    border: 1px solid #343434;\n"
"    border-radius: 2px;\n"
"    padding: 3px;\n"
"    padding-left: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QPlainTExtEdit-----*/\n"
"QPlainTextEdit\n"
"{\n"
"    background-color: #131313;\n"
"    color : #eee;\n"
"    border: 1px solid #343434;\n"
"    border-radius: 2px;\n"
"    padding: 3px;\n"
"    padding-left: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QTabBar-----*/\n"
"QTabBar::tab\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(84, 84, 84, 255),stop:1 rgba(59, 59, 59, 255));\n"
"    color: #ffffff;\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: #666;\n"
"    border-bottom: none;\n"
"    padding: 5px;\n"
"    padding-left: 15px;\n"
"    padding-right: 15px;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabWidget::pane \n"
"{\n"
"    background-color: red;\n"
"    border: 1px solid #666;\n"
"    top: 1px;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:last\n"
"{\n"
"    margin-right: 0; \n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:first:!selected\n"
"{\n"
"    background-color: #0c0c0d;\n"
"    margin-left: 0px;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:!selected\n"
"{\n"
"    color: #b1b1b1;\n"
"    border-bottom-style: solid;\n"
"    background-color: #0c0c0d;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:selected\n"
"{\n"
"    margin-bottom: 0px;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:!selected:hover\n"
"{\n"
"    border-top-color: #b78620;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QComboBox-----*/\n"
"QComboBox\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(84, 84, 84, 255),stop:1 rgba(59, 59, 59, 255));\n"
"    border: 1px solid #000;\n"
"    padding-left: 6px;\n"
"    color: #ffffff;\n"
"    height: 20px;\n"
"\n"
"}\n"
"\n"
"\n"
"QComboBox::disabled\n"
"{\n"
"    background-color: #404040;\n"
"    color: #656565;\n"
"    border-color: #051a39;\n"
"\n"
"}\n"
"\n"
"\n"
"QComboBox:on\n"
"{\n"
"    background-color: #b78620;\n"
"    color: #000;\n"
"\n"
"}\n"
"\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    background-color: #383838;\n"
"    color: #ffffff;\n"
"    border: 1px solid black;\n"
"    selection-background-color: #b78620;\n"
"    outline: 0;\n"
"\n"
"}\n"
"\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(57, 57, 57, 255),stop:1 rgba(50, 50, 50, 255));\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"    border-left-width: 1px;\n"
"    border-left-color: black;\n"
"    border-left-style: solid; \n"
"\n"
"}\n"
"\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"    image: url(://arrow-down.png);\n"
"    width: 8px;\n"
"    height: 8px;\n"
"}\n"
"\n"
"\n"
"/*-----QSpinBox & QDateTimeEdit-----*/\n"
"QSpinBox,\n"
"QDateTimeEdit \n"
"{\n"
"    background-color: #131313;\n"
"    color : #eee;\n"
"    border: 1px solid #343434;\n"
"    padding: 3px;\n"
"    padding-left: 5px;\n"
"    border-radius : 2px;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::up-button, \n"
"QDateTimeEdit::up-button\n"
"{\n"
"    border-top-right-radius:2px;\n"
"    background-color: #777777;\n"
"    width: 16px; \n"
"    border-width: 1px;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::up-button:hover, \n"
"QDateTimeEdit::up-button:hover\n"
"{\n"
"    background-color: #585858;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::up-button:pressed, \n"
"QDateTimeEdit::up-button:pressed\n"
"{\n"
"    background-color: #252525;\n"
"    width: 16px; \n"
"    border-width: 1px;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::up-arrow,\n"
"QDateTimeEdit::up-arrow\n"
"{\n"
"    image: url(://arrow-up.png);\n"
"    width: 7px;\n"
"    height: 7px;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::down-button, \n"
"QDateTimeEdit::down-button\n"
"{\n"
"    border-bottom-right-radius:2px;\n"
"    background-color: #777777;\n"
"    width: 16px; \n"
"    border-width: 1px;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::down-button:hover, \n"
"QDateTimeEdit::down-button:hover\n"
"{\n"
"    background-color: #585858;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::down-button:pressed, \n"
"QDateTimeEdit::down-button:pressed\n"
"{\n"
"    background-color: #252525;\n"
"    width: 16px; \n"
"    border-width: 1px;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::down-arrow,\n"
"QDateTimeEdit::down-arrow\n"
"{\n"
"    image: url(://arrow-down.png);\n"
"    width: 7px;\n"
"    height: 7px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QGroupBox-----*/\n"
"QGroupBox \n"
"{\n"
"    border: 1px solid;\n"
"    border-color: #666666;\n"
"    border-radius: 5px;\n"
"    margin-top: 20px;\n"
"\n"
"}\n"
"\n"
"\n"
"QGroupBox::title  \n"
"{\n"
"    background-color: transparent;\n"
"    color: #eee;\n"
"    subcontrol-origin: margin;\n"
"    padding: 5px;\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QHeaderView-----*/\n"
"QHeaderView::section\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(60, 60, 60, 255),stop:1 rgba(50, 50, 50, 255));\n"
"    border: 1px solid #000;\n"
"    color: #fff;\n"
"    text-align: left;\n"
"    padding: 4px;\n"
"    \n"
"}\n"
"\n"
"\n"
"QHeaderView::section:disabled\n"
"{\n"
"    background-color: #525251;\n"
"    color: #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section:checked\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(60, 60, 60, 255),stop:1 rgba(50, 50, 50, 255));\n"
"    color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section::vertical::first,\n"
"QHeaderView::section::vertical::only-one\n"
"{\n"
"    border-top: 1px solid #353635;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section::vertical\n"
"{\n"
"    border-top: 1px solid #353635;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section::horizontal::first,\n"
"QHeaderView::section::horizontal::only-one\n"
"{\n"
"    border-left: 1px solid #353635;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section::horizontal\n"
"{\n"
"    border-left: 1px solid #353635;\n"
"\n"
"}\n"
"\n"
"\n"
"QTableCornerButton::section\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(60, 60, 60, 255),stop:1 rgba(50, 50, 50, 255));\n"
"    border: 1px solid #000;\n"
"    color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QTreeWidget-----*/\n"
"QTreeView\n"
"{\n"
"    show-decoration-selected: 1;\n"
"    alternate-background-color: #3a3a3a;\n"
"    selection-color: #fff;\n"
"    background-color: #2d2d2d;\n"
"    border: 1px solid gray;\n"
"    padding-top : 5px;\n"
"    color: #fff;\n"
"    font: 8pt;\n"
"\n"
"}\n"
"\n"
"\n"
"QTreeView::item:selected\n"
"{\n"
"    color:#fff;\n"
"    background-color: #b78620;\n"
"    border-radius: 0px;\n"
"\n"
"}\n"
"\n"
"\n"
"QTreeView::item:!selected:hover\n"
"{\n"
"    background-color: #262626;\n"
"    border: none;\n"
"    color: white;\n"
"\n"
"}\n"
"\n"
"\n"
"QTreeView::branch:has-children:!has-siblings:closed,\n"
"QTreeView::branch:closed:has-children:has-siblings \n"
"{\n"
"    image: url(://tree-closed.png);\n"
"\n"
"}\n"
"\n"
"\n"
"QTreeView::branch:open:has-children:!has-siblings,\n"
"QTreeView::branch:open:has-children:has-siblings  \n"
"{\n"
"    image: url(://tree-open.png);\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QListView-----*/\n"
"QListView \n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(83, 83, 83, 255),stop:0.293269 rgba(81, 81, 81, 255),stop:0.634615 rgba(79, 79, 79, 255),stop:1 rgba(83, 83, 83, 255));\n"
"    border : none;\n"
"    color: white;\n"
"    show-decoration-selected: 1; \n"
"    outline: 0;\n"
"    border: 1px solid gray;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView::disabled \n"
"{\n"
"    background-color: #656565;\n"
"    color: #1b1b1b;\n"
"    border: 1px solid #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView::item \n"
"{\n"
"    background-color: #2d2d2d;\n"
"    padding: 1px;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView::item:alternate \n"
"{\n"
"    background-color: #3a3a3a;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView::item:selected \n"
"{\n"
"    background-color: #b78620;\n"
"    border: 1px solid #b78620;\n"
"    color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView::item:selected:!active \n"
"{\n"
"    background-color: #b78620;\n"
"    border: 1px solid #b78620;\n"
"    color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView::item:selected:active \n"
"{\n"
"    background-color: #b78620;\n"
"    border: 1px solid #b78620;\n"
"    color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView::item:hover {\n"
"    background-color: #262626;\n"
"    border: none;\n"
"    color: white;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QCheckBox-----*/\n"
"QCheckBox\n"
"{\n"
"    background-color: transparent;\n"
"    color: lightgray;\n"
"    border: none;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator\n"
"{\n"
"    background-color: #323232;\n"
"    border: 1px solid darkgray;\n"
"    width: 12px;\n"
"    height: 12px;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator:checked\n"
"{\n"
"    image:url(\"./ressources/check.png\");\n"
"    background-color: #b78620;\n"
"    border: 1px solid #3a546e;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator:unchecked:hover\n"
"{\n"
"    border: 1px solid #b78620; \n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::disabled\n"
"{\n"
"    color: #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator:disabled\n"
"{\n"
"    background-color: #656565;\n"
"    color: #656565;\n"
"    border: 1px solid #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QRadioButton-----*/\n"
"QRadioButton \n"
"{\n"
"    color: lightgray;\n"
"    background-color: transparent;\n"
"\n"
"}\n"
"\n"
"\n"
"QRadioButton::indicator::unchecked:hover \n"
"{\n"
"    background-color: lightgray;\n"
"    border: 2px solid #b78620;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"\n"
"QRadioButton::indicator::checked \n"
"{\n"
"    border: 2px solid #b78620;\n"
"    border-radius: 6px;\n"
"    background-color: rgba(183,134,32,20%);  \n"
"    width: 9px; \n"
"    height: 9px; \n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QSlider-----*/\n"
"QSlider::groove:horizontal \n"
"{\n"
"    background-color: transparent;\n"
"    height: 3px;\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::sub-page:horizontal \n"
"{\n"
"    background-color: #b78620;\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::add-page:horizontal \n"
"{\n"
"    background-color: #131313;\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::handle:horizontal \n"
"{\n"
"    background-color: #b78620;\n"
"    width: 14px;\n"
"    margin-top: -6px;\n"
"    margin-bottom: -6px;\n"
"    border-radius: 6px;\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::handle:horizontal:hover \n"
"{\n"
"    background-color: #d89e25;\n"
"    border-radius: 6px;\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::sub-page:horizontal:disabled \n"
"{\n"
"    background-color: #bbb;\n"
"    border-color: #999;\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::add-page:horizontal:disabled \n"
"{\n"
"    background-color: #eee;\n"
"    border-color: #999;\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::handle:horizontal:disabled \n"
"{\n"
"    background-color: #eee;\n"
"    border: 1px solid #aaa;\n"
"    border-radius: 3px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QScrollBar-----*/\n"
"QScrollBar:horizontal\n"
"{\n"
"    border: 1px solid #222222;\n"
"    background-color: #3d3d3d;\n"
"    height: 15px;\n"
"    margin: 0px 16px 0 16px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::handle:horizontal\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(97, 97, 97, 255),stop:1 rgba(90, 90, 90, 255));\n"
"    border: 1px solid #2d2d2d;\n"
"    min-height: 20px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:horizontal\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(97, 97, 97, 255),stop:1 rgba(90, 90, 90, 255));\n"
"    border: 1px solid #2d2d2d;\n"
"    width: 15px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::sub-line:horizontal\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(97, 97, 97, 255),stop:1 rgba(90, 90, 90, 255));\n"
"    border: 1px solid #2d2d2d;\n"
"    width: 15px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::right-arrow:horizontal\n"
"{\n"
"    image: url(://arrow-right.png);\n"
"    width: 6px;\n"
"    height: 6px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::left-arrow:horizontal\n"
"{\n"
"    image: url(://arrow-left.png);\n"
"    width: 6px;\n"
"    height: 6px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"    background: none;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar:vertical\n"
"{\n"
"    background-color: #3d3d3d;\n"
"    width: 16px;\n"
"    border: 1px solid #2d2d2d;\n"
"    margin: 16px 0px 16px 0px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::handle:vertical\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(97, 97, 97, 255),stop:1 rgba(90, 90, 90, 255));\n"
"    border: 1px solid #2d2d2d;\n"
"    min-height: 20px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(97, 97, 97, 255),stop:1 rgba(90, 90, 90, 255));\n"
"    border: 1px solid #2d2d2d;\n"
"    height: 15px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::sub-line:vertical\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(97, 97, 97, 255),stop:1 rgba(90, 90, 90, 255));\n"
"    border: 1px solid #2d2d2d;\n"
"    height: 15px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::up-arrow:vertical\n"
"{\n"
"    image: url(://arrow-up.png);\n"
"    width: 6px;\n"
"    height: 6px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::down-arrow:vertical\n"
"{\n"
"    image: url(://arrow-down.png);\n"
"    width: 6px;\n"
"    height: 6px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"{\n"
"    background: none;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QProgressBar-----*/\n"
"QProgressBar\n"
"{\n"
"    border: 1px solid #666666;\n"
"    text-align: center;\n"
"    color: #000;\n"
"    font-weight: bold;\n"
"\n"
"}\n"
"\n"
"\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: #b78620;\n"
"    width: 30px;\n"
"    margin: 0.5px;\n"
"\n"
"}\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 200))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.CineSpeed_Label = QtWidgets.QLabel(self.groupBox)
        self.CineSpeed_Label.setObjectName("CineSpeed_Label")
        self.horizontalLayout.addWidget(self.CineSpeed_Label)
        self.CineSpeed_Slider = QtWidgets.QSlider(self.groupBox)
        self.CineSpeed_Slider.setOrientation(QtCore.Qt.Horizontal)
        self.CineSpeed_Slider.setObjectName("CineSpeed_Slider")
        self.horizontalLayout.addWidget(self.CineSpeed_Slider)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.SelectChannel_ComboBox = QtWidgets.QComboBox(self.groupBox)
        self.SelectChannel_ComboBox.setEditable(False)
        self.SelectChannel_ComboBox.setObjectName("SelectChannel_ComboBox")
        self.SelectChannel_ComboBox.addItem("")
        self.SelectChannel_ComboBox.addItem("")
        self.SelectChannel_ComboBox.addItem("")
        self.horizontalLayout_2.addWidget(self.SelectChannel_ComboBox)
        self.SignalColor_ComboBox = QtWidgets.QComboBox(self.groupBox)
        self.SignalColor_ComboBox.setObjectName("SignalColor_ComboBox")
        self.SignalColor_ComboBox.addItem("")
        self.SignalColor_ComboBox.addItem("")
        self.SignalColor_ComboBox.addItem("")
        self.horizontalLayout_2.addWidget(self.SignalColor_ComboBox)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.BrowseFiles_PushButton = QtWidgets.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Myanmar Text")
        font.setBold(True)
        font.setWeight(75)
        self.BrowseFiles_PushButton.clicked.connect(self.browsefiles)
        self.BrowseFiles_PushButton.setFont(font)
        self.BrowseFiles_PushButton.setObjectName("BrowseFiles_PushButton")
        self.verticalLayout.addWidget(self.BrowseFiles_PushButton)
        self.horizontalLayout_6.addLayout(self.verticalLayout)
        self.Hide_GroupBox = QtWidgets.QGroupBox(self.groupBox)
        self.Hide_GroupBox.setObjectName("Hide_GroupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.Hide_GroupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.Channel1_CheckBox = QtWidgets.QCheckBox(self.Hide_GroupBox)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        self.Channel1_CheckBox.setFont(font)
        self.Channel1_CheckBox.setObjectName("Channel1_CheckBox")
        self.verticalLayout_3.addWidget(self.Channel1_CheckBox)
        self.Channel2_CheckBox = QtWidgets.QCheckBox(self.Hide_GroupBox)
        self.Channel2_CheckBox.setObjectName("Channel2_CheckBox")
        self.verticalLayout_3.addWidget(self.Channel2_CheckBox)
        self.Channel3_CheckBox = QtWidgets.QCheckBox(self.Hide_GroupBox)
        self.Channel3_CheckBox.setObjectName("Channel3_CheckBox")
        self.verticalLayout_3.addWidget(self.Channel3_CheckBox)
        self.horizontalLayout_6.addWidget(self.Hide_GroupBox)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setBold(True)
        font.setWeight(75)
        self.Rename_PushButton = QtWidgets.QPushButton(self.groupBox)
       
        self.Rename_PushButton.setFont(font)
        self.Rename_PushButton.setObjectName("Rename_PushButton")
        #self.Rename_PushButton.setText("Rename")
        self.Rename_PushButton.clicked.connect(self.SignalNames)
        self.verticalLayout_2.addWidget(self.Rename_PushButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.Channel1_Label = QtWidgets.QLabel(self.groupBox)
        self.Channel1_Label.setObjectName("Channel1_Label")
        self.horizontalLayout_3.addWidget(self.Channel1_Label)
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_3.addWidget(self.lineEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.Channnel_Label = QtWidgets.QLabel(self.groupBox)
        self.Channnel_Label.setObjectName("Channnel_Label")
        self.horizontalLayout_4.addWidget(self.Channnel_Label)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_4.addWidget(self.lineEdit_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.Channel3_Label = QtWidgets.QLabel(self.groupBox)
        self.Channel3_Label.setObjectName("Channel3_Label")
        self.horizontalLayout_5.addWidget(self.Channel3_Label)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_5.addWidget(self.lineEdit_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6.addLayout(self.verticalLayout_2)
        self.ProcessControl_GroupBox = QtWidgets.QGroupBox(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.ProcessControl_GroupBox.setFont(font)
        self.ProcessControl_GroupBox.setStyleSheet("color: rgb(85, 0, 0);")
        self.ProcessControl_GroupBox.setFlat(False)
        self.ProcessControl_GroupBox.setCheckable(False)
        self.ProcessControl_GroupBox.setObjectName("ProcessControl_GroupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.ProcessControl_GroupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.Play_PushButton = QtWidgets.QPushButton(self.ProcessControl_GroupBox)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        #self.Play_PushButton = QtWidgets.QPushButton(self.ProcessControl_GroupBox)
        self.Play_PushButton.setFont(font)
        self.Play_PushButton.setStyleSheet("color: rgb(255, 255, 255);")
        self.Play_PushButton.setObjectName("Play_PushButton")
        self.Play_PushButton.clicked.connect(self.playbutton)
        self.gridLayout.addWidget(self.Play_PushButton, 0, 0, 1, 1)
        self.Pause_PushButton = QtWidgets.QPushButton(self.ProcessControl_GroupBox)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.Pause_PushButton.clicked.connect(self.pausebutton)
        self.Pause_PushButton.setFont(font)
        self.Pause_PushButton.setStyleSheet("color: rgb(255, 255, 255);")
        self.Pause_PushButton.setObjectName("Pause_PushButton")
        self.gridLayout.addWidget(self.Pause_PushButton, 0, 1, 1, 1)
        self.Report_PushButton = QtWidgets.QPushButton(self.ProcessControl_GroupBox)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.Report_PushButton.clicked.connect(self.exportfiles)
        self.Report_PushButton.setFont(font)
        self.Report_PushButton.setStyleSheet("color: rgb(255, 255, 255);")
        self.Report_PushButton.setObjectName("Report_PushButton")
        self.gridLayout.addWidget(self.Report_PushButton, 1, 0, 1, 2)
        self.horizontalLayout_6.addWidget(self.ProcessControl_GroupBox)
        self.gridLayout_5.addLayout(self.horizontalLayout_6, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox, 1, 1, 1, 1)
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.ZoomIn_PushButton = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setBold(True)
        font.setWeight(75)
        self.ZoomIn_PushButton.clicked.connect(self.ZoomIn)
        
        self.ZoomIn_PushButton.setFont(font)
        self.ZoomIn_PushButton.setStyleSheet("color: rgb(255, 255, 255);")
        self.ZoomIn_PushButton.setObjectName("ZoomIn_PushButton")
        self.horizontalLayout_7.addWidget(self.ZoomIn_PushButton)
        self.ZoomOut_PushButton = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setBold(True)
        font.setWeight(75)
        self.ZoomOut_PushButton.setFont(font)
        self.ZoomOut_PushButton.setStyleSheet("")
        self.ZoomOut_PushButton.setObjectName("ZoomOut_PushButton")
        self.ZoomOut_PushButton.clicked.connect(self.ZoomOut)
        self.horizontalLayout_7.addWidget(self.ZoomOut_PushButton)
        self.verticalLayout_4.addLayout(self.horizontalLayout_7)
        self.line = QtWidgets.QFrame(self.layoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_4.addWidget(self.line)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        self.Figure_groupBox = QtWidgets.QGroupBox(self.layoutWidget)
        self.Figure_groupBox.setObjectName("Figure_groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.Figure_groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.Figure_Widget = PlotWidget(self.Figure_groupBox)
        self.Figure_Widget.setObjectName("Figure_Widget")
        self.gridLayout_2.addWidget(self.Figure_Widget, 0, 0, 1, 1)
        self.verticalLayout_5.addWidget(self.Figure_groupBox)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)
        self.Figure_Slider = QtWidgets.QSlider(self.layoutWidget)
        self.Figure_Slider.setOrientation(QtCore.Qt.Horizontal)
        self.Figure_Slider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.Figure_Slider.setObjectName("Figure_Slider")
        self.Figure_Slider.setMinimum(0)
        self.Figure_Slider.sliderMoved.connect(self.ChangeValue)
        self.Figure_Slider.valueChanged.connect(self.ChangeValue)
        self.verticalLayout_6.addWidget(self.Figure_Slider)
        self.Spectrogram_GroupBox = QtWidgets.QGroupBox(self.splitter)
        self.Spectrogram_GroupBox.setObjectName("Spectrogram_GroupBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.Spectrogram_GroupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.Spectrogram_Widget = pyqtgraph.GraphicsLayoutWidget(self.Spectrogram_GroupBox)
        self.Spectrogram_Widget.setObjectName("Spectrogram_Widget")
        self.gridLayout_3.addWidget(self.Spectrogram_Widget, 0, 0, 1, 3)
        #self.SpectrogramSelectChannel_Label = QtWidgets.QLabel(self.Spectrogram_GroupBox)
        #self.SpectrogramSelectChannel_Label.setStyleSheet("\n""font: 7pt \"MS Shell Dlg 2\";")
       # self.SpectrogramSelectChannel_Label.setObjectName("SpectrogramSelectChannel_Label")
        #self.gridLayout_3.addWidget(self.SpectrogramSelectChannel_Label, 1, 0, 1, 1)
        self.comboBox_3 = QtWidgets.QComboBox(self.Spectrogram_GroupBox)
        self.comboBox_3.setEditable(False)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.gridLayout_3.addWidget(self.comboBox_3, 1, 1, 1, 1)
        self.ShowSpectrogram = QtWidgets.QPushButton(self.Spectrogram_GroupBox)
        self.ShowSpectrogram.setObjectName("showSpectrogram")
        self.ShowSpectrogram.setText('Show')
        self.ShowSpectrogram.clicked.connect(self.spectrogram)
        self.gridLayout_3.addWidget(self.ShowSpectrogram, 1, 2, 1, 1)
        self.gridLayout_4.addWidget(self.splitter, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1094, 28))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pencolors_channels=['r','r','r']
        self.comboBox_3.activated.connect(self.spectrogram)
        self.Hover = QtWidgets.QStackedWidget(self.Figure_Widget)
        self.Hover.setGeometry(QtCore.QRect(0,0, 75,61))
        self.Ch1Label = QtWidgets.QLabel(self.Hover)
        self.Ch1Label.setGeometry(QtCore.QRect(5,0,71,16))
        self.Ch1Label.setText('Channel 1')
        self.Ch2Label = QtWidgets.QLabel(self.Hover)
        self.Ch2Label.setGeometry(QtCore.QRect(5,20,71,16))
        self.Ch2Label.setText('Channel 2')
        self.Ch3Label = QtWidgets.QLabel(self.Hover)
        self.Ch3Label.setGeometry(QtCore.QRect(5,40,71,16))
        self.Ch3Label.setText('Channel 3')
        self.Palette = QtWidgets.QComboBox(self.Spectrogram_GroupBox)
        self.Palette.setGeometry(QtCore.QRect(10,362,192,22))
        self.Palette.addItem('Viridis')
        self.Palette.addItem('Plasma')
        self.Palette.addItem('Inferno')
        self.Palette.addItem('Magma')
        self.Palette.addItem('Cividis')
        self.Palette.activated.connect(self.spectrogram)
        self.gridLayout_3.addWidget(self.Palette, 1, 0, 1, 1)


        ###############Functions#################
        
    def browsefiles(self): ###Browse Button###
        global selected
        selected = str(self.SelectChannel_ComboBox.currentText())
        global fname
        fname=QFileDialog.getOpenFileName(None, str("Browse Files"), None, str("Signal Files (*.mat)"))
        signal = scipy.io.loadmat(str(fname[0]))
        xaxis=signal['val']
        xnew=np.array(xaxis)
        xnew=xnew.flatten()
        xnewer=np.arange(1,len(xnew)+1,1)
        yaxis=signal['val']
        global ynew
        ynew=np.array(yaxis)
        ynew=ynew.flatten()
        global xxis1
        global yxis1
        global xxis2
        global yxis2
        global xxis
        global yxis
        if int(self.SelectChannel_ComboBox.currentIndex()) == 0:
            xxis = xnewer
            yxis = ynew
            self.ChannelOneSelected = True
        elif int(self.SelectChannel_ComboBox.currentIndex()) == 1:
            xxis1 = xnewer
            yxis1 = ynew
            self.ChannelTwoSelected = True
        elif int(self.SelectChannel_ComboBox.currentIndex()) == 2:
            xxis2 = xnewer
            yxis2 = ynew
            self.ChannelThreeSelected=True
        
        self.status_zoom = 0
        self.status_slider = 0
        self.update_plot()
        self.timer = QtCore.QTimer()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.update_plot)
        self.timer.start()
        
                                   ################ Update the plot ###############
    def update_plot(self):   
        speed = int(self.CineSpeed_Slider.value())
        self.pencolors=['r','g','b']
        self.labelcolors=['color: red', 'color: green','color: blue']
        global colorindex
        if self.SelectChannel_ComboBox.currentIndex()==0:
            colorindex = int(self.SignalColor_ComboBox.currentIndex())
            self.pencolors_channels[0]=self.pencolors[colorindex]
            self.Ch1Label.setStyleSheet(str(self.labelcolors[colorindex]))
        elif self.SelectChannel_ComboBox.currentIndex()==1:
            colorindex = int(self.SignalColor_ComboBox.currentIndex())
            self.pencolors_channels[1]=self.pencolors[colorindex]
            self.Ch2Label.setStyleSheet(str(self.labelcolors[colorindex]))      
        elif self.SelectChannel_ComboBox.currentIndex()==2:
            colorindex = int(self.SignalColor_ComboBox.currentIndex())
            self.pencolors_channels[2]=self.pencolors[colorindex]
            self.Ch3Label.setStyleSheet(str(self.labelcolors[colorindex]))
        self.Figure_Widget.clear()
        self.Figure_Widget.setYRange(np.min(yxis),np.max(yxis))
        if self.k == 0 :
            self.Figure_Widget.setXRange(0, self.scaling_factor)
        elif self.k >= 600 and self.status_slider == 0  :
            self.Figure_Widget.setXRange(self.scaling_factor_i, self.scaling_factor)
            self.scaling_factor = self.scaling_factor + 10 + int(speed/10)
            self.scaling_factor_i = self.scaling_factor_i + 10 + int(speed/10)
        elif self.size > 0:
            self.Figure_Widget.setXRange((self.int + self.size) , (self.fin +self.size))
        if self.Channel1_CheckBox.isChecked() == False:
            self.plt1 = self.Figure_Widget.plot(xxis[0:self.k], yxis[0:self.k], pen=self.pencolors_channels[0])
        if self.ChannelTwoSelected==True and self.Channel2_CheckBox.isChecked() == False:
            self.plt2 = self.Figure_Widget.plot(xxis1[0:self.k], yxis1[0:self.k], pen=self.pencolors_channels[1])
        if self.ChannelThreeSelected==True and self.Channel3_CheckBox.isChecked() == False:
            self.plt3 = self.Figure_Widget.plot(xxis2[0:self.k], yxis2[0:self.k], pen=self.pencolors_channels[2])
        self.Figure_Slider.setMaximum(self.scaling_factor)
        if self.status_zoom == 0 and self.status_slider == 0  :
            self.k = self.k + 10 + int(speed/10)
        if self.k > np.max(xxis):
            self.timer.stop()
            self.k= 0
            self.scaling_factor = 600
            self.scaling_factor_i= 0
            self.zoom = 1


                    ########### function that changes the labels of the signals in the spectrogram combobox######
    def SignalNames(self):         
        _translate = QtCore.QCoreApplication.translate
        self.chan1name = str(self.lineEdit.text())
        self.chan2name = str(self.lineEdit_2.text())
        self.chan3name = str(self.lineEdit_3.text())
        self.comboBox_3.setItemText(0, _translate("MainWindow", self.chan1name))
        self.comboBox_3.setItemText(1, _translate("MainWindow", self.chan2name))
        self.comboBox_3.setItemText(2, _translate("MainWindow", self.chan3name))
        self.Ch1Label.setText(self.chan1name)
        self.Ch2Label.setText(self.chan2name)
        self.Ch3Label.setText(self.chan3name)
        self.Channel1_CheckBox.setText(self.chan1name)
        self.Channel2_CheckBox.setText(self.chan2name)
        self.Channel3_CheckBox.setText(self.chan3name)
    
                    ########### change value function that changes the value of the horizontal slider to move along x axis###########
    def ChangeValue(self):
        self.status_slider = 1
        self.timer.stop()
        self.size = self.Figure_Slider.value()
        self.update_plot()
    
                    ###########  the function tht pauses the signal  ########## 
    def pausebutton(self):
        self.timer.stop()
                          
                         #####  zoom in function  ########  
    def ZoomIn(self):
        self.timer.stop()
        self.size= 3
        self.status_zoom = 1
        self.status_slider =1
        if self.zoom > 1 :
            self.zoom = self.zoom / 2
            self.fin = self.fin / 2
        elif self.zoom >=0.25 and self.zoom <= 1 :
            self.zoom = self.zoom / 2
            self.fin = self.fin * self.zoom
        self.update_plot() 
                        ##### Zoom out function   ######
    def ZoomOut(self):
        self.timer.stop()
        self.size= 3
        self.status_zoom = 1
        self.status_slider =1
        if self.zoom > 1 :
            self.zoom = self.zoom * 2
            self.fin = self.fin * 2
        elif self.zoom >=0.25 and self.zoom <= 1 :
            self.zoom = self.zoom * 2
            self.fin = self.fin * self.zoom
        self.update_plot()

     
                       ####### Export files function #######
    def exportfiles(self):
        pdfname=QFileDialog.getSaveFileName(None, str("Save PDF"), None, str("PDF Files (*.pdf)"))
        #print(pdfname[0])
        Channel1Max = ['No Data Loaded']
        Channel1Mean = ['No Data Loaded']
        Channel1SD = ['No Data Loaded']
        Channel1Min = ['No Data Loaded']
        Channel1Duration = ['No Data Loaded']
        Channel2Max = ['No Data Loaded']
        Channel2Mean = ['No Data Loaded']
        Channel2SD = ['No Data Loaded']
        Channel2Min = ['No Data Loaded']
        Channel2Duration = ['No Data Loaded']
        Channel3Max = ['No Data Loaded']
        Channel3Mean = ['No Data Loaded']
        Channel3SD = ['No Data Loaded']
        Channel3Min = ['No Data Loaded']
        Channel3Duration = ['No Data Loaded']
        if self.ChannelOneSelected == True:
            Channel1Max = np.amax(yxis)
            Channel1SD = np.std(yxis)
            Channel1Mean = np.mean(yxis)
            Channel1Min = np.min(yxis)
            Channel1Duration = int(len(yxis))
            self.spectrogram()
        if self.ChannelTwoSelected == True:
            Channel2Max = np.amax(yxis1)
            Channel2Mean = np.mean(yxis1)
            Channel2SD = np.std(yxis1)
            Channel2Min = np.min(yxis1)
            Channel2Duration = int(len(yxis1))
            self.spectrogram()
        if self.ChannelThreeSelected == True:
            Channel3Max = np.amax(yxis2)
            Channel3Mean = np.mean(yxis2)
            Channel3SD = np.std(yxis2)
            Channel3Min = np.min(yxis2)
            Channel3Duration = int(len(yxis2))
            self.spectrogram()
        data = (
            ('Channel 1', 'Amplitude: ' + str(Channel1Max), 'Minimum: ' + str(Channel1Min), 'Duration: ' + str(Channel1Duration), 'Standard Deviation: ' + str(Channel1SD), 'Mean: ' + str(Channel1Mean)),
            ('Channel 2', 'Amplitude: ' + str(Channel2Max), 'Minimum: ' + str(Channel2Min), 'Duration: ' + str(Channel2Duration), 'Standard Deviation: ' + str(Channel2SD), 'Mean: ' + str(Channel2Mean)),
            ('Channel 3', 'Amplitude: ' + str(Channel3Max), 'Minimum: ' + str(Channel3Min), 'Duration: ' + str(Channel3Duration), 'Standard Deviation: ' + str(Channel3SD), 'Mean: ' + str(Channel3Mean))
            )
        if pdfname !='':
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size = 18)
            pdf.cell(200, 10, txt = "Report", ln = 1, align = 'C')
            pdf.set_font("Arial", size = 12)
            pdf.cell(200, 10, txt = "Signal Data:", ln = 2, align = 'L')
            pdf.set_font("Arial", size = 8)
            for datum in data:
                for datum2 in datum:
                    pdf.cell(200, 10, str(datum2), ln=2, align = 'C')
            signalexporter = pyqtgraph.exporters.ImageExporter(self.Figure_Widget.plotItem)
            signalexporter.parameters()['width'] = 500
            signalexporter.export('temp1.png')
                 #pdf.image(str("temp1.png"))
            pdf.set_font("Arial", size = 12)
            pdf.cell(200, 10, txt = "Spectrogram", ln = 3, align = 'L')
            #self.spectrogram()
            spectroexporter = pyqtgraph.exporters.ImageExporter(self.Spectrogram_Widget.scene())
            spectroexporter.parameters()['width'] = 300
            spectroexporter.export('temp2.png')
            pdf.image(str("temp2.png"))
            pdf.output(str(pdfname[0]))
                         ###### the function that plots the spectrogram ######
    def spectrogram(self):
        self.check_comboBox_3_index()
        self.Spectrogram_Widget.clear()
        f, t, spectrogram = scipy.signal.spectrogram(yfinal)
        p1 = self.Spectrogram_Widget.addPlot()
        img = pyqtgraph.ImageItem()
        p1.addItem(img)
        hist = pyqtgraph.HistogramLUTItem()
        hist.setImageItem(img)
        #palettearray=["{'mode': 'rgb', 'ticks': [(0.5, (32,145,140, 255)), (1.0, (247,230,33, 255)), (0.0, (69,14,89, 255))]}",
        #print(palettearray[int(self.Palette.currentIndex())])
        if self.Palette.currentIndex()==0:
            hist.gradient.restoreState({'mode': 'rgb',
            'ticks': [(0.5, (32,145,140, 255)),
                    (1.0, (247,230,33, 255)),
                    (0.0, (69,14,89, 255))]})
        if self.Palette.currentIndex()==1:
            hist.gradient.restoreState({'mode': 'rgb',
            'ticks': [(0.5, (203,71,120, 255)),
                    (1.0, (241,245,36, 255)),
                    (0.0, (27,23,141, 255))]})
        if self.Palette.currentIndex()==2:
            hist.gradient.restoreState({'mode': 'rgb',
            'ticks': [(0.5, (189,56,82, 255)),
                    (1.0, (246,250,150, 255)),
                    (0.0, (0, 0, 7, 255))]})
        if self.Palette.currentIndex()==3:
            hist.gradient.restoreState({'mode': 'rgb',
            'ticks': [(0.5, (179,54,122, 255)),
                    (1.0, (252,249,187, 255)),
                    (0.0, (0, 0, 5, 255))]})
        if self.Palette.currentIndex()==4:
            hist.gradient.restoreState({'mode': 'rgb',
            'ticks': [(0.5, (124,123,119, 255)),
                    (1.0, (255,232,67, 255)),
                    (0.0, (0,34,79, 255))]})
        self.Spectrogram_Widget.addItem(hist)
        hist.setLevels(np.min(spectrogram), np.max(spectrogram))
        img.setImage(spectrogram)
       

                        ######  Ffunction that checks which channel in the spectrogram combo-box ########
    def check_comboBox_3_index(self):
        global yfinal
        if self.comboBox_3.currentIndex() == 0:
                yfinal =yxis
        if self.comboBox_3.currentIndex() == 1:
                yfinal =yxis1
        if self.comboBox_3.currentIndex() == 2:
                yfinal =yxis2 
                        ###### PlayButton function###
    def playbutton(self):
        signal = scipy.io.loadmat(str(fname[0]))
        xaxis=signal['val']
        xnew=np.array(xaxis)
        xnew=xnew.flatten()
        xnewer=np.arange(1,len(xnew)+1,1)
        yaxis=signal['val']
        global ynew
        ynew=np.array(yaxis)
        ynew=ynew.flatten()
        if int(self.SelectChannel_ComboBox.currentIndex()) == 0:
            global xxis
            global yxis
            xxis = xnewer
            yxis = ynew
        elif int(self.SelectChannel_ComboBox.currentIndex()) == 1:
            global xxis1
            global yxis1
            xxis1 = xnewer
            yxis1 = ynew
        elif int(self.SelectChannel_ComboBox.currentIndex()) == 2:
            global xxis2
            global yxis2
            xxis2 = xnewer
            yxis2 = ynew
        self.status_zoom = 0
        self.status_slider = 0
        self.update_plot()
        self.timer = QtCore.QTimer()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.update_plot)
        self.timer.start()
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Signal Viewer"))
        self.CineSpeed_Label.setText(_translate("MainWindow", "Cine Speed"))
        self.SelectChannel_ComboBox.setItemText(0, _translate("MainWindow", "Channel 1"))
        self.SelectChannel_ComboBox.setItemText(1, _translate("MainWindow", "Channel 2"))
        self.SelectChannel_ComboBox.setItemText(2, _translate("MainWindow", "Channel 3"))
        self.SignalColor_ComboBox.setItemText(0, _translate("MainWindow", "Red"))
        self.SignalColor_ComboBox.setItemText(1, _translate("MainWindow", "Green"))
        self.SignalColor_ComboBox.setItemText(2, _translate("MainWindow", "Blue"))
        self.BrowseFiles_PushButton.setText(_translate("MainWindow", " Browse Files"))
        self.Hide_GroupBox.setTitle(_translate("MainWindow", "Hide"))
        self.Channel1_CheckBox.setText(_translate("MainWindow", "Channel 1"))
        self.Channel2_CheckBox.setText(_translate("MainWindow", "Channel 2"))
        self.Channel3_CheckBox.setText(_translate("MainWindow", "Channel 3"))
        self.Rename_PushButton.setText(_translate("MainWindow", "Rename"))
        self.Channel1_Label.setText(_translate("MainWindow", "Channel 1"))
        self.Channnel_Label.setText(_translate("MainWindow", "Channel 2"))
        self.Channel3_Label.setText(_translate("MainWindow", "Channel 3"))
        self.ProcessControl_GroupBox.setTitle(_translate("MainWindow", "Process Control"))
        self.Play_PushButton.setText(_translate("MainWindow", "Play"))
        self.Pause_PushButton.setText(_translate("MainWindow", "Pause"))
        self.Report_PushButton.setText(_translate("MainWindow", "Report"))
        self.ZoomIn_PushButton.setText(_translate("MainWindow", "Zoom in"))
        self.ZoomOut_PushButton.setText(_translate("MainWindow", "Zoom out"))
        self.Figure_groupBox.setTitle(_translate("MainWindow", "Signal"))
        self.Spectrogram_GroupBox.setTitle(_translate("MainWindow", "Spectrogram"))
        #self.SpectrogramSelectChannel_Label.setText(_translate("MainWindow", "Select channel"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "Channel 1"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "Channel 2"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "Channel 3"))
        self.ShowSpectrogram.setText(_translate("MainWindow", "Show"))
        

from pyqtgraph import PlotWidget

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

