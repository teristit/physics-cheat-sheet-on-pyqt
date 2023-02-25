import csv

from PyQt5 import uic, QtGui
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QLabel


class Addformula(QMainWindow):
    def __init__(self, color):
        super().__init__()
        self.color = color
        self.addformula()

    def addformula(self):  # создает окно
        self.pixmap = QPixmap("fon.jpg")
        self.labelimage = QLabel(self)
        self.labelimage.move(0, 0)
        self.labelimage.resize(1089, 761)
        self.pixmap = self.pixmap.scaled(QSize(1500, 1000), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.labelimage.setPixmap(self.pixmap)
        uic.loadUi('addformula.ui', self)
        self.savebutton.setStyleSheet("background-color: {}".format(self.color))
        self.savebutton.clicked.connect(self.save)
        self.converterbutton.setStyleSheet("background-color: {}".format(self.color))
        self.converterbutton.clicked.connect(self.converter)

    def save(self):
        usertitle = self.title.text()
        userformula = self.formula.text()
        userdescription = self.descriptionformula.text()
        if not usertitle:
            self.labelcondition.setText('ошибка сохранения')
        elif not userformula:
            self.labelcondition.setText('ошибка сохранения')
        elif not userdescription:
            self.labelcondition.setText('ошибка сохранения')
        else:
            repetition = False
            with open('formulas.csv', encoding="utf8") as csvfile:
                reader = csv.reader(csvfile, delimiter=';', quotechar='"')
                for index, row in enumerate(reader):
                    if row:
                        if usertitle == row[0]:
                            print('ok')
                            repetition = True
            if repetition:
                self.labelcondition.setText('повторение')
            else:
                print(1)
                with open('formulas.csv', 'a', newline='') as file:
                    writer = csv.writer(file, delimiter=";")
                    list = []
                    list.append(str(usertitle))
                    list.append(str(userformula))
                    list.append(str(userdescription))
                    writer.writerow(list)
                self.labelcondition.setText('все ок')

    def converter(self):
        self.labelconverter.setText('Эта функция доступна только в платной версии')
        self.labelconverter.setStyleSheet("background-color: yellow; border: 1px solid black;")

    def closeEvent(self, event):
        from Application import Application
        self.application = Application(self.color)
        self.application.show()
