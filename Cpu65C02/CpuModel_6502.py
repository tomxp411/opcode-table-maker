from .Opcode import *
from .Group import *
from .AddressModes import *

class cpu_model_65c02:
    def __init__(self):
        # Categories of instructions (Arithmetic, Test, Branch, Jump)
        self.categories = {}
        # Groups of instructions (add, sub, etc)
        self.groups = {}
        # Individual instructions
        self.opcodes = {}
        # Address modes: Immediate, Indirect, etc.
        self.address_modes = Address_Modes()
        self.init_address_modes()

    def init_address_modes(self):
        self.address_modes.add("IMM",  "Immediate",   "#$20")
        self.address_modes.add("IMM",  "Immediate",   "#$20")
        self.address_modes.add("ZP",   "Zero Page",   "$20")
        self.address_modes.add("ZPX",  "Zero Page,X", "$20,X")
        self.address_modes.add("ABS",  "Absolute",    "$8080")
        self.address_modes.add("ABSX", "Absolute,X",  "$8080,X")
        self.address_modes.add("ABSY", "Absolute,Y",  "$8080,Y")
        self.address_modes.add("INDX", "Indirect,X",  "($20,X)")
        self.address_modes.add("INDY", "Indirect,Y",  "($20),Y")
        self.address_modes.add("ZPI",  "ZP Indirect", "($20)")
        self.address_modes.add("ACC",  "Accumulator", "A")
        self.address_modes.add("ZPR",  "ZP Relative", "$20,$8080")
        self.address_modes.add("REL",  "Relative",    "$8080")
        self.address_modes.add("IMP",  "Implied",     "")
        self.address_modes.add("IND",  "Indirect",    "($8080)")
        self.address_modes.add("ZPY",  "Zero Page,Y", "$20,Y")

