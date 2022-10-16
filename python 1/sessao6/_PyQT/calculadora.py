import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QGridLayout, QLineEdit, QSizePolicy


class Calculadora(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Calculadora do Renato')
        self.setFixedSize(400, 400)
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)

        self.display = QLineEdit()
        self.grid.addWidget(self.display, 0, 0, 1, 5)
        self.display.setDisabled(True)
        self.display.setStyleSheet(
            'background: #008000; color: #000; font-size: 30px; border-radius: 30px; border: 2px solid #000;'
        )

        self.display.setSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        self.add_btn(QPushButton('7'), 1, 0, 1, 1,style='background: #494949; border: 1px solid #707070; border-radius: 33px')
        self.add_btn(QPushButton('8'), 1, 1, 1, 1,style='background: #494949; border: 1px solid #707070; border-radius: 33px')
        self.add_btn(QPushButton('9'), 1, 2, 1, 1,style='background: #494949; border: 1px solid #707070; border-radius: 33px')
        self.add_btn(QPushButton('+'), 1, 3, 1, 1)
        self.add_btn(QPushButton('C'), 1, 4, 1, 1, lambda: self.display.setText(
            ''))

        self.add_btn(QPushButton('4'), 2, 0, 1, 1,style='background: #494949; border: 1px solid #707070; border-radius: 33px')
        self.add_btn(QPushButton('5'), 2, 1, 1, 1,style='background: #494949; border: 1px solid #707070; border-radius: 33px')
        self.add_btn(QPushButton('6'), 2, 2, 1, 1,style='background: #494949; border: 1px solid #707070; border-radius: 33px')
        self.add_btn(QPushButton('-'), 2, 3, 1, 1)
        self.add_btn(QPushButton('←'), 2, 4, 1, 1,
                     lambda: self.display.setText(self.display.text()[:-1]))

        self.add_btn(QPushButton('1'), 3, 0, 1, 1,style='background: #494949; border: 1px solid #707070; border-radius: 33px')
        self.add_btn(QPushButton('2'), 3, 1, 1, 1,style='background: #494949; border: 1px solid #707070; border-radius: 33px')
        self.add_btn(QPushButton('3'), 3, 2, 1, 1,style='background: #494949; border: 1px solid #707070; border-radius: 33px')
        self.add_btn(QPushButton('/'), 3, 3, 1, 1)
        self.add_btn(QPushButton('.'), 3, 4, 1, 1)

        self.add_btn(QPushButton(''), 4, 0, 1, 1,style='background: #333333; border: 0px solid #707070; border-radius: 33px')
        self.add_btn(QPushButton('0'), 4, 1, 1, 1,style='background: #494949; border: 1px solid #707070; border-radius: 33px')
        self.add_btn(QPushButton(''), 4, 2, 1, 1,style= 'background: #333333; border: 0px solid #707070; border-radius: 33px')
        self.add_btn(QPushButton('*'), 4, 3, 1, 1)
        self.add_btn(QPushButton('='), 4, 4, 1, 1, self.eval_igual)

        self.setCentralWidget(self.cw)

    def add_btn(self, btn, row, col, rowspan, colspan, funcao=None, style=None):
        self.grid.addWidget(btn, row, col, rowspan, colspan)

        if not funcao:
            btn.clicked.connect(lambda: self.display.setText(
                self.display.text() + btn.text()))
        else:
            btn.clicked.connect(funcao)
        btn.setSizePolicy(QSizePolicy.Policy.Expanding,
                          QSizePolicy.Policy.Expanding)

        if style:
            btn.setStyleSheet(style)

    def eval_igual(self):
        try:
            self.display.setText(str(eval(self.display.text())))
        except Exception as e:
            self.display.setText('conta invalida')


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    calc = Calculadora()
    calc.show()
    qt.exec()
