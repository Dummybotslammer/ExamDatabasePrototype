
class Sheet():
    def __init__(self, width:int, height:int, columnLabel:dict, name = "New Sheet", defaultValue=None):
        self._name = name
        self._width = width
        self._height = height

        self._defaultValue = defaultValue
        self._cells = [[self._defaultValue]*self._width for _ in range(self._height)]

        #TODO setters and getters and other stuff for this later.
        self.columnLabel = columnLabel
        
    def __repr__(self) -> str:
        return self._name
    
    #Getters:
    def get_name(self):
        return self._name

    def get_width(self):
        return self._width

    def get_height(self):
        return self._height

    def get_cell(self, row, column):
        return self._cells[row][column]

    def get_sheet(self):
        #Returns an array:
        return self._cells

    #Setters:
    def set_name(self, name):
        self._name = name

    def set_width(self, width):
        self._width = width

    def set_height(self, height):
        self._height = height

    def set_cell(self, row, column, value):
        self._cells[row, column] = value

    def generate_NewSheet(self):
        self._cells = [[self._defaultValue]*self._width]*self._height

    def set_columnValues(self, args:list, columnIndex=0):
        for x in range (0, len(args)):
            self._cells[x][columnIndex] = args[x]

    def set_rowValues(self, args:list, rowIndex=0):
        for x in range (0, len(args)):
            self._cells[rowIndex][x] = args[x]
