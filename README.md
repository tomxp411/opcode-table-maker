# Opcode Table Maker

## Description

OTM helps create tabular views of CPU opcodes, starting with a standard tex-delimited table.

Input Format:

```csv
!c,Category, Mnemonic , Short Description
!h,Opcode , Mnemonic , Address Mode , Bytes , Time , Flags    
!o,0x00   , LDA      , IMM          , 2     , 2    , CZ---VN
Text description of opcode group
Multiple lines can be added to the description.
* Markdown features are supported in the text field.
- Like lists, **bold**, and _italics_.

Use semicolon break at the end to force a line break,;
like this.
```

**Group** is used to group opcodes that have the same (or similar) names.
For example, all LDA opcodes are in the same group. Opcodes like TAX, TAY, and
TXA can also be grouped together, since they perform the same function, just
with different register pairs.

## Output

The script generates a Markdown file with a table of instructions by name,
instructions by category, and an alphabetical listing of instructions, with
the address modes, sample syntax, number of bytes, execution timing, and
flags affected.

At the end of each detail table, the group's text will be printed, explaining
the operation of the instructions.

## Merge Tokens

The script creates a stand-alone MD file with the output data, as well as a
merged document, which can contain other text.

Your template should be a standard Markdown file, but can include an Include
directive to include other Markdown files.

`!include filename`

Will include the file named _filename_.

Note that the @ must be the first character on the line, and you may not have any non-whitespace characters after the merge token.

## Contributions

If you find an error in the opcode tables, we would appreciate a message via the Issues page. Feel free to submit a PR if you have
obvious and/or simple fixes. Also, feel free to submit PRs for other CPUs: We'd love to build a definitive table of all of the CPUs
commonly used in home computers during the 1975-1985 era.

## License

This product is being built for our personal use, but we are sharing with you in the hope you'll find it useful. We provide no warranty
of any kind.

Please read [License.md]. This is open source software, and you can use it for your own projects.
Factual data on this repository (ie: opcode listings) cannot be Copyrighted under US law and so are Public Domain.
All Copyright notices must be preserved in derivative versions, as follows:

(c) 2024 Tom Wilson, Tim Soderson  
Contact: [wilsontp@gmail.com](wilsontp@gmail.com) or file an Issue on the repo
here.
