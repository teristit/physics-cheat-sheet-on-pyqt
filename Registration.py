import sqlite3
from PyQt5 import QtCore, uic
from PyQt5.QtWidgets import QMainWindow


class Registration(QMainWindow):
    def __init__(self, color):
        super().__init__()
        self.color = color
        self.contacts()
        self.changepassword = 0

    def contacts(self):
        uic.loadUi('registration.ui', self)
        self.outputtext.setWordWrap(True)
        self.outputtext.setAlignment(QtCore.Qt.AlignJustify | QtCore.Qt.AlignVCenter)
        self.registrationbutton.setStyleSheet("background-color: {}".format(self.color))
        self.registrationbutton.clicked.connect(self.addapasswordrun)
        self.changebutton.setStyleSheet("background-color: {}".format(self.color))
        self.changebutton.clicked.connect(self.changepassword)

    def changepassword(self):
        userlogin = self.linelogin.text()
        userpassword = self.linepassword.text()
        con = sqlite3.connect('passwordssql.sqlite')
        cur = con.cursor()
        if self.changepassword == 0:
            a = cur.execute(
                f"""SELECT login FROM users 
                        WHERE login = '{userlogin}' AND password = '{userpassword}'""").fetchall()
            print(a == None)
            if a:
                self.labellogin.setText('Введите новый пароль')
                self.labelpassword.setText('Повторите пароль')
                self.newlogin = userlogin
                self.changepassword = 1
            else:
                self.outputtext.setText('Неверный пароль или логин')
        else:
            if userlogin == userpassword:
                b = cur.execute(
                    f"""SELECT login FROM users 
                                    WHERE password = '{userpassword}'""").fetchall()

                if not b:
                    cur.execute(
                        f"""UPDATE users SET password = '{userpassword}' 
                        WHERE login = '{self.newlogin}'""")
                    con.commit()
                    self.outputtext.setText('Вы успешно сменили пароль')
                else:
                    self.outputtext.setText(f'Выберите другой пароль. Этот пароль принадлежит пользователю '
                                            f'{str(b).strip("()[],")}')
            else:
                self.outputtext.setText('Пароли не совпадают')
            self.changepassword = 0
            self.labellogin.setText('Логин')
            self.labelpassword.setText('Пароль')
        con.close()


    def addapasswordrun(self):
        userlogin = self.linelogin.text()
        userpassword = self.linepassword.text()
        text = self.addapassword(userlogin, userpassword)
        self.outputtext.setText(text)

    def addapassword(self, login, password):
        if login:
            if password:
                con = sqlite3.connect('passwordssql.sqlite')
                cur = con.cursor()
                userlogin = login
                userpassword = password

                a = cur.execute(
                    f"""SELECT login FROM users 
                    WHERE login = '{userlogin}'""").fetchall()

                b = cur.execute(
                    f"""SELECT login FROM users 
                    WHERE password = '{userpassword}'""").fetchall()

                outtext = ''
                if not a:
                    if not b:
                        cur.execute(f"INSERT INTO users VALUES (?, ?)", (userlogin, userpassword))
                        con.commit()
                        outtext = 'ВСЁ OK'
                    else:
                        outtext = f'Выберите другой пароль. Этот пароль принадлежит пользователю {str(b).strip("()[],")}'
                else:
                    outtext = 'Такой логин существует'

                con.close()
                return outtext
