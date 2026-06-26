from PyQt5.QtWidgets import *
import json
class mywindow(QWidget):
    def __init__(self):
        super().__init__()
        self.v_main_lay = QVBoxLayout()
        self.h_btn_lay = QHBoxLayout()
        self.movie_name=QLineEdit()
        
        
        
        
        self.setLayout(self.v_main_lay)
        self.setStyleSheet("background: black")
        f=open("movies.json","r+")
app = QApplication([])
win = mywindow()
win.show()
app.exec_()