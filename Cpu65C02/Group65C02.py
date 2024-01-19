class Group65C02:
    def __init__(self):
        self.name = ""     # group name: Add, And, Jump
        self.mnemonics = "" # all mnemonics in group
        self.anchor = ""
        self.opcodes = []  # array of opcodes
        self.comments = [] # array of strings


    def add_comment(self, text):
        s = text
        if text.startswith("#"):
            s = text[1:len(text)].strip()
        elif text.startswith("\"#"):
            s = text[2:len(text)].strip()
        self.comments.append(s)

    def add_mnemonic(self, text):
        t = text + " "
        if not t in self.mnemonics:
            self.mnemonics += t
        
        if self.name == "Branch on Bit":
            self.mnemonics = "BBRx BBSx"
        elif self.name == "RMB":
            self.mnemonics = "RMBx"
        elif self.name == "SMB":
            self.mnemonics = "SMBx"
