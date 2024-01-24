import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QSlider, QSpinBox, QPushButton, QColorDialog
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        
        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout()
        self.label1 = QLabel("Enter RGB Value")
        self.slider1 = QSlider(Qt.Horizontal)
        self.slider1.setRange(80, 255)
        self.spinbox1 = QSpinBox()
        self.spinbox1.setRange(80, 255)
        #self.button1 = QPushButton('Select Color', self)
        self.colorDisplay1 = QLabel()
        self.colorDisplay1.setText("R: ")
        self.colorDisplay1.setAlignment(Qt.AlignCenter)
        self.colorDisplay1.setStyleSheet("background-color: rgb(255, 255, 255); border: 1px solid black;")

        self.label2 = QLabel("Enter GRGB Value")
        self.slider2 = QSlider(Qt.Horizontal)
        self.slider2.setRange(60, 255)
        self.spinbox2 = QSpinBox()
        self.spinbox2.setRange(60, 255)
        #self.button2 = QPushButton('Select Color', self)
        self.colorDisplay2 = QLabel()
        self.colorDisplay2.setText("G: ")
        self.colorDisplay2.setAlignment(Qt.AlignCenter)
        self.colorDisplay2.setStyleSheet("background-color: rgb(255, 255, 255); border: 1px solid black;")

        self.slider1.valueChanged[int].connect(self.changeValue1)
        self.slider2.valueChanged[int].connect(self.changeValue2)
        self.spinbox1.valueChanged[int].connect(self.changeValue1)
        self.spinbox2.valueChanged[int].connect(self.changeValue2)
        #self.button1.clicked.connect(self.selectColor1)
        #self.button2.clicked.connect(self.selectColor2)

        vbox.addWidget(self.label1)
        vbox.addWidget(self.slider1)
        vbox.addWidget(self.spinbox1)
        #vbox.addWidget(self.button1)
        vbox.addWidget(self.colorDisplay1)

        vbox.addWidget(self.label2)
        vbox.addWidget(self.slider2)
        vbox.addWidget(self.spinbox2)
        #vbox.addWidget(self.button2)
        vbox.addWidget(self.colorDisplay2)

        self.setLayout(vbox)

        self.show()

    def changeValue1(self, value):
        self.spinbox1.setValue(value)
        self.updateColorDisplay1()

    def changeValue2(self, value):
        self.spinbox2.setValue(value)
        self.updateColorDisplay2()
    '''
    def selectColor1(self):
        color = QColorDialog.getColor() # open 윈도우 색상 table.
        if color.isValid():
            self.slider1.setValue(color.red())
            self.spinbox1.setValue(color.red())
            self.updateColorDisplay1()

    def selectColor2(self):
        color = QColorDialog.getColor() # open 윈도우 색상 table.
        if color.isValid():
            self.slider2.setValue(color.green())
            self.spinbox2.setValue(color.green())
            self.updateColorDisplay2()
    '''

    def updateColorDisplay1(self):
        red = self.slider1.value()
        self.colorDisplay1.setText(f"R: {red}")
        self.colorDisplay1.setStyleSheet(f"background-color: rgb({red}, {self.slider1.value()}, 255, 230); border: 1px solid black;")

    def updateColorDisplay2(self):
        green = self.slider2.value()
        self.colorDisplay2.setText(f"G: {green}")
        self.colorDisplay2.setStyleSheet(f"background-color: rgb(255, {green}, {green}, 230); border: 1px solid black;")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())