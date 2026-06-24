import requests
from PIL import Image
from io import BytesIO
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import QPixmap

members = [
    {"name": "Itachi", "role": "S-rank", "village": "Konoha", "img": "https://upload.wikimedia.org/wikipedia/en/thumb/4/4f/Itachi_Uchiha.png/220px-Itachi_Uchiha.png"},
    {"name": "Pain", "role": "Leader", "village": "Ame", "img": "https://upload.wikimedia.org/wikipedia/en/thumb/5/5c/Pain_Naruto.png/220px-Pain_Naruto.png"},
    {"name": "Kisame", "role": "Beast hunter", "village": "Kiri", "img": "https://upload.wikimedia.org/wikipedia/en/thumb/3/3e/Kisame_Hoshigaki.png/220px-Kisame_Hoshigaki.png"},
    {"name": "Tobi", "role": "Mysterious", "village": "Unknown", "img": "https://upload.wikimedia.org/wikipedia/en/thumb/8/85/Tobi_Naruto.png/220px-Tobi_Naruto.png"},
    {"name": "Konan", "role": "Paper user", "village": "Ame", "img": "https://upload.wikimedia.org/wikipedia/en/thumb/8/8c/Konan_Naruto.png/220px-Konan_Naruto.png"},
]

def get_pixmap(url, size):
    img = Image.open(BytesIO(requests.get(url).content)).resize((size, size))
    buf = BytesIO()
    img.save(buf, format="PNG")
    p = QPixmap()
    p.loadFromData(buf.getvalue())
    return p

class Card(QWidget):
    def init(self, m):
        super().init()
        self.m = m
        self.lbl_img = QLabel()
        self.lbl_img.setPixmap(get_pixmap(m["img"], 80))
        v = QVBoxLayout()
        v.addWidget(self.lbl_img)
        v.addWidget(QLabel(m["name"]))
        v.addWidget(QLabel(m["role"]))
        v.addWidget(QLabel(m["village"]))
        self.setLayout(v)

    def enterEvent(self, e):
        self.lbl_img.setPixmap(get_pixmap(self.m["img"], 200))

    def leaveEvent(self, e):
        self.lbl_img.setPixmap(get_pixmap(self.m["img"], 80))

class Window(QWidget):
    def init(self):
        super().init()
        self.setWindowTitle("Akatsuki")
        h = QHBoxLayout()
        for m in members:
            h.addWidget(Card(m))
        self.setLayout(h)

app = QApplication([])
win = Window()
win.show()
app.exec_()