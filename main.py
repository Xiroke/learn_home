import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout, QLCDNumber


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.count = 0
        self.resize(300, 300)
        self.setWindowTitle("Кликер")
        button_0 = QPushButton("0", self)
        button_1 = QPushButton("1", self)
        button_2 = QPushButton("2", self)
        button_3 = QPushButton("3", self)
        button_4 = QPushButton("4", self)
        button_5 = QPushButton("5", self)
        button_6 = QPushButton("6", self)
        button_7 = QPushButton("7", self)
        button_8 = QPushButton("8", self)
        button_9 = QPushButton("9", self)
        button_plus = QPushButton("+", self)
        button_del = QPushButton("/", self)
        button_ymn = QPushButton("*", self)
        button_min = QPushButton("-", self)
        button_ravno = QPushButton("=", self)

        button_0.setGeometry(0, 50, 80, 40)
        button_1.setGeometry(100, 50, 80, 40)
        button_2.setGeometry(200, 50, 80, 40)
        button_3.setGeometry(0, 100, 80, 40)
        button_4.setGeometry(100, 100, 80, 40)
        button_5.setGeometry(200, 100, 80, 40)
        button_6.setGeometry(0, 150, 80, 40)
        button_7.setGeometry(100, 150, 80, 40)
        button_8.setGeometry(200, 150, 80, 40)
        button_9.setGeometry(0, 200, 80, 40)
        button_plus.setGeometry(100, 200, 80, 40)
        button_del.setGeometry(200, 200, 80, 40)
        button_ymn.setGeometry(0, 250, 80, 40)
        button_min.setGeometry(100, 250, 80, 40)
        button_ravno.setGeometry(200, 250, 80, 40)

        self.lcd = QLCDNumber(self)
        self.lcd.setGeometry(0,0,300,50)
        vbox = QVBoxLayout()
        vbox.addWidget(button_0)
        vbox.addWidget(button_1)
        vbox.addWidget(button_2)
        vbox.addWidget(button_3)
        vbox.addWidget(button_4)
        vbox.addWidget(button_5)
        vbox.addWidget(button_6)
        vbox.addWidget(button_7)
        vbox.addWidget(button_8)
        vbox.addWidget(button_9)
        vbox.addWidget(button_plus)
        vbox.addWidget(button_del)
        vbox.addWidget(button_ymn)
        vbox.addWidget(button_min)
        vbox.addWidget(button_ravno)

        vbox.addWidget(self.lcd)
        
        button_0.clicked.connect(self.button_was_clicked)
        button_1.clicked.connect(self.button_was_clicked)
        button_2.clicked.connect(self.button_was_clicked)
        button_3.clicked.connect(self.button_was_clicked)
        button_4.clicked.connect(self.button_was_clicked)
        button_5.clicked.connect(self.button_was_clicked)
        button_6.clicked.connect(self.button_was_clicked)
        button_7.clicked.connect(self.button_was_clicked)
        button_8.clicked.connect(self.button_was_clicked)
        button_9.clicked.connect(self.button_was_clicked)
        button_plus.clicked.connect(self.button_was_clicked)
        button_del.clicked.connect(self.button_was_clicked)
        button_ymn.clicked.connect(self.button_was_clicked)
        button_min.clicked.connect(self.button_was_clicked)
        button_ravno.clicked.connect(self.button_was_clicked)
        self.answer = 0
        self.line = ''

    def button_was_clicked(self):
        sender = self.sender()
        if sender.text() == '1':
            self.line += '1'
        elif sender.text() == '2':
            self.line += '2'
        elif sender.text() == '3':
            self.line += '3'
        elif sender.text() == '4':
            self.line += '4'
        elif sender.text() == '5':
            self.line += '5'
        elif sender.text() == '6':
            self.line += '6'
        elif sender.text() == '7':
            self.line += '7'
        elif sender.text() == '8':
            self.line += '8'
        elif sender.text() == '9':
            self.line += '9'
        elif sender.text() == '+':
            self.line += '+'
        elif sender.text() == '-':
            self.line += '-'
        elif sender.text() == '*':
            self.line += '*'
        elif sender.text() == '/':
            self.line += '/'
        elif sender.text() == '=':
            self.answer = eval(self.line)
        
        self.lcd.display(self.answer)




    # def keyPressEvent(self, event):
    #     print(event.text())
    #     if event.text() == '1':
    #         self.count += 1
    #     elif event.text() == '2':
    #         self.count -= 1
    #     elif event.text() == Qt.Key_Escape:
    #         self.close()
    #     self.lcd.display(self.count)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
