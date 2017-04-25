#!/usr/bin/python
# -*- coding: utf-8 -*-

from settings import *
import nltk
import sys
import textract
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
        

def parseProject(filename):
    text = textract.process(project_directory + filename)
    text = text.decode('utf-8')
    
        
if __name__ == '__main__':
    for candidate in candidates.values():
        text = parsePDF(candidate.get('file'))
        print(text)

    
    #app = QApplication(sys.argv)
    #ex = Window()
    #sys.exit(app.exec_())
