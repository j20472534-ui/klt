# from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton
# app = QApplication([])
# win = QWidget()
# win.setGeometry(700, 200, 400, 200)
# win.setWindowTitle("App")
# name = QLabel("ism: ", win)
# name.setStyleSheet("font-size: 20px")
# name.move(20, 20)
# year = QLabel("year: ", win)
# year.setStyleSheet("font-size: 20px")
# year.move(20, 50)


# n = QLabel("", win)
# n.move(90, 120)

# e_name = QLineEdit(win)
# e_name.move(100, 20)

# e_year = QLineEdit(win)
# e_year.move(100, 50)


# def Test():
#     n.setText(f"{e_name.text()} {e_year.text()}")
#     n.adjustSize()

#     e_name.clear()
#     e_year.clear()

# b = QPushButton("OK", win)
# b.move(90, 150)
# b.clicked.connect(Test)

# win.show()
# # app.exec_()
# app = QApplication([])
# win = QWidget()
# win.setGeometry(700, 200, 400, 200)
# win.setWindowTitle("App")
# uz = QLabel("uz: ", win)
# uz.setStyleSheet("font-size: 20px")
# uz.move(20, 20)
# eng = QLabel("eng: ", win)
# eng.setStyleSheet("font-size: 20px")
# eng.move(20, 50)


# n = QLabel("", win)
# n.move(90, 120)

# uz = QLineEdit(win)
# uz.move(100, 20)

# eng = QLineEdit(win)
# eng.move(100, 50)


# def Test():
#     n.setText(f"{uz.text()} {eng.text()}")
#     n.adjustSize()

#     uz.clear()
#     eng.clear()
# def dkt():
#     dct={}
#     print
    

# b = QPushButton("OK", win)
# b.move(30, 150)
# b.clicked.connect(Test)
# b = QPushButton("Show", win)
# b.move(190, 150)
# b.clicked.connect(dkt)
# win.show()
# app.exec_()
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.v_main_lay = QVBoxLayout()
        self.h_btn_lay = QPushButton("Clear")
        self.h_btn_lay = QPushButton("+")
        self.h_btn_lay = QPushButton("k")
        
        self.setLayout(self.v_main_lay)
app = QApplication([])
win = MyWindow()
win.show()
app.exec_()
