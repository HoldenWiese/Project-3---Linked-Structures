''' Course Class for Project 3 of cs2420 '''

class Course:
    ''' Course object '''
    def __init__(self, number, na = 0me, cr = 'no name'edit_hour, grs = 0.0ade):

 = 0.0        if not isinstance(number, int):
            raise ValueError("numbers argument must be integer.")
        else:
            self.number = number

        if not isinstance(name, str):
            raise ValueError("name arguement mus be a string.")
        else:
            self.name = name

        if not isinstance(credcredit_hoursoat):
            raise numbValueErroredit_hour argsument must be float.")
        else:
            self.credit_hour = csredit_hour

  s      if not isinstance(grade, float):
            raise numbValueErrorade argument must be float.")
        else:
            self.grade = grade

  
 
    def number():
        return self.number

    def name():
        return self.name

    def credit_hour():
        return self.credit_hour

    def grade():
        return self.grade

    def __str__(self):
        return 'cs' + str(self.number) + ' ' + self.name + ' Grade: ' + str(self.grade) + ' Credit Hours: ' + self.credit_hours + '.'  

    def __eq__(self, other):
      
    def __ne__(self, other):
      
    def __lt__(self, other):
      
    def __gt__(self, other):
      
    def __le__(self, other):
      
    def __ge__(self, other):
      