import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLCDNumber, QGridLayout,QLabel
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(250, 300)
        self.setWindowTitle("Kликер")
        self.grid_layout = QGridLayout()
        self.setLayout(self.grid_layout)
        self.expression = ''
        self.lcd = QLCDNumber()     
        self.grid_layout.addWidget(self.lcd,0,0,1,3)
        for x in range(1,4):
            for y in range(1,4):
                button = QPushButton(str(str(3*x+y-3)))
                self.grid_layout.addWidget(button, x, y-1)
                button.clicked.connect(self.button_was_clicked)
        self.add_button('+',4,0)
        self.add_button('0',4,1)
        self.add_button('-',4,2)
        self.add_button('*',5,0)
        self.add_button('/',5,1)
        self.add_button('=',5,2)
        self.add_button('C',6,1)

    def button_was_clicked(self):
        sender = self.sender()
        if sender.text() == '=':
            self.lcd.display(eval(self.expression))
            self.expression = str(eval(self.expression))
        elif sender.text() == 'C':
            self.expression = ''
            self.lcd.display(0)
        elif sender.text().isdigit():
            self.lcd.display(int(sender.text()))
            self.expression += sender.text()
        else:
            self.expression += sender.text()

    def add_button(self,operand,x,y):
        button = QPushButton(operand)
        self.grid_layout.addWidget(button, x,y)
        button.clicked.connect(self.button_was_clicked)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()