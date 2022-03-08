import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
import random

class index(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("vistaER_Generica2.ui", self)
        
        self.botonIngresar.clicked.connect(self.ingresarDatos)
    
    def ingresarDatos(self, ):
        print('a')
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = index()
    GUI.show()
    sys.exit(app.exec_())