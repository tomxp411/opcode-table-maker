#
# Opcode6502
#
# The definition of one opcode, including name (mnemonic) address mode, and
# so on.
# 
class Opcode:
    last_group = ""
    parts_count = 7
    address_modes = None
    
    def __init__(self):
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
