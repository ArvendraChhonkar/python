# This Python file uses the following encoding: utf-8
import sys
import os
from pyAesCrypt.crypto import *
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi #loadING the ui file

class Life2Coding(QWidget):
    def __init__(self):
        super(Life2Coding,self).__init__()
        loadUi('user interface.ui',self)
        self.setWindowTitle('Arvendra Chhonkar Encrypting/Decryptind')
        self.en.clicked.connect(self.enc)
        self.dn.clicked.connect(self.dec)
    def enc(self):
      try:
        encryptFile(self.input.text(), self.output.text(),self.pa.text(), 1600)
        self.statuss.setText("Encrypted")
      except:
        self.statuss.setText("Error!!!")

    def dec(self):
      try:
        decryptFile(self.input.text(),self.output.text(),self.pa.text(), 1600)
        self.statuss.setText("decrypted")
      except:
        self.statuss.setText("Error!!!")

app = QApplication(sys.argv)
widget = Life2Coding()
widget.show()
sys.exit(app.exec_())

