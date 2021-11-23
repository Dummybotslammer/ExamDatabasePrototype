import enum

#This section will contain tags/enums.
class Subjects(enum.Enum):
    Invalid = "N/A"
    Math = "Mathematics"
    Science = "Science"
    English = "English"
    BM = "Bahasa Melayu"

class Grade(enum.Enum):
    Invalid = "N/A"
    A_PLUS = "A+"
    A = "A"
    A_MINUS = "A-"

    B_PLUS = "B+"
    B = "B"
    B_MINUS = "B-"

    C_PLUS = "C+"
    C = "C"
    C_MINUS = "C-"

    D_PLUS = "D+"
    D = "D"
    D_MINUS = "D-"

    E_PLUS = "E+"
    E = "E"
    E_MINUS = "E-"

    F = "F"

#This section will contain the classes.
class subjectResults():
    def __init__(self, subject=Subjects.Invalid, completed=False, score=0, grade=Grade.Invalid):
        self._subject = subject 
        self._isCompleted = completed
        self._score = score
        self._grade = grade

    #Getters:
    def get_subject(self):
        return self._subject

    def get_isCompleted(self):
        return self._isCompleted

    def get_score(self):
        return self._score

    def get_grade(self):
        return self._grade

    #Setters:
    def set_subject(self, subject:Subjects):
        self._subject = subject

    def set_isCompleted(self, arg:bool):
        self._isCompleted = arg

    def set_score(self, score:int):
        self._score = score

    def set_grade(self, grade:Grade):
        self._grade = grade

    #The update_grade function is based on SPM grading. 
    #TODO: I might add a feature where it can be modified in a settings file
    def update_grade(self):
        pass

class subjectTaught():
    def __init__(self, subject=Subjects.Invalid, classTaught="N/A"):
        self._subject = subject
        self._classTaught = classTaught

    #Getter:
    def get_subject(self):
        return self._subject

    def get_classTaught(self):
        return self._classTaught

    #Setter:
    def set_subject(self, subject:Subjects):
        self._subject = subject

    def set_classTaught(self, arg:str):
        self._classTaught = arg
