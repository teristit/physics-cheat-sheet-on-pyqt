from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow


class Contacts(QMainWindow):
    def __init__(self, color):
        super().__init__()
        self.color = color
        self.contacts()

    def contacts(self):
        uic.loadUi('contacts.ui', self)
        self.back.setStyleSheet("background-color: {}".format(self.color))
        self.back.clicked.connect(self.backran)

    def backran(self):
        self.close()