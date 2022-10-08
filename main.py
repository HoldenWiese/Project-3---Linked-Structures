from slist import SList
from course import Course

def calculate_gpa(courseList):
  sumGrades = 0
  credits = 0
  for course in courseList:
    sumGrades += course.grade() * course.credit_hr()
    credits += course.credit_hr()
  return sumGrades / credits

def is_sorted(lyst):
  for i in range(0, len(lyst)  - 1):
    if lyst[i] > lyst[i + 1]:
      return False
  return True

def main():
    test1 = Course('1400', 'OOP', 3.0, 3.6)
    test2 = Course(1410, 'DS', 4.0, 3.9)
    print(test1)
    print(test2)
    print(test1 == test2)
    print(test1 != test2)
    print(test1 < test2)
    print(test1 > test2)
    print(test1 <= test2)
    print(test1 >= test2)
  
if __name__ == "__main__":
    main()