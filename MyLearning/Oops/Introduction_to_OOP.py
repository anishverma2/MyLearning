class Student: #normally we should start the class name with uppercase
    def __init__(self, new_name, new_grades):  #dunder method with 2 underscore in start and end
        self.name = new_name    #self is a blank object and we can give any name to it
        self.grades = new_grades    #dunder init method automatically gets called when we create an object

    def average(self):
        return sum(self.grades) / len(self.grades)

student_one = Student('Anish', [70, 85, 90, 95]) #it automatically calls the dunder init method as soon as the object is created
#self refers to the object calling it
student_two = Student ('Verma', [95, 85, 75, 60])

print(student_one.name)
print(student_one.__class__) # gives the class name
print(student_two.name)

print(student_one.average())
print(Student.average(student_one)) # another way to call the method
print(student_two.average())
student_three = Student(None, None)

student_three.__init__("Anish", [100,100,100,100,100])
print(student_three.average())
print(student_three.name)