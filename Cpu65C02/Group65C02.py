class Group65C02:
    def __init__(self):
        self.name = ""     # group name: Add, And, Jump
        self.mnemonics = "" # all mnemonics in group
        self.anchor = ""
        self.description = ""
        self.comments = [] # array of strings
        self.opcodes = []

    def add_comment(self, text:str):
        text = text.strip("\r\n")
        if text.endswith(";"):
            text=text[:len(text)-1] + "<br/>"
        self.comments.append(text)

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
