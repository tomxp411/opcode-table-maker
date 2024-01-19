class Group65C02:
    def __init__(self):
        self.name = ""     # group name: Add, And, Jump
        self.mnemonics = "" # all mnemonics in group
        self.anchor = ""
        self.description = ""
        self.comments = [] # array of strings
        self.opcodes = []

    def add_comment(self, text:str):
        s = text

        # need special handling for quoted text
        q1=text.find("\"")
        if q1 < 0:
            parts = text.split(",")
            if len(parts)>0:
                s = parts[1]
        else:
            q2 = text.find("\"",q1+1)
            if q2 > 0:
                s = text[q1+1:q2]
            else:
                s = text[q1+1]
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
