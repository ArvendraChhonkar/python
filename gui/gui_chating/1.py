import sys
import os 

import socket
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi

soc = socket.socket()

soc.connect(('localhost',999))

class myclass(QWidget):
    def __init__(self):
        super(myclass,self).__init__()
        loadUi('form.ui',self)
        self.setWindowTitle('arvendra')
        self.pushButton.clicked.connect(self.onsendcl)
        #self.sendandrec.keyPressEvent(self, QKeyEvent)
    def onsendcl(self):    
        soc.send(bytes(self.sendtext.text()+"\n",'utf-8'))
        
        self.sendandrec.append('\n'+'you: ' + self.sendtext.text( ) + '\n' + soc.recv(1024).decode())  

app = QApplication(sys.argv)
widget = myclass()
widget.show()
sys.exit(app.exec())           
soc.close()