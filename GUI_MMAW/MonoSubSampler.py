# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/eudocio/Dropbox/LingCC/INVESTIGACION-Carlos/DesarrolloDeSoftware/cyanocorax/GUI_MMAW/MonoSubSampler.ui'
#
# Created: Wed Sep 24 17:44:15 2014
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(490, 349)
        self.seleccionarDirectorioOrigen = QtWidgets.QPushButton(Form)
        self.seleccionarDirectorioOrigen.setGeometry(QtCore.QRect(20, 10, 451, 41))
        self.seleccionarDirectorioOrigen.setObjectName("seleccionarDirectorioOrigen")
        self.iniciarProceso = QtWidgets.QPushButton(Form)
        self.iniciarProceso.setGeometry(QtCore.QRect(20, 290, 211, 41))
        self.iniciarProceso.setObjectName("iniciarProceso")
        self.cerrarScript = QtWidgets.QPushButton(Form)
        self.cerrarScript.setGeometry(QtCore.QRect(240, 290, 231, 41))
        self.cerrarScript.setObjectName("cerrarScript")
        self.convertirMono = QtWidgets.QGroupBox(Form)
        self.convertirMono.setGeometry(QtCore.QRect(20, 150, 451, 81))
        self.convertirMono.setObjectName("convertirMono")
        self.canalDerecho = QtWidgets.QRadioButton(self.convertirMono)
        self.canalDerecho.setGeometry(QtCore.QRect(10, 20, 121, 31))
        self.canalDerecho.setObjectName("canalDerecho")
        self.canalIzquierdo = QtWidgets.QRadioButton(self.convertirMono)
        self.canalIzquierdo.setGeometry(QtCore.QRect(160, 20, 121, 31))
        self.canalIzquierdo.setObjectName("canalIzquierdo")
        self.canalesSeparados = QtWidgets.QRadioButton(self.convertirMono)
        self.canalesSeparados.setGeometry(QtCore.QRect(10, 50, 181, 31))
        self.canalesSeparados.setObjectName("canalesSeparados")
        self.canalesPromediados = QtWidgets.QRadioButton(self.convertirMono)
        self.canalesPromediados.setGeometry(QtCore.QRect(300, 20, 141, 31))
        self.canalesPromediados.setObjectName("canalesPromediados")
        self.canalesPromediadosSeparados = QtWidgets.QRadioButton(self.convertirMono)
        self.canalesPromediadosSeparados.setGeometry(QtCore.QRect(200, 50, 251, 31))
        self.canalesPromediadosSeparados.setObjectName("canalesPromediadosSeparados")
        self.resamplear = QtWidgets.QGroupBox(Form)
        self.resamplear.setGeometry(QtCore.QRect(20, 230, 451, 61))
        self.resamplear.setObjectName("resamplear")
        self.decimacion2 = QtWidgets.QRadioButton(self.resamplear)
        self.decimacion2.setGeometry(QtCore.QRect(10, 30, 211, 24))
        self.decimacion2.setObjectName("decimacion2")
        self.decimacion4 = QtWidgets.QRadioButton(self.resamplear)
        self.decimacion4.setGeometry(QtCore.QRect(220, 30, 211, 24))
        self.decimacion4.setObjectName("decimacion4")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(20, 80, 451, 41))
        self.pushButton.setObjectName("pushButton")
        self.directorioOrigen = QtWidgets.QLabel(Form)
        self.directorioOrigen.setGeometry(QtCore.QRect(20, 50, 451, 31))
        self.directorioOrigen.setObjectName("directorioOrigen")
        self.directorioDestino = QtWidgets.QLabel(Form)
        self.directorioDestino.setGeometry(QtCore.QRect(20, 120, 451, 31))
        self.directorioDestino.setObjectName("directorioDestino")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Manipulación e inventariado masivo de archivos wav"))
        self.seleccionarDirectorioOrigen.setText(_translate("Form", "Selecciona el directorio en el que residen los wav"))
        self.iniciarProceso.setText(_translate("Form", "Iniciar proceso"))
        self.cerrarScript.setText(_translate("Form", "Cerrar el script"))
        self.convertirMono.setTitle(_translate("Form", "Convertir a mono"))
        self.canalDerecho.setText(_translate("Form", "Canal derecho"))
        self.canalIzquierdo.setText(_translate("Form", "Canal izquierdo"))
        self.canalesSeparados.setText(_translate("Form", "Archivo para cada canal"))
        self.canalesPromediados.setText(_translate("Form", "Promediar canales"))
        self.canalesPromediadosSeparados.setText(_translate("Form", "Archivo por cada canal y promedio"))
        self.resamplear.setTitle(_translate("Form", "Resamplear (decimar)"))
        self.decimacion2.setText(_translate("Form", "Reducir muestreo a la mitad"))
        self.decimacion4.setText(_translate("Form", "Reducir muestreo a un cuarto"))
        self.pushButton.setText(_translate("Form", "Seleccionar el directorio de destino"))
        self.directorioOrigen.setText(_translate("Form", "Directorio seleccionado: "))
        self.directorioDestino.setText(_translate("Form", "Directorio seleccionado: "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

