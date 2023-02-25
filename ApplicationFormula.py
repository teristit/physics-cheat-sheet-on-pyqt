from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow


class ApplicationFormula(QMainWindow):
    def __init__(self, color, formula):
        super().__init__()
        self.color = color
        self.formulas = formula[0].split(',*')
        self.unitsmeasurement = formula[-1].split(',')
        self.prefixes = {'да': 1, 'Г': 1_000_000_000, 'М': 1000_000, 'к': 1000, 'м': 0.001, 'мк': 0.000001}
        self.variable1 = [0, 'да']
        self.variable2 = [0, 'да']
        self.variable3 = [0, 'да']
        self.variable4 = [0, 'да']
        self.prefixesdict = {}
        self.applicationformula()

    def applicationformula(self):
        uic.loadUi('applicationformula.ui', self)
        self.calculatebutton.setStyleSheet("background-color: {}".format(self.color))
        text = self.formulas[0]
        self.labelformula.setText(text)
        self.variablenames = []
        self.formulasdict = {}

        for i in range(len(self.formulas)):
            self.variablenames.append(self.formulas[i].split('=')[0])
            self.formulasdict[self.formulas[i].split('=')[0]] = self.formulas[i].split('=')[1]

        for i in self.unitsmeasurement:
            for j in self.prefixes.keys():
                self.prefixesdict[j + i] = self.prefixes[j]
                if i == 'г':
                    self.prefixesdict[j + i] /= 1000
        self.prefixesdict = self.prefixesdict | self.prefixes
        combovariables1 = []
        for i in self.prefixes.keys():
            combovariables1.append(i + self.unitsmeasurement[0])
        self.combovariable1.addItems(combovariables1)
        combovariables2 = []
        for i in self.prefixes.keys():
            combovariables2.append(i + self.unitsmeasurement[1])
        self.combovariable2.addItems(combovariables2)
        combovariables3 = []
        for i in self.prefixes.keys():
            combovariables3.append(i + self.unitsmeasurement[2])
        self.combovariable3.addItems(combovariables3)
        self.labelvariable1.setText(self.variablenames[0])
        self.labelvariable2.setText(self.variablenames[1])
        self.labelvariable3.setText(self.variablenames[2])

        if len(self.unitsmeasurement) == 4:
            self.labelvariable4.setText(self.variablenames[3])
            self.combovariable4.addItems([i + self.unitsmeasurement[3] for i in self.prefixes.keys()])

        self.calculatebutton.clicked.connect(self.calculate)
        self.slidervariable1.valueChanged.connect(self.variableone)
        self.slidervariable2.valueChanged.connect(self.variabletwo)
        self.slidervariable3.valueChanged.connect(self.variablethree)
        self.slidervariable4.valueChanged.connect(self.variablefour)
        self.combovariable1.activated[str].connect(self.comboone)
        self.combovariable2.activated[str].connect(self.combotwo)
        self.combovariable3.activated[str].connect(self.combothree)
        self.combovariable4.activated[str].connect(self.combofour)
        if len(self.formulasdict) == 3:
            self.labelvariable4.hide()
            self.linevariable4.hide()
            self.slidervariable4.hide()
            self.combovariable4.hide()


    def variableone(self, slider):
        self.variable1[0] = float(slider)
        slider = str(slider)
        self.linevariable1.setText(slider)

    def variabletwo(self, slider):
        self.variable2[0] = float(slider)
        slider = str(slider)
        self.linevariable2.setText(slider)

    def variablethree(self, slider):
        self.variable3[0] = float(slider)
        slider = str(slider)
        self.linevariable3.setText(slider)

    def variablefour(self, slider):
        self.variable4[0] = float(slider)
        slider = str(slider)
        self.linevariable4.setText(slider)

    def comboone(self, slider):
        self.variable1[1] = slider

    def combotwo(self, slider):
        self.variable2[1] = slider

    def combothree(self, slider):
        self.variable3[1] = slider

    def combofour(self, slider):
        self.variable4[1] = slider

    def calculate(self):
        try:
            if len(self.formulasdict) == 3:
                if not self.linevariable1.text():
                    result = self.formulasdict[self.labelvariable1.text()]
                    multiplier = self.prefixesdict[self.variable2[1]]
                    result = result.replace(self.labelvariable2.text(),
                                            str(float(self.linevariable2.text()) * multiplier))
                    multiplier = self.prefixesdict[self.variable3[1]]
                    result = result.replace(self.labelvariable3.text(),
                                            str(float(self.linevariable3.text()) * multiplier))
                    multiplier = self.prefixesdict[self.variable1[1]]
                    result = eval(result)
                    result = str(result / multiplier)
                    self.linevariable1.setText(result)
                elif not self.linevariable2.text():
                    result = self.formulasdict[self.labelvariable2.text()]
                    multiplier = self.prefixesdict[self.variable1[1]]
                    result = result.replace(self.labelvariable1.text(),
                                            str(float(self.linevariable1.text()) * multiplier))
                    multiplier = self.prefixesdict[self.variable3[1]]
                    result = result.replace(self.labelvariable3.text(),
                                            str(float(self.linevariable3.text()) * multiplier))
                    result = eval(result)
                    multiplier = self.prefixesdict[self.variable2[1]]
                    result = str(result / multiplier)
                    self.linevariable2.setText(result)
                else:
                    result = self.formulasdict[self.labelvariable3.text()]
                    multiplier = self.prefixesdict[self.variable1[1]]
                    result = result.replace(self.labelvariable1.text(),
                                            str(float(self.linevariable1.text()) * multiplier))
                    multiplier = self.prefixesdict[self.variable2[1]]
                    result = result.replace(self.labelvariable2.text(),
                                            str(float(self.linevariable2.text()) * multiplier))
                    result = eval(result)
                    multiplier = self.prefixesdict[self.variable3[1]]
                    result = str(result / multiplier)
                    self.linevariable3.setText(result)
            else:

                if not self.linevariable1.text():
                    result = self.formulasdict[self.labelvariable1.text()]
                    multiplier = self.prefixesdict[self.variable2[1]]
                    result = result.replace(self.labelvariable2.text(),
                                            str(float(self.linevariable2.text()) * multiplier))
                    multiplier = self.prefixesdict[self.variable3[1]]
                    result = result.replace(self.labelvariable3.text(),
                                            str(float(self.linevariable3.text()) * multiplier))
                    multiplier = self.prefixesdict[self.variable4[1]]
                    result = result.replace(self.labelvariable4.text(),
                                            str(float(self.linevariable4.text()) * multiplier))
                    result = eval(result)
                    multiplier = self.prefixesdict[self.variable1[1]]
                    result = str(result / multiplier)
                    self.linevariable1.setText(result)
                elif not self.linevariable2.text():
                    result = self.formulasdict[self.labelvariable2.text()]
                    multiplier = self.prefixesdict[self.variable1[1]]
                    result = result.replace(self.labelvariable1.text(),
                                            str(float(self.linevariable1.text()) * multiplier))
                    multiplier = self.prefixesdict[self.variable3[1]]
                    result = result.replace(self.labelvariable3.text(),
                                            str(float(self.linevariable3.text()) * multiplier))
                    multiplier = self.prefixesdict[self.variable4[1]]
                    result = result.replace(self.labelvariable4.text(),
                                            str(float(self.linevariable4.text()) * multiplier))
                    multiplier = self.prefixesdict[self.variable2[1]]
                    result = eval(result)
                    result = str(result / multiplier)
                    self.linevariable1.setText(result)
                elif not self.linevariable2.text():
                    result = self.formulasdict[self.labelvariable4.text()]
                    multiplier = self.prefixesdict[self.variable1[1]]
                    result = result.replace(self.labelvariable1.text(),
                                            str(float(self.linevariable1.text()) * multiplier))
                    multiplier = self.prefixesdict[self.variable3[1]]
                    result = result.replace(self.labelvariable3.text(),
                                            str(float(self.linevariable3.text()) * multiplier))
                    multiplier = self.prefixesdict[self.variable2[1]]
                    result = result.replace(self.labelvariable2.text(),
                                            str(float(self.linevariable2.text()) * multiplier))
                    multiplier = self.prefixesdict[self.variable4[1]]
                    result = eval(result)
                    result = str(result / multiplier)
                    self.linevariable1.setText(result)
                else:
                    result = self.formulasdict[self.labelvariable3.text()]
                    multiplier = self.prefixesdict[self.variable1[1]]
                    result = result.replace(self.labelvariable1.text(),
                                            str(float(self.linevariable1.text()) * multiplier))
                    multiplier = self.prefixesdict[self.variable2[1]]
                    result = result.replace(self.labelvariable2.text(),
                                            str(float(self.linevariable2.text()) * multiplier))
                    multiplier = self.prefixesdict[self.variable4[1]]
                    result = result.replace(self.labelvariable4.text(),
                                            str(float(self.linevariable4.text()) * multiplier))
                    multiplier = self.prefixesdict[self.variable3[1]]
                    result = eval(result)
                    result = str(result / multiplier)
                    self.linevariable1.setText(result)
        except Exception:
            print('ошибка')
