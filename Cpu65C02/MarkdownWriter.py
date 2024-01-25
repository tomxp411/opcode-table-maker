#
# MarkdownWriter
# 

from .Opcode import *
from .Group import *
from .CsvImport import *
from .AddressModes import *
from .MergeFile import *

class markdown_writer:
    def __init__(self):
        #internal variables 
        self.last_group=""

        self.template_filename="Templates/template_65C02.md"
        self.opcode_file="CSV/Opcodes65C02.csv"
        self.output_table="Markdown/table_65C02.md"
        self.output_list="Markdown/list_65C02.md"
        self.output_merged_filename="Markdown/X16 Reference - Appendix C - 65C02 Processor.md"

        self.cpu = None # type: cpu_model_65c02()

    def generate_tables(self):
        csv = csv_65C02()
        csv.load_csv(self.opcode_file)
        self.cpu = csv.cpu
        self.write_table()

    def write_table(self):
        for g in self.cpu.groups.values():
            t = g.name.lower()
            t = t.replace(" ","-")
            t = t.replace("/","")
            g.anchor = t

        hex="0123456789ABCDEF"
        col_width = 12

        f = open(self.output_table,"w")
        print("## Instructions By Number",file=f)
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
                if key in self.cpu.opcodes:
                    oc=self.cpu.opcodes[key]
                    text = "[" + oc.mnemonic + "](#" + self.cpu.groups[oc.group_name].anchor + ")"
                print("|" + text,file=f,end="")
            print("|", file=f)

        # f.close()
        
        # f = open(self.output_list,"w")
        
        # Opcodes By Name 
        column_count = 16
        col_width = 5

        print(file=f)
        print("## Instructions By Name",file=f)
        print(file=f)

        for i in range(0,column_count):
            print("|" + " ".rjust(col_width," "),file=f,end="")
        print("|", file=f)
        for i in range(0,column_count):
            print("|" + "-".rjust(col_width,"-"),file=f,end="")
        print("|", file=f)

        ocbn = {}
        for key,val in self.cpu.opcodes.items():
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
                print("| [" + t + "](#" + self.cpu.groups[oc.group_name].anchor + ") ",
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
        print("## Instructions By Category",file=f)
        print(file=f)

        for i in range(0,column_count):
            print("|" + " ".rjust(col_width," "),file=f,end="")
        print("|", file=f)
        for i in range(0,column_count):
            print("|" + "-".rjust(col_width,"-"),file=f,end="")
        print("|", file=f)

        for key,cat in self.cpu.categories.items():
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
                    print("| [" + t + "](#" + self.cpu.groups[oc.group_name].anchor + ") ",
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
        for key in self.cpu.groups:
            groups_sorted.append(key)
        groups_sorted=sorted(groups_sorted)
        
        layout = 1
        # layout = 2

        for key in groups_sorted:
            grp = self.cpu.groups[key]
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

