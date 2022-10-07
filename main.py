from print import *
from slist import SList
# from course import Course

# def calculate_gpa(courseList):
#   sumGrades = 0
#   credits = 0
#   for course in courseList:
#     sumGrades += course.grade() * course.credit_hr()
#     credits += course.credit_hr()
#   return sumGrades / credits

# def is_sorted(lyst):
#   for i in range(0, len(lyst)  - 1):
#     if lyst[i] > lyst[i + 1]:
#       return False
#   return True

def main():
  test = SList()
  test.insert(1)  
  
  print(test.find(32))
  
if __name__ == "__main__":
    main()