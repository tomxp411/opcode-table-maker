#
# csv
#
# Read a CSV file into the program
#

import os

class CsvFile(list):
    def __init__(self, filename = None):
        if filename:
            self.load_csv(filename)
            
    # read the CPU opcodes from the CSV file
    # format is:
    # Group,opcode,mnemonic,address mode,bytes,cycles,flags
    # or 
    # #Descriptive text 
    def load_csv(self, input_file):
        f = open(input_file,"r")
        full_text = f.read()
        f.close()

        ri = 0
        row = []
        cell = ""
        in_quote = False
        full_text = full_text.replace(os.linesep, "\n")
        lastc = ''
        for i in range(0,len(full_text)):
            c = full_text[i]

            if c == '"':
                if lastc == '"':
                    cell += '"'
                in_quote = not in_quote
            elif in_quote:
                cell += c
            elif c == "\n":
                row.append(cell.strip())
                self.append(row)
                row = []
                cell = ""
            elif c == ",":
                row.append(cell.strip())
                cell = ""
            else:
                cell += c

        if len(row) > 0:
            row.append(cell.strip())
            self.append(row)

        print(input_file, len(self),"rows read.")
