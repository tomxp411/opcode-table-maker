#
# Addr65C02
#
# 6502 Address modes
#

class Address_Mode:
    def __init__(self):
        self.key = ""
        self.name = ""
        self.example = ""

class Address_Modes(dict):
    def __init__(self):
        pass 

    def add(self, key:str, name:str, example:str):
        m=Address_Mode()
        m.key = key
        m.name = name
        m.example = example

        self[key] = m 
    
