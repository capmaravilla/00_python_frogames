from os import system

system("cls")


class Date:
    days_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    months_names = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]

    def __init__(self, day=1, month=1, year=1):
        self.day = day
        self.month = month
        self.year = year

    @staticmethod
    def zero_filler(n, l):
        n = str(n)
        r = l - len(n)
        if r == 0:
            return n
        else:
            for _ in range(r):
                n = f"0{n}"
        return n

    def __str__(self):
        return f"{self.zero_filler(self.day,2)}/{self.zero_filler(self.month,2)}/{self.zero_filler(self.year,4)}"

    def isLeap(self):
        if self.year % 4 == 0:
            if self.year % 400 == 0:
                return True
            elif self.year % 100 == 0:
                return False
            return True
        return False

    def totalMonthDays(self):
        if self.month > 12 or self.month < 1:
            return "Introduce primero una fecha valida!"
        if self.month == 2 and self.isLeap == True:
            return 29
        else:
            return self.days_month[self.month - 1]

    def validDate(self):
        if self.month < 1 or self.month > 12:
            return False
        elif self.day < 1 or self.day > self.totalMonthDays():
            return False
        return True

    @property
    def monthName(self):
        return self.months_names[self.month - 1]

    @staticmethod
    def areEqual(a, b):
        if a.year == b.year and a.month == b.month and a.day == b.day:
            return "La fechas son iguales"
        return "Las fechas no son iguales"

    @staticmethod
    def isLater(a, b):
        if a.year != b.year:
            if a.year > b.year:
                return a
            return b
        elif a.month != b.month:
            if a.month > b.month:
                return a
            return b
        elif a.day != b.day:
            if a.day > b.day:
                return a
            return b
        else:
            Date.areEqual(a, b)

    @staticmethod
    def isPrevious(a, b):
        if Date.isLater(a, b) == a:
            return b
        return a

    @classmethod
    def firstDayOfTheYear(cls, year):
        return cls(1, 1, year)

    @classmethod
    def lastDayOfTheYear(cls, year):
        return cls(31, 12, year)

    def plusDay(self):
        if self.day < self.days_month[self.month - 1]:
            self.day += 1
            return self.__str__()
        elif self.month < 12:
            self.day = 1
            self.month += 1
            return self.__str__()
        else:
            self.day = 1
            self.month = 1
            self.year += 1
            return self.__str__()

    def minusDay(self):
        if self.day > 1:
            self.day -= 1
            return self.__str__()
        elif self.month > 1:
            self.month -= 1
            self.day = self.days_month[self.month - 1]
            return self.__str__()
        else:
            self.day = self.days_month[self.month - 1]
            self.month = 12
            self.year -= 1
            return self.__str__()

    @classmethod
    def copy(cls, sample):
        return cls(sample.day, sample.month, sample.year)

    @staticmethod
    def difference(a, b):
        pos = Date.isLater(a, b)
        pre = Date.isPrevious(a, b)
        total_days = 0

        # Recorremos los años completos entre pre.year y pos.year
        for year in range(pre.year, pos.year + 1):
            temp_date = Date(1, 1, year)
            if temp_date.isLeap():
                total_days += 366  # Año bisiesto
            else:
                total_days += 365  # Año no bisiesto

        # Restamos los días del año inicial antes de la fecha 'pre'
        temp_pre = Date(1, 1, pre.year)
        for month in range(1, pre.month):
            temp_pre.month = month
            total_days -= temp_pre.totalMonthDays()
        total_days -= pre.day - 1

        # Restamos los días del año final después de la fecha 'pos'
        temp_pos = Date(1, 1, pos.year)
        for month in range(pos.month + 1, 13):
            temp_pos.month = month
            total_days -= temp_pos.totalMonthDays()
        total_days -= temp_pos.totalMonthDays() - pos.day

        return total_days


a = Date(6, 5, 1976)
b = Date(1, 1, 2025)
print(Date.difference(a, b))
