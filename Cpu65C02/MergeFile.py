class merge_file():
    INCLUDE_TOKEN = "!include "

    def __init__(self):
        self.template_filename = ""
        self.output_filename = ""
    
    def merge(self, template_filename, output_filename):
        self.template_file = template_filename
        self.output_merged = output_filename

        lines = []
        f = open(self.template_file,"r")
        for tline in f:
            if tline.startswith(self.INCLUDE_TOKEN):
                self.include(tline[len(self.INCLUDE_TOKEN):].strip(), 
                             lines)
            else:
                lines.append(tline)
        f.close()

        foutput = open(self.output_merged,"w")
        for line in lines:
            foutput.write(line)
        foutput.close()

    def include(self, filename:str, lines:list):
        f = open(filename,"r")
        for line in f:
            lines.append(line)
        f.close()