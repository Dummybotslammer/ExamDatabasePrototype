import class_person
import class_student
import class_teacher
import class_subject
import class_spreadsheet
import class_SheetRenderer

test = class_SheetRenderer.SheetTextRenderer(10, 10, defaultText="True", cellSpacing=1)
command = ""

def main():
    print("Running ExamDatabase...")
    test.RenderSheet("TestSheet")
    command = input(">")
    
if __name__ == "__main__":
    main()
