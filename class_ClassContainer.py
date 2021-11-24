
class ClasContainer():
    #members should be a list of student objects.
    def __init__(self, members=[]):
        self._members = members

    #Getters:
    def get_members(self):
        return self._members

    def get_names(self):
        x = []
        for y in self._members:
            x.append(y.get_name())
        return x

    def get_ages(self):
        x = []
        for y in self._members:
            x.append(y.get_age())
        return x

    def get_subjects(self):
        x = []
        for y in self._members:
            x.append(y.get_subjectResults())
        return x

    def get_subjectCounts(self):
        x = []
        for y in self._members:
            x.append(len(y.get_subjectResults()))
        return x

    #Setters:
    def set_members(self, arg:list):
        self._members = arg
