class MyDate:
    MONTHS = ["Yanvar", "Fevral", "Mart", "Aprel", "May", "Iyun",
              "Iyul", "Avgust", "Sentabr", "Oktabr", "Noyabr", "Dekabr"]
    DAY_IN_MONTHS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    def __init__(self, day, month, year):
        if self.isValidDate(day, month, year):
            self.__day = day
            self.__month = month
            self.__year = year
        else:
            raise ValueError("Noto'g'ri sana")

    def isLeapYear(self, year):
        if year % 400 == 0:
            return True
        elif year % 100 == 0:
            return False
        elif year % 4 == 0:
            return True
        return False

    def isValidDate(self, day, month, year):
        if year < 1 or year > 9999:
            return False
        if month < 1 or month > 12:
            return False

        max_day = self.DAY_IN_MONTHS[month - 1]
        if month == 2 and self.isLeapYear(year):
            max_day = 29

        if day < 1 or day > max_day:
            return False

        return True

    def setDate(self, day, month, year):
        if self.isValidDate(day, month, year):
            self.__day = day
            self.__month = month
            self.__year = year
        else:
            raise ValueError("Noto'g'ri sana")

    def nextDay(self):
        max_day = self.DAY_IN_MONTHS[self.__month - 1]

        if self.__month == 2 and self.isLeapYear(self.__year):
            max_day = 29

        if self.__day < max_day:
            self.__day += 1
        elif self.__month == 12:
            self.__day = 1
            self.__month = 1
            self.__year += 1
        else:
            self.__day = 1
            self.__month += 1

    def previousDay(self):
        if self.__day > 1:
            self.__day -= 1
        elif self.__month == 1:
            self.__day = 31
            self.__month = 12
            self.__year -= 1
        else:
            self.__month -= 1

            max_day = self.DAY_IN_MONTHS[self.__month - 1]
            if self.__month == 2 and self.isLeapYear(self.__year):
                max_day = 29

            self.__day = max_day

    def nextMonth(self):
        if self.__month == 12:
            self.__month = 1
            self.__year += 1
        else:
            self.__month += 1

        max_day = self.DAY_IN_MONTHS[self.__month - 1]
        if self.__month == 2 and self.isLeapYear(self.__year):
            max_day = 29

        if self.__day > max_day:
            self.__day = max_day

    def previousMonth(self):
        if self.__month == 1:
            self.__month = 12
            self.__year -= 1
        else:
            self.__month -= 1

        max_day = self.DAY_IN_MONTHS[self.__month - 1]
        if self.__month == 2 and self.isLeapYear(self.__year):
            max_day = 29

        if self.__day > max_day:
            self.__day = max_day

    def nextYear(self):
        self.__year += 1

        if self.__month == 2 and self.__day == 29:
            if not self.isLeapYear(self.__year):
                self.__day = 28

    def previousYear(self):
        self.__year -= 1

        if self.__month == 2 and self.__day == 29:
            if not self.isLeapYear(self.__year):
                self.__day = 28

    def __str__(self):
        return f"{self.__day:02d}-{self.MONTHS[self.__month - 1]} {self.__year} yil"
sana = MyDate(15, 6, 2023)
sana.nextDay()
print(sana)

sana = MyDate(31, 12, 2023)
sana.nextDay()
print(sana)

sana = MyDate(29, 2, 2024)
sana.nextDay()
print(sana)