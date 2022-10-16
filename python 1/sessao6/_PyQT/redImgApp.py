import sys
from design import *
from PyQt6.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt6.QtGui import QPixmap


class Novo(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.btnEscolherArquivo.clicked.connect(self.abrir_imagem)
        self.btnRedimensionar.clicked.connect(self.redimensionar)
        self.btnSalvar.clicked.connect(self.salvar)
       

    def abrir_imagem(self):
        nome_arquivo, _ = QFileDialog.getOpenFileName(self, 'Abrir arquivo','/Users/renatomota/Desktop', filter='Imagens (*.png *.jpg)')
        if nome_arquivo:
            self.inputAbrirArquivo.setText(nome_arquivo)
            self.original_img = QPixmap(nome_arquivo)
            self.labelimg.setPixmap(QPixmap(nome_arquivo))
            self.labelimg.setScaledContents(True)
            self.inputLargura.setText(str(self.original_img.width()))
            self.inputAltura.setText(str(self.original_img.height()))


    def redimensionar(self):
      largura = int(self.inputLargura.text())
      self.nova_imagem = self.original_img.scaledToWidth(largura)
      self.labelimg.setPixmap(self.nova_imagem)
      self.inputLargura.setText(str(self.nova_imagem.width()))
      self.inputAltura.setText(str(self.nova_imagem.height()))

    def salvar(self):
      nome_arquivo, _ = QFileDialog.getSaveFileName(self, 'Salvar arquivo','/Users/renatomota/Desktop')
      if nome_arquivo:
        self.nova_imagem.save(nome_arquivo + '.jpg', 'jpg')



if __name__ == '__main__':
    qt = QApplication(sys.argv)
    novo = Novo()
    novo.show()
    qt.exec()
