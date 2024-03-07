from .CsvFile import *
from .Opcode import *
from .OpcodeGroup import *
from .AddressModes import *

class Cpu:
    def __init__(self):
        # Categories of instructions (Arithmetic, Test, Branch, Jump)
        self.categories = {} # string, list of OpcodeGroup()
        # Groups of instructions (add, sub, etc)
        self.groups = {} # string, OpcodeGroup()
        # Individual instructions
        self.opcodes = {} # string, Opcode()
        # Instruction details
        self.details = {} # string, string
        # Address modes: Immediate, Indirect, etc.
        self.address_modes = Address_Modes()

    def load(self, opcode_file, category_file, modes_file,details_file):
        self.load_address_modes(modes_file)
        self.load_groups(category_file)
        self.load_opcodes(opcode_file)
        self.load_details(defails_file)

    def load_address_modes(self, filename, start_row = 0):
        csv = CsvFile(filename)
        for rn in range(start_row, len(csv)):
            row = csv[rn]
            self.address_modes.add(row[0],row[1],row[2],row[3])

    # Loads a groups CSV in the format
    # Category, Desc
    def load_groups(self, filename, start_row = 0):
        csv = CsvFile(filename)
        for rn in range(start_row, len(csv)):
            row = csv[rn]
            
            grp = OpcodeGroup()
            grp.name = row[0]
            grp.description = row[1]
            self.groups[grp.name] = grp

    # load the opcode details
    # csv is a list of lists, where each row is a list of 7 items in the
    # sequence
    #
    # Name,Mode,flags,Oc,Len,Cycles,Syntax
    # 
    def load_opcodes(self, filename, start_row = 1):
        csv = CsvFile(filename)
        for rn in range(start_row, len(csv)):
            row = csv[rn]
            
            oc = Opcode()
            oc.category_name = row[0]
            oc.mnemonic = row[1]
            oc.address_mode = row[2]
            oc.flags = row[3]
            oc.opcode = row[4]
            oc.bytes = row[5]
            oc.cycles = row[6]
            oc.syntax = row[7]

            grp : OpcodeGroup = self.groups[oc.mnemonic]
            grp.opcodes.append(oc)

            self.opcodes[oc.opcode] = oc

            cn = oc.category_name
            if not cn in self.categories:
                self.categories[cn] = []
            
            if not (oc.mnemonic in self.categories[cn]):
                self.categories[cn].append(oc.mnemonic)

    # loads a details file in the format
    # ## Catgegory
    # Information  about category.
    def load_details(self, filename):
        pass