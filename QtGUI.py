import sys
from PyQt5.QtWidgets import *


# noinspection PyArgumentList
class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        layout = QGridLayout()

        groupbox = QGroupBox("GroupBox Example")
        layout.addWidget(groupbox)

        vbox = QVBoxLayout()
        groupbox.setLayout(vbox)

        radiobutton1 = QRadioButton("RadioButton 1")
        radiobutton1.setChecked(True)
        vbox.addWidget(radiobutton1)

        radiobutton2 = QRadioButton("RadioButton 2")
        vbox.addWidget(radiobutton2)

        groupbox1 = QGroupBox("GroupBox Example")
        layout.addWidget(groupbox1)

        vbox1 = QVBoxLayout()
        groupbox1.setLayout(vbox1)


        radiobutton3 = QRadioButton("RadioButton 1")
        radiobutton3.setChecked(True)
        vbox1.addWidget(radiobutton3)

        radiobutton4 = QRadioButton("RadioButton 2")
        vbox1.addWidget(radiobutton4)

        layout2 = QGridLayout()

        groupbox2 = QGroupBox("GroupBox Example")
        layout2.addWidget(groupbox2)

        vbox2 = QVBoxLayout()
        groupbox2.setLayout(vbox2)

        radiobutton1 = QRadioButton("RadioButton 1")
        radiobutton1.setChecked(True)
        vbox2.addWidget(radiobutton1)

        radiobutton2 = QRadioButton("RadioButton 2")
        vbox2.addWidget(radiobutton2)

        layout3 = QHBoxLayout()
        layout3.addLayout(layout)
        layout3.addSpacing(10)
        layout3.addLayout(layout2)

        self.setLayout(layout3)
        self.setGeometry(300, 300, 500, 400)
        self.setWindowTitle('QSplitter demo')
        self.show()




app = QApplication(sys.argv)
w = Example()
app.exec()
