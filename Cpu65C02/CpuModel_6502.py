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
        self.address_modes.add("IMM",  "Immediate",   "#$12")
        self.address_modes.add("IMM",  "Immediate",   "#$12")
        self.address_modes.add("ZP",   "Zero Page",   "$12")
        self.address_modes.add("ZPX",  "Zero Page,X", "$12,X")
        self.address_modes.add("ABS",  "Absolute",    "$1234")
        self.address_modes.add("ABSX", "Absolute,X",  "$1234,X")
        self.address_modes.add("ABSY", "Absolute,Y",  "$1234,Y")
        self.address_modes.add("INDX", "Indirect,X",  "($12,X)")
        self.address_modes.add("INDY", "Indirect,Y",  "($12),Y")
        self.address_modes.add("ZPI",  "ZP Indirect", "($12)")
        self.address_modes.add("ACC",  "Accumulator", "A")
        self.address_modes.add("ZPR",  "ZP Relative", "$12,$1234")
        self.address_modes.add("REL",  "Relative",    "$1234")
        self.address_modes.add("IMP",  "Implied",     "")
        self.address_modes.add("IND",  "Indirect",    "($1234)")
        self.address_modes.add("ZPY",  "Zero Page,Y", "$12,Y")

