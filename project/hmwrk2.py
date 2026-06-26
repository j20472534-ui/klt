import json
import os

from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QMessageBox,
    QVBoxLayout
)


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Yangi film qo'shish ilovasi")
        self.setFixedSize(450, 350)

        layout = QVBoxLayout()

        self.title_input = QLineEdit()
        self.director_input = QLineEdit()
        self.year_input = QLineEdit()
        self.genre_input = QLineEdit()

        self.add_button = QPushButton("Qo'shish")

        layout.addWidget(QLabel("Film nomi:"))
        layout.addWidget(self.title_input)

        layout.addWidget(QLabel("Rejissor:"))
        layout.addWidget(self.director_input)

        layout.addWidget(QLabel("Yili:"))
        layout.addWidget(self.year_input)

        layout.addWidget(QLabel("Janr:"))
        layout.addWidget(self.genre_input)

        layout.addWidget(self.add_button)

        self.setLayout(layout)

        self.add_button.clicked.connect(self.add_movie)

    def add_movie(self):
        title = self.title_input.text()
        director = self.director_input.text()
        year = self.year_input.text()
        genre = self.genre_input.text()

        if not title or not director or not year or not genre:
            QMessageBox.warning(
                self,
                "Xatolik",
                "Iltimos, barcha ma'lumotlarni to'ldiring!"
            )
            return

        if not year.isdigit():
            QMessageBox.warning(
                self,
                "Xatolik",
                "Yil raqam bo'lishi kerak!"
            )
            return

        movie = {
            "title": title,
            "director": director,
            "year": int(year),
            "genre": genre
        }

        if not os.path.exists("movies.json"):
            with open("movies.json", "w") as file:
                json.dump([], file)

        with open("movies.json", "r") as file:
            data = json.load(file)

        data.append(movie)

        with open("movies.json", "w") as file:
            json.dump(data, file, indent=4)

        QMessageBox.information(
            self,
            "Muvaffaqiyatli",
            "Film muvaffaqiyatli qo'shildi!"
        )

        self.title_input.clear()
        self.director_input.clear()
        self.year_input.clear()
        self.genre_input.clear()


app = QApplication([])

window = Window()
window.show()

app.exec_()