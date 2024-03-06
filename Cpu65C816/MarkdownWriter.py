#
# MarkdownWriter
# 

from .CsvFile import *
from .Opcode import *
from .OpcodeGroup import *
from .Cpu import *
from .AddressModes import *
from .MergeFile import *

class markdown_writer:
    def __init__(self):
        #internal variables 
        self.last_group=""

        self.hex_digits = "0123456789ABCDEF"

        self.template_filename="Templates/template_65C816.md"
        self.opcode_file="CSV/Opcodes65C816.csv"
        self.category_file="CSV/Groups65C816.csv"
        self.modes_file="CSV/Modes65C816.csv"
        self.output_file="Markdown/table_65C816.md"
        self.output_merged_filename="Markdown/X16 Reference - Appendix E - 65C816 Processor.md"

        self.cpu = None
        self.file = None

    def generate_tables(self):
        self.cpu = Cpu()
        self.cpu.load(self.opcode_file, self.category_file, self.modes_file)

        self.file = open(self.output_file, "w")
        self.write_opcodes_by_number()
        self.write_opcodes_by_category()

    def write_opcodes_by_number(self):
        print("## Instructions By Opcode",file=self.file)
        print("",file=self.file)

        hex_header = ["", "x0","x1","x2","x3","x4","x5","x6","x7",
                      "x8","x9","xA","xB","xC","xD","xE","xF"]
        self.write_header(hex_header, 11)
        
        for y in self.hex_digits:
            print("|        " + y + "x ",end="|",file=self.file)
            for x in self.hex_digits:
                n = y + x
                if n in self.cpu.opcodes:
                    print("[" + self.cpu.opcodes[n].mnemonic + "](#" + 
                          self.cpu.opcodes[n].mnemonic + ")",
                          end="|",file=self.file)
                else:
                    print("",end="|",file=self.file)
            print(file=self.file)
        print("",file=self.file)

    def write_opcodes_by_category(self):
        print("## Instructions By Category",file=self.file)
        print("",file=self.file)

        header = ["Category","Instructions"]
        self.write_header(header,15)
        for name,cat in self.cpu.categories.items():
            print("|",name.ljust(13),"|",self.anchor(cat[0]), end="", file=self.file)
            for n in range(1,len(cat)):
                print(" ,",self.anchor(cat[n]),end="",file=self.file)
            print(" |",file=self.file)
        print("",file=self.file)

    def write_header(self, items:list, col_width:int):
        for i in range(0,len(items)):
            print("|"+items[i].ljust(col_width," "),file=self.file,end="")
        print("|", file=self.file)
        for i in range(0,len(items)):
            print("|" + "-".ljust(col_width,"-"),file=self.file,end="")
        print("|", file=self.file)

    def anchor(self, mnemonic):
        return "[" + mnemonic + "](#" + mnemonic + ")"
