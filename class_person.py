import enum

#This section will contain tags/enums for human objects.
class Gender(enum.Enum):
    Invalid = "N/A"
    Male = "MALE"
    Female = "FEMALE"

#This section is for the Person class.
class Person():
    def __init__(self, name="N/A", age=0, gender=Gender.Invalid, IC="N/A"):
        self._name = name
        self._age = age
        self._gender = gender
        self._IC = IC

    #GETTERS
    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    def get_gender(self):
        return self._gender

    def get_IC(self):
        return self._IC

    #SETTERS
    def set_name(self, name:str):
        self._name = name

    def set_age(self, age:int):
        self._age = age

    def set_gender(self, gender:Gender):
        self._gender = gender

    def set_IC(self, IC:str):
        self._IC = IC

''' Test code:
new = Person()
print(new.get_name())
new.set_gender(Human.Gender.Male)
print(new.get_gender().name)
'''