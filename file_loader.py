

class File_Loader:
    symbols = list()
    full_names = list()

    def load_list(self, buffer):
        isSymbol = True
        symbol = ""
        fullName = ""

        for char in buffer:
            if char == '|':
                isSymbol = False
                continue
            if char == '-':
                break

            if isSymbol:
                symbol += char
            else:
                fullName += char
        self.full_names.append(fullName)
        self.symbols.append(symbol)

    def read_file(self):
        with open("nasdaqlisted.txt") as f:
            for line in f:
                self.load_list(line)

    def __init__(self):
        self.read_file()
