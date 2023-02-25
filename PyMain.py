import sqlite3
import sys

from PyQt5 import QtCore, uic
from PyQt5.QtWidgets import QMainWindow, QColorDialog, QApplication

from Application import Application
from Contacts import Contacts
from Feedback import Feedback
from Registration import Registration


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.color = '#d0d3ff'
        self.mainwindow()

    def mainwindow(self):
        uic.loadUi('pymain.ui', self) # создает главное окно
        self.support.setStyleSheet("background-color: {}".format(self.color))
        self.start.setStyleSheet("background-color: {}".format(self.color))
        self.changcolor.setStyleSheet("background-color: {}".format(self.color))
        self.registrationbutton.setStyleSheet("background-color: {}".format(self.color))
        self.feedbackbutton.setStyleSheet("background-color: {}".format(self.color))
        self.labelcondition.setWordWrap(True)
        self.labelcondition.setAlignment(QtCore.Qt.AlignJustify | QtCore.Qt.AlignVCenter)
        self.support.clicked.connect(self.supportran)
        self.changcolor.clicked.connect(self.changcolorran)
        self.start.clicked.connect(self.startran)
        self.registrationbutton.clicked.connect(self.registration)
        self.feedbackbutton.clicked.connect(self.feedbackrun)

    def feedbackrun(self): # открывает окно для оставления коментариев
        self.feedback = Feedback(self.color)
        self.feedback.show()

    def supportran(self): # открывает окно с контактами техподдержки
        self.contacts = Contacts(self.color)
        self.contacts.show()

    def startran(self): # проверяет прароль
        userlogin = self.linelogin.text()
        userpassword = self.linepassword.text()
        con = sqlite3.connect('passwordssql.sqlite')
        cur = con.cursor()
        a = cur.execute(
            f"""SELECT login FROM users 
            WHERE login = '{userlogin}' AND password = '{userpassword}'""").fetchall()
        con.close()
        if a:
            self.application = Application(self.color)

            self.application.show()
            self.close()

        else:
            self.labelcondition.setText('Неверный пароль или логин')


    def changcolorran(self): # меняет цвет кнопок
        color = QColorDialog.getColor()
        if color.isValid():
            self.color = color.name()
        self.support.setStyleSheet("background-color: {}".format(self.color))
        self.start.setStyleSheet("background-color: {}".format(self.color))
        self.changcolor.setStyleSheet("background-color: {}".format(self.color))
        self.registrationbutton.setStyleSheet("background-color: {}".format(self.color))

    def registration(self): # открывает окно для регистрации
        self.registrationstart = Registration(self.color)
        self.registrationstart.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())
