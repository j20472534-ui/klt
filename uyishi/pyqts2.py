from PyQt5.QtWidgets import *
import json

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.v_main_lay = QVBoxLayout()
        self.h_btn_lay = QHBoxLayout()

        self.setStyleSheet("background: black")

        self.name = QLineEdit()
        self.name.setText("name")
        self.name.setStyleSheet("""
            color: white;
            font-size: 20px
        """)

        self.second = QLineEdit()
        self.second.setText("second")
        self.second.setStyleSheet("""
            color: white;
            font-size: 20px
        """)

        self.age = QLineEdit()
        self.age.setText("age")
        self.age.setStyleSheet("""
            color: white;
            font-size: 20px
        """)

        self.lbl_city = QLabel("SHAHAR")
        self.lbl_city.setStyleSheet("""
            color: orange;
            font-size: 25px
        """)

        self.cmb_city = QComboBox()
        self.cmb_city.addItems([
            "Toshkent",
            "Samarqand",
            "Buxoro"
        ])

        self.cmb_city.setStyleSheet("""
            color: white;
            font-size: 20px
        """)

        self.lbl_tuman = QLabel("TUMAN")
        self.lbl_tuman.setStyleSheet("""
            color: orange;
            font-size: 25px
        """)

        self.cmb_tuman = QComboBox()

        self.cmb_tuman.setStyleSheet("""
            color: white;
            font-size: 20px
        """)

        self.cmb_city.activated[str].connect(self.ChangeTuman)

        self.btn_submit = QPushButton("SUBMIT")
        self.btn_submit.clicked.connect(self.Submit)

        self.btn_submit.setStyleSheet("""
            color: lime;
            font-size: 20px
        """)

        self.btn_exit = QPushButton("EXIT")
        self.btn_exit.clicked.connect(exit)

        self.btn_exit.setStyleSheet("""
            color: lime;
            font-size: 20px
        """)

        self.h_btn_lay.addWidget(self.btn_submit)
        self.h_btn_lay.addWidget(self.btn_exit)

        self.v_main_lay.addWidget(self.name)
        self.v_main_lay.addWidget(self.second)
        self.v_main_lay.addWidget(self.age)

        self.v_main_lay.addWidget(self.lbl_city)
        self.v_main_lay.addWidget(self.cmb_city)

        self.v_main_lay.addWidget(self.lbl_tuman)
        self.v_main_lay.addWidget(self.cmb_tuman)

        self.v_main_lay.addLayout(self.h_btn_lay)

        self.setLayout(self.v_main_lay)

        self.ChangeTuman("Toshkent")

    def ChangeTuman(self, city):

        self.cmb_tuman.clear()

        if city == "Toshkent":
            self.cmb_tuman.addItems([
                "Yunusobod",
                "Chilonzor",
                "Olmazor"
            ])

        elif city == "Samarqand":
            self.cmb_tuman.addItems([
                "Urgut",
                "Bulungur"
            ])

        elif city == "Buxoro":
            self.cmb_tuman.addItems([
                "Gijduvon",
                "Kogon"
            ])

    def Submit(self):

        data = {
            "name": self.name.text(),
            "second": self.second.text(),
            "age": self.age.text(),
            "city": self.cmb_city.currentText(),
            "tuman": self.cmb_tuman.currentText()
        }

        file = open("users.json", "w")

        json.dump(data, file, indent=4)

        file.close()

        QMessageBox.information(
            self,
            "message",
            "saved"
        )

app = QApplication([])

win = MyWindow()
win.show()

app.exec_()