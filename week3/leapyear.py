class LeapYear():
    def __init__(self):
        pass

    def is_leapyear(self, year):
        if (not isinstance(year, int)) or isinstance(year, bool):
            raise ValueError(f"This is not a year, silly: {year}")

        return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0
