#
# Opcode6502
#
# The definition of one opcode, including name (mnemonic) address mode, and
# so on.
# 
class Opcode65C02:
    last_group = ""
    parts_count = 7
    
    def __init__(self, line:str = None):
        self.group_name = "" 
        self.opcode = ""  # 2 hex digits. Trim leading $ or 0X on import
        self.mnemonic = ""
        self.address_mode = ""
        self.bytes = ""
        self.cycles = ""
        self.flags = ""
        self.valid = False 


        if line:
            self.parse(line)
    
    # read a line of text into this object
    def parse(self, line:str):
        parts = line.split(",")
        if len(parts) < Opcode65C02.parts_count:
            raise Exception("Can't fully parse line" + line)
        
        if len(parts[0].strip()) > 0:
            self.group_name = parts[0].strip()
            Opcode65C02.last_group = self.group_name
        else:
            self.group_name = Opcode65C02.last_group
        
        self.opcode = parts[1].strip()
        self.mnemonic = parts[2].strip()
        self.address_mode = parts[3].strip()
        self.bytes = parts[4].strip()
        self.cycles = parts[5].strip()
        self.flags = parts[6].strip()

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
            if c>'a' and c<'z':
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
