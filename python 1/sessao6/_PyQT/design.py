# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(612, 412)
        self.redimen = QtWidgets.QWidget(MainWindow)
        self.redimen.setObjectName("redimen")
        self.gridLayout = QtWidgets.QGridLayout(self.redimen)
        self.gridLayout.setHorizontalSpacing(4)
        self.gridLayout.setObjectName("gridLayout")
        self.inputAltura = QtWidgets.QLineEdit(self.redimen)
        self.inputAltura.setObjectName("inputAltura")
        self.gridLayout.addWidget(self.inputAltura, 2, 3, 1, 1)
        self.label = QtWidgets.QLabel(self.redimen)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.redimen)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 2, 1, 1)
        self.inputLargura = QtWidgets.QLineEdit(self.redimen)
        self.inputLargura.setObjectName("inputLargura")
        self.gridLayout.addWidget(self.inputLargura, 2, 1, 1, 1)
        self.btnRedimensionar = QtWidgets.QPushButton(self.redimen)
        self.btnRedimensionar.setObjectName("btnRedimensionar")
        self.gridLayout.addWidget(self.btnRedimensionar, 2, 4, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(self.redimen)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 586, 282))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.labelimg = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.labelimg.setText("")
        self.labelimg.setObjectName("labelimg")
        self.gridLayout_2.addWidget(self.labelimg, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 5)
        self.btnEscolherArquivo = QtWidgets.QPushButton(self.redimen)
        self.btnEscolherArquivo.setObjectName("btnEscolherArquivo")
        self.gridLayout.addWidget(self.btnEscolherArquivo, 1, 4, 1, 1)
        self.inputAbrirArquivo = QtWidgets.QLineEdit(self.redimen)
        self.inputAbrirArquivo.setObjectName("inputAbrirArquivo")
        self.gridLayout.addWidget(self.inputAbrirArquivo, 1, 0, 1, 4)
        self.btnSalvar = QtWidgets.QPushButton(self.redimen)
        self.btnSalvar.setObjectName("btnSalvar")
        self.gridLayout.addWidget(self.btnSalvar, 3, 4, 1, 1)
        MainWindow.setCentralWidget(self.redimen)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Redimensionador"))
        self.redimen.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.redimen.setAccessibleName(_translate("MainWindow", "<html><head/><body><p>mainwq</p></body></html>"))
        self.label.setText(_translate("MainWindow", "Largura"))
        self.label_2.setText(_translate("MainWindow", "Altura"))
        self.btnRedimensionar.setText(_translate("MainWindow", "Redimensionar"))
        self.btnEscolherArquivo.setText(_translate("MainWindow", "Escoler arquivo"))
        self.btnSalvar.setText(_translate("MainWindow", "Salvar"))
