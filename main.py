import class_person
import class_student
import class_teacher
import class_subject
import class_spreadsheet
import class_SheetRenderer
import class_ClassContainer

#If im not careful, this project could turn into an unmanageable/over-engineered mess.

command = ""
#columnLabel will be linked to the object's getters (Students)
testSheet = class_spreadsheet.Sheet(5, 5, {}, name = "Class 2A Results", defaultValue="N/A")
classContainer = class_ClassContainer.ClasContainer([
    class_student.Student(name="Adrian", age=14, gender=class_person.Gender.Male, IC="XXXXXXXXXXXX", Class="2A", subjectResults=[]),
    class_student.Student(name="Brandon", age=15, gender=class_person.Gender.Male, IC="XXXXXXXXXXXX", Class="2A", subjectResults=[]),
    class_student.Student(name="Dominic", age=16, gender=class_person.Gender.Male, IC="XXXXXXXXXXXX", Class="2A", subjectResults=[]),
    class_student.Student(name="Kelvin", age=17, gender=class_person.Gender.Male, IC="XXXXXXXXXXXX", Class="2A", subjectResults=[]),
    class_student.Student(name="Edith", age=18, gender=class_person.Gender.Male, IC="XXXXXXXXXXXX", Class="2A", subjectResults=[])
    ])
testRenderer = class_SheetRenderer.SheetTextRenderer(5, 5, defaultText=True, cellSpacing=1, cellSize=10)

#Test Code:
#print(testSheet.get_sheet())
#print(classContainer.get_names())

#Fills values:
testSheet.set_columnValues(classContainer.get_names(), 0) #Names
testSheet.set_columnValues(classContainer.get_ages(), 1) #Ages
testSheet.set_columnValues(classContainer.get_subjectCounts(), 2) #Subject Count

def main():
    print("Running ExamDatabase...\n")

    while True:
        #Command input:
        command = input(">")

        #TODO: Basic command interpreter, but might need to redo it into a module/class:
        if command.lower() == "help":
            print("Work in Progress.")

        elif command.lower() == "fetch":
            print("\n")
            testRenderer.RenderSheet(testSheet.get_name(), testSheet.get_sheet())
    
        elif command.lower() == "clear" or command.lower() == "clr":
            class_SheetRenderer.clrscrn()

if __name__ == "__main__":
    main()
