from Cpu65C816.MarkdownWriter import *
from Cpu65C816.MergeFile import *

md = markdown_writer()
md.generate_tables()

mf = merge_file()
mf.merge(md.template_filename, md.output_merged_filename)
