from os import system, name

from class_spreadsheet import Sheet #This will be for clearing the screen.

#Important functions:
def clrscrn():
    #For clearing in windows
    if name == 'nt':
        i = system('cls')
  
    #For clearing mac and linux(here, os.name is 'posix')
    else:
        i = system('clear')

#TODO Text Renderer Class and the Spreadsheet Class.
class SheetTextRenderer():
    def __init__(self, bufferWidth:int, bufferHeight:int, defaultText=None, cellSize=5, cellSpacing=1, horizontalBorderCharacter="-", verticalBorderCharacter ="|", showCoords=False):
        self._bufferWidth = bufferWidth
        self._bufferHeight = bufferHeight
        self._defaultText = defaultText
        self._sheetRenderBuffer = [[self._defaultText]*self._bufferWidth for _ in range(self._bufferHeight)]
        self._cellSize = cellSize
        self._cellSpacing = cellSpacing
        self._horizontalBorderCharacter = horizontalBorderCharacter
        self._verticalBorderCharacter = verticalBorderCharacter
        self._showCoords = showCoords

    #Getters:
    def get_bufferWidth(self):
        return self._bufferWidth

    def get_bufferHeight(self):
        return self._bufferHeight

    def get_defaultText(self):
        return self._defaultText

    def get_cellSpacing(self):
        return self._cellSpacing

    def get_horizontalBorderCharacter(self):
        return self._horizontalBorderCharacter

    def get_veritcalBorderCharacter(self):
        return self._verticalBorderCharacter

    def get_sheetRenderBuffer(self):
        return self._sheetRenderBuffer

    def get_element_sheetRenderBuffer(self, row:int , column:int):
        return self._sheetRenderBuffer[row][column]

    def get_showCoords(self):
        return self._showCoords

    def get_cellSize(self):
        return self._cellSize

    #Setters:
    def set_bufferWidth(self, bufferWidth:int):
        self._bufferWidth = bufferWidth

    def set_bufferHeight(self, bufferHeight:int):
        self._bufferHeight = bufferHeight

    def set_defaultText(self, defaultText:str):
        self._defaultText = defaultText

    def set_cellSpacing(self, cellSpacing:int):
        self._cellSpacing = cellSpacing

    def set_horizontalBorderCharacter(self, arg:chr):
        self._horizontalBorderCharacter = arg

    def set_veritcalBorderCharacter(self, arg:chr):
        self._verticalBorderCharacter = arg

    def generate_NewRenderBuffer(self):
        self._sheetRenderBuffer = [[self._defaultText]*self._bufferWidth]*self._bufferHeight

    def set_element_sheetRenderBuffer(self, row:int, column:int, arg):
        self._sheetRenderBuffer[row][column] = arg

    def set_showCoords(self, arg:bool):
        self._showCoords = arg

    def set_cellSize(self, cellSize):
        self._cellSize = cellSize

    #Rendering functions:
    def RenderSheet(self, label:str, sheet:list):
        #Sets the rendered sheet to the sheet given.
        self._sheetRenderBuffer = sheet

        #Prints a top cover for the label, and the beginning of the sheet. Might want to redo the code
        print(self._horizontalBorderCharacter*(self._cellSize+(2*self._cellSpacing)+1)*self._bufferWidth, end=self._horizontalBorderCharacter+"\n")
        print(label)
        print(self._horizontalBorderCharacter*(self._cellSize+(2*self._cellSpacing)+1)*self._bufferWidth, end=self._horizontalBorderCharacter+"\n")
        #TODO: print out column labels
        print(self._horizontalBorderCharacter*(self._cellSize+(2*self._cellSpacing)+1)*self._bufferWidth, end=self._horizontalBorderCharacter+"\n")

        #Test code for the cell printing
        for y in self._sheetRenderBuffer:
            for x in y:
                if len(str(x)) > self._cellSize:
                    #TODO 
                    pass

                elif len(str(x)) < self._cellSize:
                    print(self._verticalBorderCharacter + " "*1 + str(x) + " "*(self._cellSize-len(str(x))), end=" "*self._cellSpacing)

                #In this scenario, the spacing would be perfect.
                else:
                    print(self._verticalBorderCharacter + " "*1 + str(x), end=" "*self._cellSpacing)
            print("|")

        #Prints a bottom cover.
        print(self._horizontalBorderCharacter*(self._cellSize+(2*self._cellSpacing)+1)*self._bufferWidth, end=self._horizontalBorderCharacter+"\n")

'''Test Code:
test = SheetTextRenderer(10, 10, defaultText="Yes", cellSpacing=1)
test.RenderSheet()
'''
