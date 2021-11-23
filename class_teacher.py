import class_person
import class_subject

class Teacher(class_person.Person):
    #subjectsTaught is an array of subjects/classes that are currently being taught by the teacher.
    def __init__(self, name="N/A", age=0, gender=class_person.Gender.Invalid, IC="N/A", subjectsTaught=None):
        #The super(). function gives access to the __init__ function of the parent class.
        super().__init__(name=name, age=age, gender=gender, IC=IC)
        self._subjectsTaught = subjectsTaught

    #Getters:
    def get_subjectsTaught(self):
        return self._subjectsTaught

    #Setters:
    def set_subjectsTaught(self, arg:list):
        self._subjectsTaught = arg