class OpcodeGroup:
    def __init__(self):
        self.name = ""     # group name: Add, And, Jump
        self.anchor = ""
        self.description = ""
        self.comments = [] # array of strings
        self.opcodes = []
