""" Course Class for Project 3 of cs2420 """


class Course:
    """ Course object """

    def __init__(self, number=0, name="no name", credit_hours=0.0, grade=0.0):

        if not isinstance(number, int):
            raise ValueError("numbers argument must be integer.")
        self._number = number

        if not isinstance(name, str):
            raise ValueError("name argument must be a string.")
        self._name = name

        if not isinstance(credit_hours, float):
            raise ValueError("credit_hour argument must be float.")
        self._credit_hours = credit_hours

        if not isinstance(grade, float):
            raise ValueError("grade argument must be float.")
        self._grade = grade

    def number(self):
        "Return number"
        return self._number

    def name(self):
        "Return name"
        return self._name

    def credit_hours(self):
        "return credit_hours"
        return self._credit_hours

    def grade(self):
        "return grade"
        return self._grade

    def __str__(self):
        num = str(self.number())
        cname = self.name()
        cgrade = str(self.grade())
        hours = str(self.credit_hours())
        return (
            'cs'
            + num
            + ' '
            + cname
            + ' Grade: '
            + cgrade
            + ' Credit Hours: '
            + hours
        )

    def __eq__(self, other):
        return self.number() is other.number()

    def __ne__(self, other):
        return self.number() is not other.number()

    def __lt__(self, other):
        return self.number() < other.number()

    def __gt__(self, other):
        return self.number() > other.number()

    def __le__(self, other):
        return self.number() <= other.number()

    def __ge__(self, other):
        return self.number() >= other.number()
