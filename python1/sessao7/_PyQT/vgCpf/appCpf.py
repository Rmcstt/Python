import sys
from validaCpf import valida_cpf
from geraCpf import gera_cpf

import design

from PyQt6.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt6.QtGui import QPixmap

class GeraValidaCPF(QMainWindow, design.Ui_MainWindow):
  def __init__(self, parent=None):
    super().__init__(parent)
    super().setupUi(self)
    self.btnGeraCPf.clicked.connect(self.gera_cpf)
    self.btnValidaCPF.clicked.connect(self.valida_cpf)

  def gera_cpf(self):
    self.labelRetorno.setText(gera_cpf())

  def valida_cpf(self):
    cpf = self.inputValidaCPF.text()
    self.labelRetorno.setText(str(valida_cpf(cpf)))

if __name__ == '__main__':
  qt = QApplication(sys.argv)
  gera_valida_cpf = GeraValidaCPF()
  gera_valida_cpf.show()
  qt.exec()