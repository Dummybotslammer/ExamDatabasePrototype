import class_person
import class_subject

class Student(class_person.Person):
    #subjectsTaken should be an array of subjectResults
    def __init__(self, name="N/A", age=0, gender=class_person.Gender.Invalid, IC="N/A", Class="N/A", subjectResults=None):
        #The super(). function gives access to the __init__ function of the parent class.
        super().__init__(name=name, age=age, gender=gender, IC=IC)
        self._Class = Class
        self._subjectResults = subjectResults

    #Getters:
    def get_Class(self):
        return self._Class

    def get_subjectResults(self):
        return self._subjectResults

    #Setters:
    def set_Class(self, Class:str):
        self._Class = Class

    def set_subjectResults(self, arg:list):
        self._subjectResults = arg

'''Test Code:
new = Student()
print(new.get_name())
print("Yes \t yes")
print(new.test)
'''