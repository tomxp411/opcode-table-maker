#
# csv
#
# Read a CSV file into the program
#

from .CpuModel_6502 import *
from .Opcode import *
from .Group import *
from .AddressModes import *

class csv_65C02:
    def __init__(self):
        self.cpu = cpu_model_65c02()

    # read the CPU opcodes from the CSV file
    # format is:
    # Group,opcode,mnemonic,address mode,bytes,cycles,flags
    # or 
    # #Descriptive text 
    def load_csv(self, input_filename:str):
        line_number = 0
        cat = Group65C02()
        grp = Group65C02()
        Opcode65C02.address_modes = self.cpu.address_modes

        self.opcode_file = input_filename
        f = open(self.opcode_file,"r")
        for line in f:
            line_number += 1
            
            parts = [line]
            tt = ""
            # ! lines are CSV
            if line.startswith("!"):
                parts = line.rstrip().split(",")
                tt = parts[0][1:].lower().strip()

            # Category
            # can be c,Name or
            # c,Name,OpcodeGroup,Description
            if tt == "c":
                # category
                val = parts[1]
                if not val in self.cpu.categories:
                    cat = Group65C02()
                    cat.name = val 
                    self.cpu.categories[val] = cat
                else:
                    cat = self.cpu.categories[val]
                # Mnemonic
                if len(parts) > 2:
                    val = parts[2]
                    if not val in self.cpu.groups:
                        grp = Group65C02()
                        grp.name = val 
                        self.cpu.groups[val] = grp
                    else:
                        grp = self.cpu.groups[val]
                # Description
                if len(parts) > 3:
                    grp.description = parts[3]

            # Opcode/Instruction
            elif tt == "o":
                op = Opcode65C02(line)
                op.group_name = grp.name
                op.category_name = cat.name
                self.cpu.opcodes[op.opcode] = op
                grp.opcodes.append(op)
                cat.opcodes.append(op)
            else:
                grp.add_comment(line)
        f.close()