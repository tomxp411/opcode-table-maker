
# Appendix C: The 65C02 Processor

[Click here for the opcode listing](#instruction-tables)

This is not meant to be a complete manual on the 65C816 processor. This is a
reference. Much of this information comes from 6502.org, undisbeliever.net, and
[Programming the 65816: Including the 6502, 65C02, and
65802](https://www.amazon.com/Programming-65816-Including-65C02-65802/dp/0893037893)
by David Eyes and Ron Lichty.

## Overviewv

The WDC65C816 CPU is an 8/16 bit CPU and a follow-up to the 6502 processor. It
uses the same basic instructions, with additional 16-bit instructions and
several new address modes. It also includes two block move instructions, which
are handy for copying large amounts of memory around the system.

The CPU has 16-bit wide registers. In addition, Zero Page has been renamed to
Direct Page and, along with the Stack, can be moved anywhere in the first 64K of
RAM.

## Compatibility with the 65C02

The 65C916 CPU is generally compatible with the 65C02 instruction set, with the
exception  of the `BBRx`, `BBSx`, `RMBx`, and `SMBx` instructions.

## Registers

The 65C816 has some additional registers, mostly dealing with banking. The .A,
.X, and .Y registers are also upgrade to 16 bits when in native mode and the .m
and .x flags are clear.

| Notation   | Name             | Description     |
|------------|------------------|-----------------|
| .A         | Accumulator      | The accumulator. It stores the result of moth math and logical operations.  |
| .X         | X Index          | .X is mostly used as a counter and to offset addresses with X indexed modes |
| .Y         | Y Index          | .Y is mostly used as a counter and to offset addresses with Y indexed modes |
| .S         | Stack Pointer    | SP points to the next open position on the stack.                           |
| DBR / .K   | Data Bank        | Data bank is the default bank for operations that use a 16 bit address.     |
| .PB / PBR  | Program Bank     | The default address for 16 bit JMP and JSR oprerations. Can only be set with a 24 bit JMP or JSR. |
| .P         | Processor Status | The flags. |
| PC         | Program Counter  | The address of the current CPU instruction |

## Status Flags

Flags are stored as the P register. PHP, PLP, SEP, and REP instructions can
modify the flags. They can be tested with the various Branch instructions

The e flag can only be set with the XCE instruction, which swaps the Carry flag
and the Emulation flag.

Depending on the CPU mode, there are two configurations. (Note that on the
65C816, the flag names are written in *lower case*, to avoid confusion with
overlapping CPU register names.)

In Emulation mode, the flags follow the 65C02 convention. In Native mode (e=1),
the flags are as follows:

`nvmx dizc e`

  n = Negative  
  v = oVerflow  
  m = Memory width (0=16 bit, 1=8 bit)  
  x = Index register width (0=16 bit, 1=8 bit)  
  d = Decimal Mode  
  i = Interupts Disabled  
  z = Zero  
  c = Carry  
  e = Emulation Mode (0=65C02 mode, 1=65C816 mode)

## Address Modes

The 65C816 now has 24 discinct address modes, although most are veriations on a
theme. Make note of the new syntax for Stack relative instructions (,S), the use
of brackets for [24 bit indirect] addressing, and the fact that Zero Page has
been renamed to Direct Page. This means that $0001 and $01 are now two different
addresses (although they would be the same if .DP is set to $00.

| Mode                            | Syntax    | Description |
| ------------------------------- | --------- | ------------------------------------------------------------------ |
| Immediate                       | #$12      | Value is supplied in the program stream                            |
| Absolute                        | $1234     | Data is at this address.                                           |
| Absolute X Indexed              | $1234,X   | Address is offset by X. If X=2 this is $1236.                      |
| Absolute Y Indexed              | $1234,Y   | Address is offset by X. If Y=2 this is $1236.                      |
| Direct                          | $12       | Direct Page address. Operand is 1 byte.                            |
| Direct X Indexed                | $12,X     | Address on Direct Page is offset by .X                             |
| Direct Y Indexed                | $12,Y     | Address on Direct Page is offset by .Y                             |
| Direct Indirect                 | ($12)     | Value at $12 is a 16-bit address.                                  |
| Direct Indirect Y Indexed       | ($12),Y   | Resolve pointer at $12 then offset by Y.                           |
| Direct X Indexed Indirect       | ($12,X)   | Start at $12, offset by X, then read that address.                 |
| Direct Indirect Long            | [$12]     | 24 bit pointer on Direct Page.                                     |
| Direct Indrect Long Y Indexed   | [$12],Y   | Resolve address at $12, then offset by Y.                          |
| Indirect                        | ($1234)   | Read pointer at $1234 and get data from the resultant address      |
| Indirect X Indexed              | ($1234,X) | Read pointer at $1234 offset by X, get data from resultant address |
| Indirect Long                   | [$1234]   | Pointer is a 24-bit address.                                       |
| Absolute Long                   | $123456   | 24 bit address.                                                    |
| Absolute Indexed Long           | $123456,X | 24 bit address, offset by X.                                       |
| Stack Relative Indexed          | $12,S     | Stack relative.                                                    |
| Stack Relative Indirect Indexed | ($12,S),Y | Resolve Pointer at $12, then offset by Y.                          |
| Accumulator (implied)           |           | Operation acts on .A                                               |
| Implied                         |           | Target is part of the opcode name.                                 |
| Relative Address (8 bit signed) | $1234     | Branches can only jump by -128 to 127 bytes.                       |
| 16 bit relative address         | 1234      | BRL can jump by 32K bytes.                                         |
| Block Move                      | #$12,#$34 | Operands are the bank numbers for block move/copy.                 |

## Instruction Tables

## Instructions By Opcode

|           |x0         |x1         |x2         |x3         |x4         |x5         |x6         |x7         |x8         |x9         |xA         |xB         |xC         |xD         |xE         |xF         |
|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|
|        0x |[BRK](#BRK)|[ORA](#ORA)|[COP](#COP)|[ORA](#ORA)|[TSB](#TSB)|[ORA](#ORA)|[ASL](#ASL)|[ORA](#ORA)|[PHP](#PHP)|[ORA](#ORA)|[ASL](#ASL)|[PHD](#PHD)|[TSB](#TSB)|[ORA](#ORA)|[ASL](#ASL)|[ORA](#ORA)|
|        1x |[BPL](#BPL)|[ORA](#ORA)|[ORA](#ORA)|[ORA](#ORA)|[TRB](#TRB)|[ORA](#ORA)|[ASL](#ASL)|[ORA](#ORA)|[CLC](#CLC)|[ORA](#ORA)|[INC](#INC)|[TCS](#TCS)|[TRB](#TRB)|[ORA](#ORA)|[ASL](#ASL)|[ORA](#ORA)|
|        2x |[JSR](#JSR)|[AND](#AND)|[JSL](#JSL)|[AND](#AND)|[BIT](#BIT)|[AND](#AND)|[ROL](#ROL)|[AND](#AND)|[PLP](#PLP)|[AND](#AND)|[ROL](#ROL)|[PLD](#PLD)|[BIT](#BIT)|[AND](#AND)|[ROL](#ROL)|[AND](#AND)|
|        3x |[BMI](#BMI)|[AND](#AND)|[AND](#AND)|[AND](#AND)|[BIT](#BIT)|[AND](#AND)|[ROL](#ROL)|[AND](#AND)|[SEC](#SEC)|[AND](#AND)|[DEC](#DEC)|[TSC](#TSC)|[BIT](#BIT)|[AND](#AND)|[ROL](#ROL)|[AND](#AND)|
|        4x |[RTI](#RTI)|[EOR](#EOR)|[WDM](#WDM)|[EOR](#EOR)|[MVP](#MVP)|[EOR](#EOR)|[LSR](#LSR)|[EOR](#EOR)|[PHA](#PHA)|[EOR](#EOR)|[LSR](#LSR)|[PHK](#PHK)|[JMP](#JMP)|[EOR](#EOR)|[LSR](#LSR)|[EOR](#EOR)|
|        5x |[BVC](#BVC)|[EOR](#EOR)|[EOR](#EOR)|[EOR](#EOR)|[MVN](#MVN)|[EOR](#EOR)|[LSR](#LSR)|[EOR](#EOR)|[CLI](#CLI)|[EOR](#EOR)|[PHY](#PHY)|[TCD](#TCD)|[JMP](#JMP)|[EOR](#EOR)|[LSR](#LSR)|[EOR](#EOR)|
|        6x |[RTS](#RTS)|[ADC](#ADC)|[PER](#PER)|[ADC](#ADC)|[STZ](#STZ)|[ADC](#ADC)|[ROR](#ROR)|[ADC](#ADC)|[PLA](#PLA)|[ADC](#ADC)|[ROR](#ROR)|[RTL](#RTL)|[JMP](#JMP)|[ADC](#ADC)|[ROR](#ROR)|[ADC](#ADC)|
|        7x |[BVS](#BVS)|[ADC](#ADC)|[ADC](#ADC)|[ADC](#ADC)|[STZ](#STZ)|[ADC](#ADC)|[ROR](#ROR)|[ADC](#ADC)|[SEI](#SEI)|[ADC](#ADC)|[PLY](#PLY)|[TDC](#TDC)|[JMP](#JMP)|[ADC](#ADC)|[ROR](#ROR)|[ADC](#ADC)|
|        8x |[BRA](#BRA)|[STA](#STA)|[BRL](#BRL)|[STA](#STA)|[STY](#STY)|[STA](#STA)|[STX](#STX)|[STA](#STA)|[DEY](#DEY)|[BIT](#BIT)|[TXA](#TXA)|[PHB](#PHB)|[STY](#STY)|[STA](#STA)|[STX](#STX)|[STA](#STA)|
|        9x |[BCC](#BCC)|[STA](#STA)|[STA](#STA)|[STA](#STA)|[STY](#STY)|[STA](#STA)|[STX](#STX)|[STA](#STA)|[TYA](#TYA)|[STA](#STA)|[TXS](#TXS)|[TXY](#TXY)|[STZ](#STZ)|[STA](#STA)|[STZ](#STZ)|[STA](#STA)|
|        Ax |[LDY](#LDY)|[LDA](#LDA)|[LDX](#LDX)|[LDA](#LDA)|[LDY](#LDY)|[LDA](#LDA)|[LDX](#LDX)|[LDA](#LDA)|[TAY](#TAY)|[LDA](#LDA)|[TAX](#TAX)|[PLB](#PLB)|[LDY](#LDY)|[LDA](#LDA)|[LDX](#LDX)|[LDA](#LDA)|
|        Bx |[BCS](#BCS)|[LDA](#LDA)|[LDA](#LDA)|[LDA](#LDA)|[LDY](#LDY)|[LDA](#LDA)|[LDX](#LDX)|[LDA](#LDA)|[CLV](#CLV)|[LDA](#LDA)|[TSX](#TSX)|[TYX](#TYX)|[LDY](#LDY)|[LDA](#LDA)|[LDX](#LDX)|[LDA](#LDA)|
|        Cx |[CPY](#CPY)|[CMP](#CMP)|[REP](#REP)|[CMP](#CMP)|[CPY](#CPY)|[CMP](#CMP)|[DEC](#DEC)|[CMP](#CMP)|[INY](#INY)|[CMP](#CMP)|[DEX](#DEX)|[WAI](#WAI)|[CPY](#CPY)|[CMP](#CMP)|[DEC](#DEC)|[CMP](#CMP)|
|        Dx |[BNE](#BNE)|[CMP](#CMP)|[CMP](#CMP)|[CMP](#CMP)|[PEI](#PEI)|[CMP](#CMP)|[DEC](#DEC)|[CMP](#CMP)|[CLD](#CLD)|[CMP](#CMP)|[PHX](#PHX)|[STP](#STP)|[JMP](#JMP)|[CMP](#CMP)|[DEC](#DEC)|[CMP](#CMP)|
|        Ex |[CPX](#CPX)|[SBC](#SBC)|[SEP](#SEP)|[SBC](#SBC)|[CPX](#CPX)|[SBC](#SBC)|[INC](#INC)|[SBC](#SBC)|[INX](#INX)|[SBC](#SBC)|[NOP](#NOP)|[XBA](#XBA)|[CPX](#CPX)|[SBC](#SBC)|[INC](#INC)|[SBC](#SBC)|
|        Fx |[BEQ](#BEQ)|[SBC](#SBC)|[SBC](#SBC)|[SBC](#SBC)|[PEA](#PEA)|[SBC](#SBC)|[INC](#INC)|[SBC](#SBC)|[SED](#SED)|[SBC](#SBC)|[PLX](#PLX)|[XCE](#XCE)|[JSR](#JSR)|[SBC](#SBC)|[INC](#INC)|[SBC](#SBC)|

## Instructions By Name

|             |             |             |             |             |             |             |             |             |             |
|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|
| [ADC](#ADC) | [AND](#AND) | [ASL](#ASL) | [BCC](#BCC) | [BCS](#BCS) | [BEQ](#BEQ) | [BIT](#BIT) | [BMI](#BMI) | [BNE](#BNE) | [BPL](#BPL) |
| [BRA](#BRA) | [BRK](#BRK) | [BRL](#BRL) | [BVC](#BVC) | [BVS](#BVS) | [CLC](#CLC) | [CLD](#CLD) | [CLI](#CLI) | [CLV](#CLV) | [CMP](#CMP) |
| [COP](#COP) | [CPX](#CPX) | [CPY](#CPY) | [DEC](#DEC) | [DEX](#DEX) | [DEY](#DEY) | [EOR](#EOR) | [INC](#INC) | [INX](#INX) | [INY](#INY) |
| [JMP](#JMP) | [JSL](#JSL) | [JSR](#JSR) | [LDA](#LDA) | [LDX](#LDX) | [LDY](#LDY) | [LSR](#LSR) | [MVN](#MVN) | [MVP](#MVP) | [NOP](#NOP) |
| [ORA](#ORA) | [PEA](#PEA) | [PEI](#PEI) | [PER](#PER) | [PHA](#PHA) | [PHB](#PHB) | [PHD](#PHD) | [PHK](#PHK) | [PHP](#PHP) | [PHX](#PHX) |
| [PHY](#PHY) | [PLA](#PLA) | [PLB](#PLB) | [PLD](#PLD) | [PLP](#PLP) | [PLX](#PLX) | [PLY](#PLY) | [REP](#REP) | [ROL](#ROL) | [ROR](#ROR) |
| [RTI](#RTI) | [RTL](#RTL) | [RTS](#RTS) | [SBC](#SBC) | [SEC](#SEC) | [SED](#SED) | [SEI](#SEI) | [SEP](#SEP) | [STA](#STA) | [STP](#STP) |
| [STX](#STX) | [STY](#STY) | [STZ](#STZ) | [TAX](#TAX) | [TAY](#TAY) | [TCD](#TCD) | [TCS](#TCS) | [TDC](#TDC) | [TRB](#TRB) | [TSB](#TSB) |
| [TSC](#TSC) | [TSX](#TSX) | [TXA](#TXA) | [TXS](#TXS) | [TXY](#TXY) | [TYA](#TYA) | [TYX](#TYX) | [WAI](#WAI) | [WDM](#WDM) | [XBA](#XBA) |
| [XCE](#XCE) |

## Instructions By Category

|Category       |Instructions   |
|---------------|---------------|
| Arithmetic    | [ADC](#ADC) , [SBC](#SBC) |
| Boolean       | [AND](#AND) , [EOR](#EOR) , [ORA](#ORA) |
| Shift         | [ASL](#ASL) , [LSR](#LSR) , [ROL](#ROL) , [ROR](#ROR) |
| Branch        | [BCC](#BCC) , [BCS](#BCS) , [BEQ](#BEQ) , [BMI](#BMI) , [BNE](#BNE) , [BPL](#BPL) , [BRA](#BRA) , [BRK](#BRK) , [BRL](#BRL) , [BVC](#BVC) , [BVS](#BVS) |
| Test          | [BIT](#BIT) , [TRB](#TRB) , [TSB](#TSB) |
| Flags         | [CLC](#CLC) , [CLD](#CLD) , [CLI](#CLI) , [CLV](#CLV) , [REP](#REP) , [SEC](#SEC) , [SED](#SED) , [SEI](#SEI) , [SEP](#SEP) |
| Compare       | [CMP](#CMP) , [CPX](#CPX) , [CPY](#CPY) |
| Interrupt     | [COP](#COP) , [WAI](#WAI) |
| Inc/Dec       | [DEC](#DEC) , [DEX](#DEX) , [DEY](#DEY) , [INC](#INC) , [INX](#INX) , [INY](#INY) |
| Flow          | [JMP](#JMP) , [JSL](#JSL) , [JSR](#JSR) , [NOP](#NOP) , [RTI](#RTI) , [RTL](#RTL) , [RTS](#RTS) , [WDM](#WDM) |
| Load          | [LDA](#LDA) , [LDX](#LDX) , [LDY](#LDY) |
| Block Move    | [MVN](#MVN) , [MVP](#MVP) |
| Stack         | [PEA](#PEA) , [PEI](#PEI) , [PER](#PER) , [PHA](#PHA) , [PHB](#PHB) , [PHD](#PHD) , [PHK](#PHK) , [PHP](#PHP) , [PHX](#PHX) , [PHY](#PHY) , [PLA](#PLA) , [PLB](#PLB) , [PLD](#PLD) , [PLP](#PLP) , [PLX](#PLX) , [PLY](#PLY) |
| Store         | [STA](#STA) , [STP](#STP) , [STX](#STX) , [STY](#STY) , [STZ](#STZ) |
| Register Swap | [TAX](#TAX) , [TAY](#TAY) , [TCD](#TCD) , [TCS](#TCS) , [TDC](#TDC) , [TSC](#TSC) , [TSX](#TSX) , [TXA](#TXA) , [TXS](#TXS) , [TXY](#TXY) , [TYA](#TYA) , [TYX](#TYX) , [XBA](#XBA) , [XCE](#XCE) |

### ADC

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
ADC #$54       imm           69  3-m 3-m         nv....zc .
ADC $10        dir           65  2   4-m+w       nv....zc .
ADC $10,X      dir,X         75  2   5-m+w       nv....zc .
ADC $32,S      stk,S         63  2   5-m         nv....zc .
ADC $9876      abs           6D  3   5-m         nv....zc .
ADC $9876,X    abs,X         7D  3   6-m-x+x*p   nv....zc .
ADC $9876,Y    abs,Y         79  3   6-m-x+x*p   nv....zc .
ADC $FEDBCA    long          6F  4   6-m         nv....zc .
ADC $FEDCBA,X  long,X        7F  4   6-m         nv....zc .
ADC ($10)      (dir)         72  2   6-m+w       nv....zc .
ADC ($10),Y    (dir),Y       71  2   7-m+w-x+x*p nv....zc .
ADC ($10,X)    (dir,X)       61  2   7-m+w       nv....zc .
ADC ($32,S),Y  (stk,S),Y     73  2   8-m         nv....zc .
ADC [$10]      [dir]         67  2   7-m+w       nv....zc .
ADC [$10],Y    [dir],Y       77  2   7-m+w       nv....zc .
```

details go here

### AND

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
AND #$54       imm           29  3-m 3-m         n.....z. .
AND $10        dir           25  2   4-m+w       n.....z. .
AND $10,X      dir,X         35  2   5-m+w       n.....z. .
AND $32,S      stk,S         23  2   5-m         n.....z. .
AND $9876      abs           2D  3   5-m         n.....z. .
AND $9876,X    abs,X         3D  3   6-m-x+x*p   n.....z. .
AND $9876,Y    abs,Y         39  3   6-m-x+x*p   n.....z. .
AND $FEDBCA    long          2F  4   6-m         n.....z. .
AND $FEDCBA,X  long,X        3F  4   6-m         n.....z. .
AND ($10)      (dir)         32  2   6-m+w       n.....z. .
AND ($10),Y    (dir),Y       31  2   7-m+w-x+x*p n.....z. .
AND ($10,X)    (dir,X)       21  2   7-m+w       n.....z. .
AND ($32,S),Y  (stk,S),Y     33  2   8-m         n.....z. .
AND [$10]      [dir]         27  2   7-m+w       n.....z. .
AND [$10],Y    [dir],Y       37  2   7-m+w       n.....z. .
```

details go here

### ASL

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
ASL            acc           0A  1   2           n.....zc .
ASL $10        dir           06  2   7-2*m+w     n.....zc .
ASL $10,X      dir,X         16  2   8-2*m+w     n.....zc .
ASL $9876      abs           0E  3   8-2*m       n.....zc .
ASL $9876,X    abs,X         1E  3   9-2*m       n.....zc .
```

details go here

### BCC

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
BCC LABEL      rel8          90  2   2+t+t*e*p   ........ .
```

details go here

### BCS

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
BCS LABEL      rel8          B0  2   2+t+t*e*p   ........ .
```

details go here

### BEQ

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
BEQ LABEL      rel8          F0  2   2+t+t*e*p   ........ .
```

details go here

### BIT

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
BIT #$54       imm           89  3-m 3-m         ......z. .
BIT $10        dir           24  2   4-m+w       nv....z. .
BIT $10,X      dir,X         34  2   5-m+w       nv....z. .
BIT $9876      abs           2C  3   5-m         nv....z. .
BIT $9876,X    abs,X         3C  3   6-m-x+x*p   nv....z. .
```

details go here

### BMI

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
BMI LABEL      rel8          30  2   2+t+t*e*p   ........ .
```

details go here

### BNE

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
BNE LABEL      rel8          D0  2   2+t+t*e*p   ........ .
```

details go here

### BPL

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
BPL LABEL      rel8          10  2   2+t+t*e*p   ........ .
```

details go here

### BRA

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
BRA LABEL      rel8          80  2   3+e*p       ........ .
```

details go here

### BRK

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
BRK            imp           00  1   8-e         ....di.. .
```

details go here

### BRL

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
BRL LABEL      rel16         82  3   4           ........ .
```

details go here

### BVC

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
BVC LABEL      rel8          50  2   2+t+t*e*p   ........ .
```

details go here

### BVS

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
BVS LABEL      rel8          70  2   2+t+t*e*p   ........ .
```

details go here

### CLC

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
CLC            imp           18  1   2           .......c .
```

details go here

### CLD

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
CLD            imp           D8  1   2           ....d... .
```

details go here

### CLI

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
CLI            imp           58  1   2           .....i.. .
```

details go here

### CLV

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
CLV            imp           B8  1   2           .v...... .
```

details go here

### CMP

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
CMP #$54       imm           C9  3-m 3-m         n.....zc .
CMP $10        dir           C5  2   4-m+w       n.....zc .
CMP $10,X      dir,X         D5  2   5-m+w       n.....zc .
CMP $32,S      stk,S         C3  2   5-m         n.....zc .
CMP $9876      abs           CD  3   5-m         n.....zc .
CMP $9876,X    abs,X         DD  3   6-m-x+x*p   n.....zc .
CMP $9876,Y    abs,Y         D9  3   6-m-x+x*p   n.....zc .
CMP $FEDBCA    long          CF  4   6-m         n.....zc .
CMP $FEDCBA,X  long,X        DF  4   6-m         n.....zc .
CMP ($10)      (dir)         D2  2   6-m+w       n.....zc .
CMP ($10),Y    (dir),Y       D1  2   7-m+w-x+x*p n.....zc .
CMP ($10,X)    (dir,X)       C1  2   7-m+w       n.....zc .
CMP ($32,S),Y  (stk,S),Y     D3  2   8-m         n.....zc .
CMP [$10]      [dir]         C7  2   7-m+w       n.....zc .
CMP [$10],Y    [dir],Y       D7  2   7-m+w       n.....zc .
```

details go here

### COP

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
COP #$12       imm           02  2   8-e         ....di.. .
```

details go here

### CPX

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
CPX #$54       imm           E0  3-x 3-x         n.....zc .
CPX $10        dir           E4  2   4-x+w       n.....zc .
CPX $9876      abs           EC  3   5-x         n.....zc .
```

details go here

### CPY

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
CPY #$54       imm           C0  3-x 3-x         n.....zc .
CPY $10        dir           C4  2   4-x+w       n.....zc .
CPY $9876      abs           CC  3   5-x         n.....zc .
```

details go here

### DEC

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
DEC            acc           3A  1   2           n.....z. .
DEC $10        dir           C6  2   7-2*m+w     n.....z. .
DEC $10,X      dir,X         D6  2   8-2*m+w     n.....z. .
DEC $9876      abs           CE  3   8-2*m       n.....z. .
DEC $9876,X    abs,X         DE  3   9-2*m       n.....z. .
```

details go here

### DEX

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
DEX            imp           CA  1   2           n.....z. .
```

details go here

### DEY

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
DEY            imp           88  1   2           n.....z. .
```

details go here

### EOR

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
EOR #$54       imm           49  3-m 3-m         n.....z. .
EOR $10        dir           45  2   4-m+w       n.....z. .
EOR $10,X      dir,X         55  2   5-m+w       n.....z. .
EOR $32,S      stk,S         43  2   5-m         n.....z. .
EOR $9876      abs           4D  3   5-m         n.....z. .
EOR $9876,X    abs,X         5D  3   6-m-x+x*p   n.....z. .
EOR $9876,Y    abs,Y         59  3   6-m-x+x*p   n.....z. .
EOR $FEDBCA    long          4F  4   6-m         n.....z. .
EOR $FEDCBA,X  long,X        5F  4   6-m         n.....z. .
EOR ($10)      (dir)         52  2   6-m+w       n.....z. .
EOR ($10),Y    (dir),Y       51  2   7-m+w-x+x*p n.....z. .
EOR ($10,X)    (dir,X)       41  2   7-m+w       n.....z. .
EOR ($32,S),Y  (stk,S),Y     53  2   8-m         n.....z. .
EOR [$10]      [dir]         47  2   7-m+w       n.....z. .
EOR [$10],Y    [dir],Y       57  2   7-m+w       n.....z. .
```

details go here

### INC

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
INC            acc           1A  1   2           n.....z. .
INC $10        dir           E6  2   7-2*m+w     n.....z. .
INC $10,X      dir,X         F6  2   8-2*m+w     n.....z. .
INC $9876      abs           EE  3   8-2*m       n.....z. .
INC $9876,X    abs,X         FE  3   9-2*m       n.....z. .
```

details go here

### INX

```text
SYNTAX         MODE          HEX 
<!-- For PDF formatting -->
<div class="page-break"></div>
