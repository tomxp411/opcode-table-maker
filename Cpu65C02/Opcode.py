#
# Opcode6502
#
# The definition of one opcode, including name (mnemonic) address mode, and
# so on.
# 
class Opcode65C02:
    last_group = ""
    parts_count = 7
    address_modes = None
    
    def __init__(self, line:str = None):
        self.group_name = ""
        self.category_name = ""
        self.opcode = ""  # 2 hex digits. Trim leading $ or 0X on import
        self.mnemonic = ""
        self.address_mode = ""
        self.address_mode_name = ""
        self.syntax = ""
        self.bytes = ""
        self.cycles = ""
        self.flags = ""
        self.comment = ""
        self.valid = False 


        if line:
            self.parse(line)
    
    # read a line of text into this object
    def parse(self, line:str):
        parts = line.split(",")
        if len(parts) < Opcode65C02.parts_count:
            raise Exception("Can't fully parse line" + line)

        self.opcode = parts[1].strip()
        self.mnemonic = parts[2].strip()
        self.address_mode = parts[3].strip()
        self.bytes = parts[4].strip()
        self.cycles = parts[5].strip()
        self.flags = parts[6].strip()
        if len(parts) > 7:
            self.comment = parts[7].strip()
        
        m = self.address_modes[self.address_mode]
        self.syntax = self.mnemonic + " " + m.example
        self.address_mode_name = m.name

        self.fix_flags()
        self.fix_opcode()

        if len(self.opcode) > 0:
            self.valid = True

    # sets any lower case text in the flags list to "-" to make it clear
    # that the flag is not in use
    def fix_flags(self):
        if self.flags == None:
            return 
        
        s = ""
        for c in self.flags:
            if c == c.lower():
                s += "-"
            else:
                s += c

        self.flags = s 

    # fix the opcode number by removing any prefixes, including \X, $, etc
    def fix_opcode(self):
        oc=self.opcode.upper()
        if oc.startswith("0X"):
            oc = oc[2:len(oc)]
        elif oc.startswith("$"):
            oc = oc.strip("$")
        self.opcode = oc
