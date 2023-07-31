import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import tts
import player

editFont = QFont()
editFont.setFamily("Arial")
editFont.setPointSize(16)

btnFont = QFont()
btnFont.setFamily("Arial")
btnFont.setPointSize(14)

class Btn(QPushButton):
    def __init__(self, text, parent):
        super().__init__(text, parent)
        self.resize(160, 60)
        self.setFont(btnFont)

class window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500,180)
        self.setWindowTitle("TTS GUI")
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.initUI()
    
    def initUI(self):
        self.editor = QLineEdit(self)
        self.editor.resize(460, 80)
        self.editor.setFont(editFont)
        self.editor.move(20, 10)

        self.reqBtn = Btn("Speak", self)
        self.reqBtn.move(320, 100)
        self.reqBtn.clicked.connect(self.onReqClick)

        self.clrBtn = Btn("Clear", self)
        self.clrBtn.move(20, 100)
        self.clrBtn.clicked.connect(self.onClrClick)

    def onReqClick(self):
        targetText = self.editor.text()
        tts.req(targetText)
        player.playsound("audio.mp3")

    def onClrClick(self):
        self.editor.clear()
        self.editor.setFocus()

app = QApplication(sys.argv)
win = window()
win.show()
sys.exit(app.exec_())

# speak.req("hello hello")
