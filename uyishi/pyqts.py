from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")

        self.lbl = QLabel("")

        self.btn_7 = QPushButton("7")
        self.btn_8 = QPushButton("8")
        self.btn_9 = QPushButton("9")
        self.btn_div = QPushButton("/")
        self.btn_4 = QPushButton("4")
        self.btn_5 = QPushButton("5")
        self.btn_6 = QPushButton("6")
        self.btn_mul = QPushButton("*")
        self.btn_1 = QPushButton("1") 
        self.btn_2 = QPushButton("2")
        self.btn_3 = QPushButton("3")
        self.btn_min = QPushButton("-")
        self.btn_c = QPushButton("C")
        self.btn_0 = QPushButton("0")
        self.btn_eq = QPushButton("=")
        self.btn_plus = QPushButton("+")

        self.btn_7.clicked.connect(self.press_7)
        self.btn_8.clicked.connect(self.press_8)
        self.btn_9.clicked.connect(self.press_9)
        self.btn_div.clicked.connect(self.press_div)
        self.btn_4.clicked.connect(self.press_4)
        self.btn_5.clicked.connect(self.press_5)
        self.btn_6.clicked.connect(self.press_6)
        self.btn_mul.clicked.connect(self.press_mul)
        self.btn_1.clicked.connect(self.press_1)
        self.btn_2.clicked.connect(self.press_2)
        self.btn_3.clicked.connect(self.press_3)
        self.btn_min.clicked.connect(self.press_min)
        self.btn_c.clicked.connect(self.press_c)
        self.btn_0.clicked.connect(self.press_0)
        self.btn_eq.clicked.connect(self.press_eq)
        self.btn_plus.clicked.connect(self.press_plus)

        self.h_lay1 = QHBoxLayout()
        self.h_lay2 = QHBoxLayout()
        self.h_lay3 = QHBoxLayout()
        self.h_lay4 = QHBoxLayout()
        self.v_lay = QVBoxLayout()

        self.h_lay1.addWidget(self.btn_7)
        self.h_lay1.addWidget(self.btn_8)
        self.h_lay1.addWidget(self.btn_9)
        self.h_lay1.addWidget(self.btn_div)

        self.h_lay2.addWidget(self.btn_4)
        self.h_lay2.addWidget(self.btn_5)
        self.h_lay2.addWidget(self.btn_6)
        self.h_lay2.addWidget(self.btn_mul)

        self.h_lay3.addWidget(self.btn_1)
        self.h_lay3.addWidget(self.btn_2)
        self.h_lay3.addWidget(self.btn_3)
        self.h_lay3.addWidget(self.btn_min)

        self.h_lay4.addWidget(self.btn_c)
        self.h_lay4.addWidget(self.btn_0)
        self.h_lay4.addWidget(self.btn_eq)
        self.h_lay4.addWidget(self.btn_plus)

        self.v_lay.addWidget(self.lbl)
        self.v_lay.addLayout(self.h_lay1)
        self.v_lay.addLayout(self.h_lay2)
        self.v_lay.addLayout(self.h_lay3)
        self.v_lay.addLayout(self.h_lay4)

        self.setLayout(self.v_lay)

    def press_7(self):
        self.lbl.setText(self.lbl.text() + "7")

    def press_8(self):
        self.lbl.setText(self.lbl.text() + "8")

    def press_9(self):
        self.lbl.setText(self.lbl.text() + "9")

    def press_div(self):
        self.lbl.setText(self.lbl.text() + "/")

    def press_4(self):
        self.lbl.setText(self.lbl.text() + "4")

    def press_5(self):
        self.lbl.setText(self.lbl.text() + "5")

    def press_6(self):
        self.lbl.setText(self.lbl.text() + "6")

    def press_mul(self):
        self.lbl.setText(self.lbl.text() + "*")

    def press_1(self):
        self.lbl.setText(self.lbl.text() + "1")

    def press_2(self):
        self.lbl.setText(self.lbl.text() + "2")

    def press_3(self):
        self.lbl.setText(self.lbl.text() + "3")

    def press_min(self):
        self.lbl.setText(self.lbl.text() + "-")

    def press_c(self):
        self.lbl.setText("")

    def press_0(self):
        self.lbl.setText(self.lbl.text() + "0")

    def press_eq(self):
        self.lbl.setText(str(eval(self.lbl.text())))

    def press_plus(self):
        self.lbl.setText(self.lbl.text() + "+")

app = QApplication([])
win = Calculator()
win.show()
app.exec_()