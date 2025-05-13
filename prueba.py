class Date:
    days_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def __init__(self, day=1, month=1, year=1):
        self.day = day
        self.month = month
        self.year = year

    def isLeap(self):
        if self.year % 4 == 0:
            if self.year % 400 == 0:
                return "Es bisiesto"
            elif self.year % 100 == 0:
                return "No es bisiesto"
            return "Es bisiesto"
        return "No es bisiesto"

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
