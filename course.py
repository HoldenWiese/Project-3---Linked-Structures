""" Course Class for Project 3 of cs2420 """


class Course:
    """ Course object """

    def __init__(self, number=0, name="", credit_hours=0.0, grade=0.0):

        if not isinstance(number, int) or number < 0:
            raise ValueError("number argument must be a positive integer.")
        self._number = number

        if not isinstance(name, str):
            raise ValueError("name argument must be a string.")
        self._name = name

        if not isinstance(credit_hours, float) or credit_hours < 0.0:
            raise ValueError("credit_hour argument must be float and must be positive.")
        self._credit_hours = credit_hours

        if not isinstance(grade, float) or grade < 0.0:
            raise ValueError("grade argument must be float and must be positive.")
        self._grade = grade

    def number(self):
        "Return number"
        return self._number

    def name(self):
        "Return name"
        return self._name

    def credit_hr(self):
        "return credit_hours"
        return self._credit_hours

    def grade(self):
        "return grade"
        return self._grade

    def __str__(self):
        num = str(self.number())
        cname = self.name()
        cgrade = str(self.grade())
        hours = str(self.credit_hr())
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
        return self.number() == other

    def __ne__(self, other):
        return self.number() != other.number()

    def __lt__(self, other):
        return self.number() < other.number()

    def __gt__(self, other):
        return self.number() > other.number()

    def __le__(self, other):
        return self.number() <= other.number()

    def __ge__(self, other):
        return self.number() >= other.number()
