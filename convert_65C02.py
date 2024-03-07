from Cpu65C02.MarkdownWriter import *
from Cpu65C02.MergeFile import *

md = markdown_writer()
md.generate_tables()

mf = merge_file()
mf.merge(md.template_filename, md.output_merged_filename)
