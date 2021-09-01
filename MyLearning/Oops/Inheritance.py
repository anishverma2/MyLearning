class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)


class WorkingStudent(Student):
    def __init__(self, name, school, salary):
        super().__init__(name, school)
        self.salary = salary

    def weekly_salary(self):
        return self.salary * 37.5

anish = WorkingStudent('Anish', 'AIT', 16)
print(anish.salary)
anish.marks.append(55)
anish.marks.append(70)
print(anish.average())
print(anish.weekly_salary())

#use of @ decorator

class Working(Student):
    def __init__(self, name, school, salary):
        super().__init__(name, school)
        self.salary = salary

    @property   #this decorator turns the method such that without the parenthesis we can still call the method
    def weekly_salary(self):
        return self.salary * 37.5

rolf = Working('Rolf', 'MIT', 15.50)
print(rolf.weekly_salary)

'''
verma = Student('Verma', 'AIT')
print(verma.weekly_salary()) # this gives an error as Student don't have any method named Weekly_Salary
'''