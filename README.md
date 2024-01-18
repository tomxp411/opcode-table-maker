# Opcode Table Maker

## Description 

OTM helps create tabular views of CPU opcodes, starting with a standard tex-delimited table.

For example: 

```
Group , Opcode , Mnemonic , Target , Address Mode , Bytes , Time , Flags    , Comments
LOAD  , $01    , LOAD     , A      , Addr         , 3     , 7    , N------Z , \
\Load a register from memory
\Sets N flag to bit 7
\Sets Z flag if loaded data is zero, Clears Z flag if data is non-zero
      , $02    , LOAD     , B      , Addr         , 3     , 7    , N------Z
```

This will be converted to a Markdown table, like this:

| -- | -0          | -1          | -2          | -3 
|----|-------------|-------------|-------------|----                                                                  
| 0- | BRK         | LOAD A,ADDR | LOAD B,ADDR | ...
| 1- | ...

It also creates a detailed listing, like this:

### LOAD

$01  N------Z  LOAD A,Addr
$02  N------Z  LOAD B,Addr

Load a register from memory
Sets N flag to bit 7
Sets Z flag if loaded data is zero. Clears Z flag if loaded data is non-zero.

## Merge Tokens

The script creates a stand-alone MD file with the output data, as well as a merged document with other descriptive text. 

`@opcode-table` will be replaced with the text from the table view.

`@opcode-list` will be replaced with the text from the list view.

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
Contact: wilsontp@gmail.com 
