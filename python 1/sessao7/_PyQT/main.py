"""
PyQT é um toolkit desenvolvido em c++ para desenvolvimento de aplicações graficas. Tambem inclui diversas funcionalidades, como; acessoa  DB, Threads, comunicações de rede, etc
"""

import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QGridLayout

#  QApplication é a classe principal do PyQT, ela é responsavel por gerenciar os eventos e a execução da aplicação

#  QMainWindow é a classe que representa a janela principal da aplicação

#  QPushButton é a classe que representa um botão

#  QWidget é a classe que representa um widget

#  QGridLayout é a classe que representa um layout de grade


# tudo em pyqt é uma classe, e para criar uma classe, basta herdar de uma classe existente



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



# importante ter salvo essa parte do codigo
if __name__ == '__main__':
  qt = QApplication(sys.argv)
  app = App()
  app.show()
  qt.exec()  # antes era qt.exec_(), mas agora no pyqt6 é qt.exec()