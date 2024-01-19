#
# merge_65c02
# 

from .Opcode65c02 import *
from .Group65C02 import *
from .Address_Modes import *

class Cpu65c02:
    def __init__(self):
        #internal variables 
        self.last_group=""

        self.template_file="Templates/template_65C02.md"
        self.opcode_file="CSV/Opcodes65C02.csv"
        self.output_table="Output/table_65C02.md"
        self.output_list="Output/list_65C02.md"
        self.output_merged="Output/Opcodes_65C02.md"

        self.opcodes = {}
        self.groups = {}
        self.address_modes = Address_Modes()
    
        self.init_address_modes()

    def merge(self, 
              template_file=None, 
              opcode_file=None, 
              output_table=None,
              output_list=None,
              output_merged=None):
        
        self.load_csv()

    # read the CPU opcodes from the CSV file
    # format is:
    # Group,opcode,mnemonic,address mode,bytes,cycles,flags
    # or 
    # #Descriptive text 
    def load_csv(self):
        line_number = 0
        group = Group65C02()
        
        f = open(self.opcode_file,"r")
        for line in f:
            line = line.strip()
            line_number += 1
            # skip header line
            if line_number == 1:
                pass
            elif len(line) < 1:
                pass 
            elif line.startswith("#"):
                group.add_comment(line)
            else:
                op = Opcode65C02(line)
                if op.valid:
                    if op.group_name != group.name:
                        group = Group65C02()
                        group.name = op.group_name
                        self.groups[group.name] = group
                    self.opcodes[op.opcode] = op
                    group.add_mnemonic(op.mnemonic)
                    group.opcodes.append(op)
        f.close()

        for g in self.groups.values():
            t = g.name.lower()
            t = t.replace(" ","-")
            t = t.replace("/","")
            g.anchor = t

        hex="0123456789ABCDEF"
        col_width = 12

        f = open(self.output_table,"w")
        print("## Opcodes By Number",file=f)

        #header
        print("|" + " ".ljust(col_width),file=f,end="")
        for i in range(0,16):
            print("| x" + hex[i].ljust(col_width-1," "),file=f,end="")
        print("|", file=f)

        print("|" + "-".ljust(col_width,"-"),file=f,end="")
        for i in range(0,16):
            print("|" + "-".rjust(col_width,"-"),file=f,end="")
        print("|", file=f)

        for j in range(0,16):
            print("|" + hex[j]+"x".ljust(col_width),file=f,end="")
            for i in range(0,16):
                key = hex[j]+hex[i]
                text = ""
                if key in self.opcodes:
                    oc=self.opcodes[key]
                    text = "[" + oc.mnemonic + "](#" + self.groups[oc.group_name].anchor + ")"
                print("|" + text,file=f,end="")
            print("|", file=f)

        # f.close()
        
        # f = open(self.output_list,"w")
        
        column_names = ["SYNTAX","HEX","LEN","CYCLES","FLAGS"]
        column_width =  [12,      4,    4,    7,       8]

        print("## Opcodes By name",file=f)
        print(file=f)
        last = "" 
        for oc in self.opcodes.values():
            t = oc.mnemonic.strip()
            skip = False

            if len(t) == 4:
                t=t[0:3]+"x"                

            if t == last:
                skip = True

            if not skip:
                print("[" + t + "](#" + self.groups[oc.group_name].anchor + ")",
                    file=f)
            last=t

        for grp in self.groups.values():
            print(file=f)
            #print("###",grp.name,"("+grp.mnemonics.strip()+")",file=f)
            print("###",grp.name,file=f)
            print(file=f)
            print("```text",file=f)
            for i in range(0,len(column_names)):
                print(column_names[i].ljust(column_width[i]), end=" ", file=f)
            print(file=f)
            for op in grp.opcodes:
                # print("$" + op.opcode,op.flags,op.bytes,op.cycles,op.mnemonic,op.address_mode)
                print((op.mnemonic + " " + self.address_modes[op.address_mode].example).ljust(column_width[0]),
                    ("$" + op.opcode).ljust(column_width[1]),
                    op.bytes.ljust(column_width[2]),
                    op.cycles.rjust(4).ljust(column_width[3]),
                    op.flags,file=f)
            print("```",file=f)
            print(file=f)
            for c in grp.comments:
                 print(c,"<br/>",file=f)
            print(file=f)
            print("---", file=f)
            print("[top](#)",file=f)
            print(file=f)

    def init_address_modes(self):
        self.address_modes.add("IMM",  "Immediate","#$12")
        self.address_modes.add("IMM",  "Immediate","#$12")
        self.address_modes.add("ZP",   "Zero Page","$12")
        self.address_modes.add("ZPX",  "Zero Page,X", "$12,X")
        self.address_modes.add("ABS",  "Absolute", "$1234")
        self.address_modes.add("ABSX", "Absolute,X", "$1234,X")
        self.address_modes.add("ABSY", "Absolute,Y", "$1234,Y")
        self.address_modes.add("INDX", "Indirect,X", "($12,X)")
        self.address_modes.add("INDY", "Indirect,Y", "($12),Y")
        self.address_modes.add("ZPI",  "ZP Indirect", "($12)")
        self.address_modes.add("ACC",  "Accumulator", "A")
        self.address_modes.add("ZPR",  "ZP Relative", "$1234")
        self.address_modes.add("REL",  "Relative", "$1234")
        self.address_modes.add("IMP",  "Implied", "")
        self.address_modes.add("IND",  "Indirect", "($1234)")
        self.address_modes.add("ZPY",  "Zero Page,Y", "$12,Y")
