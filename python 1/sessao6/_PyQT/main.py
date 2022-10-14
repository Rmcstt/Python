"""
PyQT é um toolkit desenvolvido em c++ para desenvolvimento de aplicações graficas. Tambem inclui diversas funcionalidades, como; acessoa  DB, Threads, comunicações de rede, etc
"""

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QGridLayout



class App(QMainWindow):
  def __init__(self, parent=None):
    super().__init__(parent)
    self.cw = QWidget()
    self.grid = QGridLayout(self.cw)

    self.btn = QPushButton('☠︎')
    self.btn.setStyleSheet('font-size: 80px; color: red;')
    self.grid.addWidget(self.btn, 0,0, 1,1)

    self.btn.clicked.connect(self.acao)

    self.setCentralWidget(self.cw)

  def acao(self):
    print('lascou')


if __name__ == '__main__':
  qt = QApplication(sys.argv)
  app = App()
  app.show()
  qt.exec()