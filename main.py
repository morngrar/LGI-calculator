import sys
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtUiTools import QUiLoader

import os

HOST_DIR = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(HOST_DIR, "window.ui")

loader = QUiLoader()
app = QtWidgets.QApplication(sys.argv)
window = loader.load(path, None)

def lg(pre, post):
    d = post - pre
    return d / pre

def lgi(lg_e, lg_c):
    d = lg_e - lg_c
    return d / lg_c

def calcClicked(*args):
    expPre = float(window.expPreInput.value())
    expPost = float(window.expPostInput.value())
    controlPre = float(window.controlPreInput.value())
    controlPost = float(window.controlPostInput.value())

    lg_e = lg(expPre, expPost)
    lg_c = lg(controlPre, controlPost)
    
    window.expLGLabel.setText(str(round(lg_e, 3)))
    window.controlLGLabel.setText(str(round(lg_c, 3)))
    window.LGILabel.setText(str(round(lgi(lg_e, lg_c), 3)))



window.calculateButton.clicked.connect(calcClicked)


window.show()
app.exec_()
