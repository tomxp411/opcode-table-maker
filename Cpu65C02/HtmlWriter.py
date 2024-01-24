from .Opcode import *
from .Group import *
from .CsvImport import *
from .AddressModes import *
from .HtmlTypes import *

from collections import deque
import os

class HtmlWriter_65C02:
    def __init__(self):
        # internal variables 
        self.hex_text="0123456789ABCDEF"

        self.last_group=""
        self.cpu = None # type: cpu_model_65c02()
        self.indent_level = 0
        self.indent_steps = 2
        self.file_handle = None # open(filename,"w")
        self.tags = []
        self.text = ""

        # filenames
        self.opcode_file        = "CSV/Opcodes65C02.csv"
        self.output_dir         = "Html"
        self.output_index       = "index_65C02.html"
        self.output_matrix      = "matrix_65C02.html"
        self.output_by_name     = "by_name_65C02.html"
        self.output_by_function = "by_function_65C02.html"

    def hex(self, value:int, digits:int = 2):
        s = hex(value).upper()
        s = s[2:]
        s = s[-digits:]
        s = s.rjust(digits, "0")
        return s

    def generate_tables(self):
        csv = csv_65C02()
        csv.load_csv(self.opcode_file)
        self.cpu = csv.cpu
        self.write_opcode_matrix()
        self.write_details()

    def write_file(self, filename:str, contents:str):
        self.file_handle = open(self.output_dir + "/" + filename,"w")
        # print(markup)
        print(contents,file=self.file_handle)
        self.file_handle.close()            

    def write_opcode_matrix(self):
        doc = html_document()
        doc.set_title("65C02 Opcode Matrix")
        body = doc.body

        style = doc.header.add("style")
        style.add_text(
            "table, th, td {"
            + "border: 1px solid;"
            + "border-collapse: collapse;"
            + "}")

        col_width = 12

        table = body.add("table")
        row = table.add("tr")
        row.add("th",text="&nbsp;")
        for c in range(0,16):
            row.add("th",text="x" + self.hex(c,1))

        for r in range(0,16):
            row = table.add("tr")
            row.add("td",text=self.hex(r,1) + "x")
            for c in range(0,16):
                key = self.hex(r,1)+self.hex(c,1)
                td = row.add("td")
                if key in self.cpu.opcodes:
                    oc=self.cpu.opcodes[key]
                    syntax = oc.syntax.replace(" ","&nbsp;")
                    href = self.get_opcode_url(oc.mnemonic)
                    a = html_anchor(href, syntax)
                    td.append(a)

        markup = doc.get_markup()
        self.write_file(self.output_matrix, markup)

    def write_details(self):
        # Details
        column_names = ["SYNTAX","MODE","HEX","LEN","CYCLES","FLAGS"]
        
        groups_sorted = []
        for key in self.cpu.groups:
            groups_sorted.append(key)
        groups_sorted=sorted(groups_sorted)
        
        layout = 1
        # layout = 2

        for key in groups_sorted:
            grp = self.cpu.groups[key]

            doc = html_document()
            doc.set_title("65C02 Opcode Details: " + grp.name)
            style = html_style()
            doc.header.append(style)
            style.add_style("th, td", "border", "none")
            style.add_style("th, td", "border-collapse", "collapse")
            style.add_style("th, td", "font-family", "'Lucida Console', 'Courier New', monospace")
            style.add_style("th, td", "padding-left", "8px")
            style.add_style("th, td", "padding-right", "8px")
            style.add_style(".number", "text-align", "center")
            body = doc.body

            body.add("h1",grp.description)

            t = body.add("table")
            tr = t.add("tr")
            for i in range(0,len(column_names)):
                th = tr.add("th",text=column_names[i])

            for op in grp.opcodes:
                tr = t.add("tr")
                tr.add("td", op.syntax)
                tr.add("td", op.address_mode_name)
                tr.add("td", "$" + op.opcode)
                tr.add("td", op.bytes, "number")
                tr.add("td", op.cycles, "number")
                tr.add("td", op.flags)
                tr.add("td", op.comment)

            p = body.add("p")
            for c in grp.comments:
                if len(c) == 0:
                    p = body.add("p")
                else:
                    p.add_text(c)

            p = body.add("p")
            a = html_anchor("#",text="<< Back")
            a.attributes["onclick"] = "history.back();"
            p.add(a)

            filename = self.get_opcode_filename(grp.name)
            self.write_file(filename, doc.get_markup())

    #     col_width = 12

    #     self.file_handle = open(self.output_dir + "/" + self.output_matrix,"w")
    #     self.write_header("Opcode Matrix")

    #     headers = ["&nbsp;"]
    #     for c in range(0,16):
    #         headers.append("x" + hex(c))

    #     self.table(headers=headers)
    #     for r in range(0,16):
    #         self.tr()
    #         self.td(hex(r)+"x")
    #         for c in range(0,16):
    #             key = hex(r)+hex(c)
    #             text = ""
    #             if key in self.cpu.opcodes:
    #                 oc=self.cpu.opcodes[key]
    #                 text = oc.syntax
    #             self.td(text)
    #         self.close_tag()
    #     self.close_tag()

    #     self.write_footer()
    #     self.file_handle.close()

        # for j in range(0,16):
        #     print("|" + hex[j]+"x".ljust(col_width),file=f,end="")
        #     for i in range(0,16):
        #         key = hex[j]+hex[i]
        #         text = ""
        #         if key in self.cpu.opcodes:
        #             oc=self.cpu.opcodes[key]
        #             text = "[" + oc.mnemonic + "](#" + self.cpu.groups[oc.group_name].anchor + ")"
        #         print("|" + text,file=f,end="")
        #     print("|", file=f)

        # # f.close()
        
        # # f = open(self.output_list,"w")
        
        # # Opcodes By Name 
        # column_count = 16
        # col_width = 5

        # print(file=f)
        # print("## Opcodes By Name",file=f)
        # print(file=f)

        # for i in range(0,column_count):
        #     print("|" + " ".rjust(col_width," "),file=f,end="")
        # print("|", file=f)
        # for i in range(0,column_count):
        #     print("|" + "-".rjust(col_width,"-"),file=f,end="")
        # print("|", file=f)

        # ocbn = {}
        # for key,val in self.cpu.opcodes.items():
        #     if not val.mnemonic in ocbn:
        #         ocbn[val.mnemonic] = val
        # ocs = sorted(ocbn)

        # last = ""
        # n = 0
        # for key in ocs:
        #     oc = ocbn[key]
        #     t = oc.mnemonic
        #     skip = False
        #     if len(t) == 4:
        #         t=t[0:3]+"x"                
        #     if t == last:
        #         skip = True
        #     last=t

        #     if not skip:
        #         print("| [" + t + "](#" + self.cpu.groups[oc.group_name].anchor + ") ",
        #             file=f,end="")
        #         n += 1
        #         if n > column_count - 1:
        #             print("|",file=f)
        #             n = 0

        # if n != column_count - 1:
        #     print("|",file=f)

        # # Opcodes By Category 
        # column_count = 16
        # col_width = 5

        # print(file=f)
        # print("## Opcodes By Category",file=f)
        # print(file=f)

        # for i in range(0,column_count):
        #     print("|" + " ".rjust(col_width," "),file=f,end="")
        # print("|", file=f)
        # for i in range(0,column_count):
        #     print("|" + "-".rjust(col_width,"-"),file=f,end="")
        # print("|", file=f)

        # for key,cat in self.cpu.categories.items():
        #     print("| ",cat.name,file=f,end=" ")

        #     last = ""
        #     n = 0
        #     for oc in cat.opcodes:
        #         t = oc.mnemonic.strip()
        #         skip = False

        #         if len(t) == 4:
        #             t=t[0:3]+"x"                

        #         if t == last:
        #             skip = True

        #         if not skip:
        #             print("| [" + t + "](#" + self.cpu.groups[oc.group_name].anchor + ") ",
        #                 file=f,end="")
        #             n += 1
        #             if n > column_count - 1:
        #                 print("|",file=f)
        #                 print("|".ljust(col_width),end="",file=f)
        #                 n = 0
        #         last=t
        #     print("|",file=f)

        # # Details
        # column_names = ["SYNTAX","MODE","HEX","LEN","CYCLES","FLAGS"]
        # column_width = [12,      14,     4,    4,    7,       8]
        
        # groups_sorted = []
        # for key in self.cpu.groups:
        #     groups_sorted.append(key)
        # groups_sorted=sorted(groups_sorted)
        
        # layout = 1
        # # layout = 2

        # for key in groups_sorted:
        #     grp = self.cpu.groups[key]
        #     print(file=f)
        #     #print("###",grp.name,"("+grp.mnemonics.strip()+")",file=f)
        #     print("###",grp.name,file=f)
        #     print(file=f)
        #     print(grp.description,file=f)
        #     print(file=f)
        #     if layout == 1:
        #         print("```text",file=f)
        #         for i in range(0,len(column_names)):
        #             print(column_names[i].ljust(column_width[i]), end=" ", file=f)
        #         print(file=f)
        #     else:
        #         for i in range(0,len(column_names)):
        #             #print(column_names[i].ljust(column_width[i]), end=" ", file=f)
        #             print("|",column_names[i].ljust(column_width[i]),end=" ",file=f)
        #         print("|",file=f)
        #         for i in range(0,len(column_names)):
        #             #print(column_names[i].ljust(column_width[i]), end=" ", file=f)
        #             print("|","".ljust(column_width[i],"-"),end=" ",file=f)
        #         print("|",file=f)
        #     for op in grp.opcodes:
        #         if layout == 1:
        #             # print("$" + op.opcode,op.flags,op.bytes,op.cycles,op.mnemonic,op.address_mode)
        #             print(op.syntax.ljust(column_width[0]),
        #                 op.address_mode_name.ljust(column_width[1]),
        #                 ("$" + op.opcode).ljust(column_width[2]),
        #                 op.bytes.rjust(2).ljust(column_width[3]),
        #                 op.cycles.ljust(2).rjust(4).ljust(column_width[4]),
        #                 op.flags,op.comment,file=f)
        #         else:
        #             print("|",op.syntax.ljust(column_width[0]),end=" ",file=f)
        #             print("|",op.address_mode_name.ljust(column_width[1]),end=" ",file=f)
        #             print("|",("$" + op.opcode).ljust(column_width[2]),end=" ",file=f)
        #             print("|",op.bytes.rjust(2).ljust(column_width[3]),end=" ",file=f)
        #             print("|",op.cycles.ljust(2).rjust(4).ljust(column_width[4]),end=" ",file=f)
        #             print("|",op.flags,op.comment,end=" ",file=f)
        #             print("|",file=f)
        #     if layout == 1:
        #         print("```",file=f)
        #     print(file=f)
        #     for c in grp.comments:
        #         print(c,file=f)
        #     print(file=f)
        #     print("---", file=f)
        #     print("[top](#)",file=f)
        #     print(file=f)

    def get_anchor(self, mnemonic:str):
        t = mnemonic.lower()
        t = t.replace(" ","-")
        return t

    def get_opcode_filename(self, mnemonic:str):
        t = mnemonic.lower()
        t = t.replace(" ","_")
        t = "detail_" + t + ".html"
        return t

    def get_opcode_url(self, mnemonic:str):
        return self.get_opcode_filename(mnemonic)
