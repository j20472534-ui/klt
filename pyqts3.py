import json
import os

from PyQt5.QtWidgets import *


class TaskManagerLite(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Task Manager Lite")

        self.fayl_nomi = "tasks.json"

        self.jsonni_tekshir()

        self.v_main_lay = QVBoxLayout()

        self.task_input = QLineEdit()

        self.status_input = QLineEdit()

        self.search_input = QLineEdit()

        self.add_btn = QPushButton("Qo'shish")
        self.add_btn.clicked.connect(self.task_qoshish)

        self.search_btn = QPushButton("Qidirish")
        self.search_btn.clicked.connect(self.task_qidirish)

        self.total_btn = QPushButton("Umumiy son")
        self.total_btn.clicked.connect(self.umumiy_son)

        self.info_label = QLabel("Jami tasklar: 0")

        self.v_main_lay.addWidget(self.task_input)
        self.v_main_lay.addWidget(self.status_input)
        self.v_main_lay.addWidget(self.search_input)

        self.v_main_lay.addWidget(self.add_btn)
        self.v_main_lay.addWidget(self.search_btn)
        self.v_main_lay.addWidget(self.total_btn)

        self.v_main_lay.addWidget(self.info_label)

        self.setLayout(self.v_main_lay)

    def jsonni_tekshir(self):

        if os.path.exists(self.fayl_nomi):

            try:
                with open(self.fayl_nomi, "r") as f:
                    self.tasks = json.load(f)

            except:
                self.tasks = []

        else:
            self.tasks = []
            self.jsonga_saqlash()

    def jsonga_saqlash(self):

        with open(self.fayl_nomi, "w") as f:
            json.dump(self.tasks, f, indent=4)

    def task_qoshish(self):

        task = self.task_input.text().strip()
        status = self.status_input.text().strip()

        if not task or not status:

            QMessageBox.warning(
                self,
                "Xato",
                "Barcha maydonlarni to'ldiring!"
            )

            return

        if status != "Done" and status != "Pending":

            QMessageBox.warning(
                self,
                "Xato",
                "Status noto'g'ri!"
            )

            return

        yangi_task = {
            "task": task,
            "status": status
        }

        self.tasks.append(yangi_task)

        self.jsonga_saqlash()

        QMessageBox.information(
            self,
            "OK",
            "Task qo'shildi!"
        )

        self.task_input.clear()
        self.status_input.clear()

    def task_qidirish(self):

        qidiruv = self.search_input.text().strip()

        for task in self.tasks:

            if task["task"].lower() == qidiruv.lower():

                QMessageBox.information(
                    self,
                    "Topildi",
                    f"Task: {task['task']}\nStatus: {task['status']}"
                )

                return

        QMessageBox.information(
            self,
            "Natija",
            "Topilmadi!"
        )

    def umumiy_son(self):

        jami = len(self.tasks)

        self.info_label.setText(f"Jami tasklar: {jami}")

        QMessageBox.information(
            self,
            "Umumiy",
            f"Umumiy tasklar soni: {jami}"
        )


app = QApplication([])

oyna = TaskManagerLite()
oyna.show()

app.exec_()