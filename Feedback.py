import sqlite3

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow


class Feedback(QMainWindow):
    def __init__(self, color):
        super().__init__()
        self.color = color
        self.feedback()

    def feedback(self):
        uic.loadUi('feedback.ui', self)
        self.feedbackbutton.setStyleSheet("background-color: {}".format(self.color))
        self.feedbackbutton.clicked.connect(self.feedbackran)

    def feedbackran(self):
        con = sqlite3.connect('feedback.sqlite')
        cur = con.cursor()
        userlogin = self.linename.text()
        userpassword = self.linefeedback.text()
        if userlogin:
            if userpassword:
                cur.execute(f"INSERT INTO users VALUES (?, ?)", (userlogin, userpassword))
                con.commit()
        con.close()
