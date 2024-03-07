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
        self.details_file="CSV/Details65C816.md"
        self.output_file="Markdown/table_65C816.md"
        self.output_merged_filename="Markdown/X16 Reference - Appendix E - 65C816 Processor.md"

        self.cpu = None
        self.file = None

    def generate_tables(self):
        self.cpu = Cpu()
        self.cpu.load(self.opcode_file, self.category_file, self.modes_file, self.details_file)

        self.file = open(self.output_file, "w")
        self.write_opcodes_by_number()
        self.write_opcodes_by_name()
        self.write_opcodes_by_category()
        self.write_opcode_details()

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
                    print(self.anchor(self.cpu.opcodes[n].mnemonic),
                          end="|",file=self.file)
                else:
                    print("",end="|",file=self.file)
            print(file=self.file)
        print("",file=self.file)

    def write_opcodes_by_name(self):
        print("## Instructions By Name",file=self.file)
        print("",file=self.file)

        header = ["","","","","","","","","",""]
        self.write_header(header,13)
        c = 0
        for name,grp in self.cpu.groups.items():
            print("|",self.anchor(name), end=" ", file=self.file)
            c += 1
            if c % len(header) == 0:
                print("|",file=self.file)
        if c % len(header) != 0:
            print("|",file=self.file)
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

    def anchor(self, mnemonic:str):
        return "[" + mnemonic + "](#" + mnemonic.lower() + ")"

    def write_header_pre(self, items:list, col_width:list):
        for i in range(0,len(items)):
            print(items[i].ljust(col_width[i]," "),file=self.file,end="")
        print(file=self.file)

    def write_opcode_details(self):
        column_names = ["SYNTAX","MODE","HEX","LEN","CYCLES","FLAGS"]
        column_width = [15,      14,     4,    4,    12,       8]

        for name,grp in self.cpu.groups.items():
            print("###",name, end="\n\n", file=self.file)
            print("```text",file=self.file)
            self.write_header_pre(column_names, column_width)
            for oc in grp.opcodes:
                col = 0
                print(oc.syntax.ljust(column_width[col]," "),end="", file=self.file)
                col += 1
                print(oc.address_mode.ljust(column_width[col]," "),end="", file=self.file)
                col += 1
                print(oc.opcode.ljust(column_width[col]," "),end="", file=self.file)
                col += 1
                print(oc.bytes.ljust(column_width[col]," "),end="", file=self.file)
                col += 1
                print(oc.cycles.ljust(column_width[col]," "),end="", file=self.file)
                col += 1
                print(oc.flags.ljust(column_width[col]," "),end="", file=self.file)
                col += 1
                print(oc.comment,end="", file=self.file)

                print(file=self.file)
            print("```",end="\n\n",file=self.file)
            if name in self.cpu.details:
                print(self.cpu.details[name],file=self.file)
            print("[top](#instructions-by-opcode)",end="\n\n",file=self.file)


            
    