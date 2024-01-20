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

        # Categories of instructions (Arithmetic, Test, Branch, Jump)
        self.categories = {}
        # Groups of instructions (add, sub, etc)
        self.groups = {}
        # Individual instructions
        self.opcodes = {}
        # Address modes: Immediate, Indirect, etc.
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
        cat = Group65C02()
        grp = Group65C02()
        Opcode65C02.address_modes = self.address_modes
        
        f = open(self.opcode_file,"r")
        for line in f:
            line_number += 1
            
            parts = [line]
            tt = ""
            # ! lines are CSV
            if line.startswith("!"):
                parts = line.split(",")
                tt = parts[0][1:].lower().strip()

            # Category
            # can be c,Name or
            # c,Name,OpcodeGroup,Description
            if tt == "c":
                # category
                val = parts[1]
                if not val in self.categories:
                    cat = Group65C02()
                    cat.name = val 
                    self.categories[val] = cat
                else:
                    cat = self.categories[val]
                # Mnemonic
                if len(parts) > 2:
                    val = parts[2]
                    if not val in self.groups:
                        grp = Group65C02()
                        grp.name = val 
                        self.groups[val] = grp
                    else:
                        grp = self.groups[val]
                # Description
                if len(parts) > 3:
                    grp.description = parts[3]

            # Opcode/Instruction
            elif tt == "o":
                op = Opcode65C02(line)
                op.group_name = grp.name
                op.category_name = cat.name
                self.opcodes[op.opcode] = op
                grp.opcodes.append(op)
                cat.opcodes.append(op)
            else:
                grp.add_comment(line)

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
        print(file=f)

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
        
        # Opcodes By Name 
        column_count = 16
        col_width = 5

        print(file=f)
        print("## Opcodes By Name",file=f)
        print(file=f)

        for i in range(0,column_count):
            print("|" + " ".rjust(col_width," "),file=f,end="")
        print("|", file=f)
        for i in range(0,column_count):
            print("|" + "-".rjust(col_width,"-"),file=f,end="")
        print("|", file=f)

        ocbn = {}
        for key,val in self.opcodes.items():
            if not val.mnemonic in ocbn:
                ocbn[val.mnemonic] = val
        ocs = sorted(ocbn)

        last = ""
        n = 0
        for key in ocs:
            oc = ocbn[key]
            t = oc.mnemonic
            skip = False
            if len(t) == 4:
                t=t[0:3]+"x"                
            if t == last:
                skip = True
            last=t

            if not skip:
                print("| [" + t + "](#" + self.groups[oc.group_name].anchor + ") ",
                    file=f,end="")
                n += 1
                if n > column_count - 1:
                    print("|",file=f)
                    n = 0

        if n != column_count - 1:
            print("|",file=f)

        # Opcodes By Category 
        column_count = 16
        col_width = 5

        print(file=f)
        print("## Opcodes By Category",file=f)
        print(file=f)

        for i in range(0,column_count):
            print("|" + " ".rjust(col_width," "),file=f,end="")
        print("|", file=f)
        for i in range(0,column_count):
            print("|" + "-".rjust(col_width,"-"),file=f,end="")
        print("|", file=f)

        for key,cat in self.categories.items():
            print("| ",cat.name,file=f,end=" ")

            last = ""
            n = 0
            for oc in cat.opcodes:
                t = oc.mnemonic.strip()
                skip = False

                if len(t) == 4:
                    t=t[0:3]+"x"                

                if t == last:
                    skip = True

                if not skip:
                    print("| [" + t + "](#" + self.groups[oc.group_name].anchor + ") ",
                        file=f,end="")
                    n += 1
                    if n > column_count - 1:
                        print("|",file=f)
                        print("|".ljust(col_width),end="",file=f)
                        n = 0
                last=t
            print("|",file=f)

        # Details
        column_names = ["SYNTAX","MODE","HEX","LEN","CYCLES","FLAGS"]
        column_width = [12,      14,     4,    4,    7,       8]
        
        groups_sorted = []
        for key in self.groups:
            groups_sorted.append(key)
        groups_sorted=sorted(groups_sorted)
        
        layout = 1
        # layout = 2

        for key in groups_sorted:
            grp = self.groups[key]
            print(file=f)
            #print("###",grp.name,"("+grp.mnemonics.strip()+")",file=f)
            print("###",grp.name,file=f)
            print(file=f)
            print(grp.description,file=f)
            print(file=f)
            if layout == 1:
                print("```text",file=f)
                for i in range(0,len(column_names)):
                    print(column_names[i].ljust(column_width[i]), end=" ", file=f)
                print(file=f)
            else:
                for i in range(0,len(column_names)):
                    #print(column_names[i].ljust(column_width[i]), end=" ", file=f)
                    print("|",column_names[i].ljust(column_width[i]),end=" ",file=f)
                print("|",file=f)
                for i in range(0,len(column_names)):
                    #print(column_names[i].ljust(column_width[i]), end=" ", file=f)
                    print("|","".ljust(column_width[i],"-"),end=" ",file=f)
                print("|",file=f)
            for op in grp.opcodes:
                if layout == 1:
                    # print("$" + op.opcode,op.flags,op.bytes,op.cycles,op.mnemonic,op.address_mode)
                    print(op.syntax.ljust(column_width[0]),
                        op.address_mode_name.ljust(column_width[1]),
                        ("$" + op.opcode).ljust(column_width[2]),
                        op.bytes.rjust(2).ljust(column_width[3]),
                        op.cycles.ljust(2).rjust(4).ljust(column_width[4]),
                        op.flags,op.comment,file=f)
                else:
                    print("|",op.syntax.ljust(column_width[0]),end=" ",file=f)
                    print("|",op.address_mode_name.ljust(column_width[1]),end=" ",file=f)
                    print("|",("$" + op.opcode).ljust(column_width[2]),end=" ",file=f)
                    print("|",op.bytes.rjust(2).ljust(column_width[3]),end=" ",file=f)
                    print("|",op.cycles.ljust(2).rjust(4).ljust(column_width[4]),end=" ",file=f)
                    print("|",op.flags,op.comment,end=" ",file=f)
                    print("|",file=f)
            if layout == 1:
                print("```",file=f)
            print(file=f)
            for c in grp.comments:
                print(c,file=f)
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
