class merge_file():
    INCLUDE_TOKEN = "!include "

    def __init__(self):
        self.template_filename = ""
        self.output_filename = ""
    
    def merge(self, template_filename, output_filename):
        self.template_file = template_filename
        self.output_merged = output_filename

        lines = []
        f_template = open(self.template_file,"r")
        foutput = open(self.output_merged,"w")
        for tline in f_template:
            if tline.startswith(self.INCLUDE_TOKEN):
                filename = tline[len(self.INCLUDE_TOKEN):].strip()
                f_include = open(filename,"r")
                for inc_line in f_include:
                    foutput.write(inc_line)
            else:
                foutput.write(tline)
        f_template.close()
        foutput.close()

    def include(self, lines:list, filename:str):
        f = open(filename,"r")
        # include_text = f.read()
        # lines.append(include_text)
        for line in f:
            lines.append(line)
        f.close()