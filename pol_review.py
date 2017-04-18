#!/usr/bin/python

from settings import *
import nltk
import sys
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication

class Window(QWidget):    
    def __init__(self):
        super().__init__()        
        self.initUI()        
        
    def initUI(self):                       
        self.resize(250, 150)
        self.center()
        
        self.setWindowTitle('Projets politiques des candidats à l\'élection présidentielle française de 2017')    
        self.show()
        
        
    def center(self):        
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec_())  

