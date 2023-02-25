import csv
from PyQt5 import QtCore, uic
from PyQt5.QtWidgets import QMainWindow

from ApplicationFormula import ApplicationFormula
from Addformula import Addformula


class Application(QMainWindow):
    def __init__(self, color):
        super().__init__()
        self.color = color
        self.application()
        self.formulas = self.opencsv()
        self.combo.addItems(self.formulas.keys())

    def opencsv(self):
        formulas = {}
        try:
            with open('formulas.csv', encoding="utf8") as csvfile:
                reader = csv.reader(csvfile, delimiter=';', quotechar='"')
                for index, row in enumerate(reader):
                    formulas[row[0]] = [row[1], row[2], row[-1]]
            return formulas

        except Exception:
            return formulas

    def application(self):
        uic.loadUi('application.ui', self)
        self.combo.activated[str].connect(self.onActivated)
        try:
            self.addformulabutton.setStyleSheet("background-color: {}".format(self.color))
            self.converterbutton.setStyleSheet("background-color: {}".format(self.color))
            self.addformulabutton.clicked.connect(self.addformula)
            self.converterbutton.clicked.connect(self.calculate)
        except Exception():
            pass

    def calculate(self):
        try:
            if self.formulas[self.keyformula][-1] != self.formulas[self.keyformula][1]:
                self.contacts = ApplicationFormula(self.color, self.formulas[self.keyformula])
                self.contacts.show()
            else:
                self.labelconverter.setText('формула не была конвертирована')
        except Exception:
            pass

    def addformula(self):
        self.contacts = Addformula(self.color)
        self.contacts.show()
        self.close()

    def onActivated(self, text):
        self.keyformula = text
        self.formula.setText(self.formulas[text][0].split(',*')[0])
        self.description.setText(self.formulas[text][1])
        self.description.setWordWrap(True)
        self.description.setAlignment(QtCore.Qt.AlignJustify | QtCore.Qt.AlignVCenter)
