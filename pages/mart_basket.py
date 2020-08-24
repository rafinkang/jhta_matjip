import tkinter as tk
import sys
from PyQt5.QtWidgets import * 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from classes.DbConn import *


class MartRe(QWidget):
    def __init__(self, parent, params):
        super().__init__()
        self.parent = parent
        self.params = params
        self.initUI(parent)
