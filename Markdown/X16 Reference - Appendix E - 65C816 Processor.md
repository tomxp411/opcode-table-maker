
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
|        0x |[BRK](#brk)|[ORA](#ora)|[COP](#cop)|[ORA](#ora)|[TSB](#tsb)|[ORA](#ora)|[ASL](#asl)|[ORA](#ora)|[PHP](#php)|[ORA](#ora)|[ASL](#asl)|[PHD](#phd)|[TSB](#tsb)|[ORA](#ora)|[ASL](#asl)|[ORA](#ora)|
|        1x |[BPL](#bpl)|[ORA](#ora)|[ORA](#ora)|[ORA](#ora)|[TRB](#trb)|[ORA](#ora)|[ASL](#asl)|[ORA](#ora)|[CLC](#clc)|[ORA](#ora)|[INC](#inc)|[TCS](#tcs)|[TRB](#trb)|[ORA](#ora)|[ASL](#asl)|[ORA](#ora)|
|        2x |[JSR](#jsr)|[AND](#and)|[JSL](#jsl)|[AND](#and)|[BIT](#bit)|[AND](#and)|[ROL](#rol)|[AND](#and)|[PLP](#plp)|[AND](#and)|[ROL](#rol)|[PLD](#pld)|[BIT](#bit)|[AND](#and)|[ROL](#rol)|[AND](#and)|
|        3x |[BMI](#bmi)|[AND](#and)|[AND](#and)|[AND](#and)|[BIT](#bit)|[AND](#and)|[ROL](#rol)|[AND](#and)|[SEC](#sec)|[AND](#and)|[DEC](#dec)|[TSC](#tsc)|[BIT](#bit)|[AND](#and)|[ROL](#rol)|[AND](#and)|
|        4x |[RTI](#rti)|[EOR](#eor)|[WDM](#wdm)|[EOR](#eor)|[MVP](#mvp)|[EOR](#eor)|[LSR](#lsr)|[EOR](#eor)|[PHA](#pha)|[EOR](#eor)|[LSR](#lsr)|[PHK](#phk)|[JMP](#jmp)|[EOR](#eor)|[LSR](#lsr)|[EOR](#eor)|
|        5x |[BVC](#bvc)|[EOR](#eor)|[EOR](#eor)|[EOR](#eor)|[MVN](#mvn)|[EOR](#eor)|[LSR](#lsr)|[EOR](#eor)|[CLI](#cli)|[EOR](#eor)|[PHY](#phy)|[TCD](#tcd)|[JMP](#jmp)|[EOR](#eor)|[LSR](#lsr)|[EOR](#eor)|
|        6x |[RTS](#rts)|[ADC](#adc)|[PER](#per)|[ADC](#adc)|[STZ](#stz)|[ADC](#adc)|[ROR](#ror)|[ADC](#adc)|[PLA](#pla)|[ADC](#adc)|[ROR](#ror)|[RTL](#rtl)|[JMP](#jmp)|[ADC](#adc)|[ROR](#ror)|[ADC](#adc)|
|        7x |[BVS](#bvs)|[ADC](#adc)|[ADC](#adc)|[ADC](#adc)|[STZ](#stz)|[ADC](#adc)|[ROR](#ror)|[ADC](#adc)|[SEI](#sei)|[ADC](#adc)|[PLY](#ply)|[TDC](#tdc)|[JMP](#jmp)|[ADC](#adc)|[ROR](#ror)|[ADC](#adc)|
|        8x |[BRA](#bra)|[STA](#sta)|[BRL](#brl)|[STA](#sta)|[STY](#sty)|[STA](#sta)|[STX](#stx)|[STA](#sta)|[DEY](#dey)|[BIT](#bit)|[TXA](#txa)|[PHB](#phb)|[STY](#sty)|[STA](#sta)|[STX](#stx)|[STA](#sta)|
|        9x |[BCC](#bcc)|[STA](#sta)|[STA](#sta)|[STA](#sta)|[STY](#sty)|[STA](#sta)|[STX](#stx)|[STA](#sta)|[TYA](#tya)|[STA](#sta)|[TXS](#txs)|[TXY](#txy)|[STZ](#stz)|[STA](#sta)|[STZ](#stz)|[STA](#sta)|
|        Ax |[LDY](#ldy)|[LDA](#lda)|[LDX](#ldx)|[LDA](#lda)|[LDY](#ldy)|[LDA](#lda)|[LDX](#ldx)|[LDA](#lda)|[TAY](#tay)|[LDA](#lda)|[TAX](#tax)|[PLB](#plb)|[LDY](#ldy)|[LDA](#lda)|[LDX](#ldx)|[LDA](#lda)|
|        Bx |[BCS](#bcs)|[LDA](#lda)|[LDA](#lda)|[LDA](#lda)|[LDY](#ldy)|[LDA](#lda)|[LDX](#ldx)|[LDA](#lda)|[CLV](#clv)|[LDA](#lda)|[TSX](#tsx)|[TYX](#tyx)|[LDY](#ldy)|[LDA](#lda)|[LDX](#ldx)|[LDA](#lda)|
|        Cx |[CPY](#cpy)|[CMP](#cmp)|[REP](#rep)|[CMP](#cmp)|[CPY](#cpy)|[CMP](#cmp)|[DEC](#dec)|[CMP](#cmp)|[INY](#iny)|[CMP](#cmp)|[DEX](#dex)|[WAI](#wai)|[CPY](#cpy)|[CMP](#cmp)|[DEC](#dec)|[CMP](#cmp)|
|        Dx |[BNE](#bne)|[CMP](#cmp)|[CMP](#cmp)|[CMP](#cmp)|[PEI](#pei)|[CMP](#cmp)|[DEC](#dec)|[CMP](#cmp)|[CLD](#cld)|[CMP](#cmp)|[PHX](#phx)|[STP](#stp)|[JMP](#jmp)|[CMP](#cmp)|[DEC](#dec)|[CMP](#cmp)|
|        Ex |[CPX](#cpx)|[SBC](#sbc)|[SEP](#sep)|[SBC](#sbc)|[CPX](#cpx)|[SBC](#sbc)|[INC](#inc)|[SBC](#sbc)|[INX](#inx)|[SBC](#sbc)|[NOP](#nop)|[XBA](#xba)|[CPX](#cpx)|[SBC](#sbc)|[INC](#inc)|[SBC](#sbc)|
|        Fx |[BEQ](#beq)|[SBC](#sbc)|[SBC](#sbc)|[SBC](#sbc)|[PEA](#pea)|[SBC](#sbc)|[INC](#inc)|[SBC](#sbc)|[SED](#sed)|[SBC](#sbc)|[PLX](#plx)|[XCE](#xce)|[JSR](#jsr)|[SBC](#sbc)|[INC](#inc)|[SBC](#sbc)|

## Instructions By Name

|             |             |             |             |             |             |             |             |             |             |
|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|
| [ADC](#adc) | [AND](#and) | [ASL](#asl) | [BCC](#bcc) | [BCS](#bcs) | [BEQ](#beq) | [BIT](#bit) | [BMI](#bmi) | [BNE](#bne) | [BPL](#bpl) |
| [BRA](#bra) | [BRK](#brk) | [BRL](#brl) | [BVC](#bvc) | [BVS](#bvs) | [CLC](#clc) | [CLD](#cld) | [CLI](#cli) | [CLV](#clv) | [CMP](#cmp) |
| [COP](#cop) | [CPX](#cpx) | [CPY](#cpy) | [DEC](#dec) | [DEX](#dex) | [DEY](#dey) | [EOR](#eor) | [INC](#inc) | [INX](#inx) | [INY](#iny) |
| [JMP](#jmp) | [JSL](#jsl) | [JSR](#jsr) | [LDA](#lda) | [LDX](#ldx) | [LDY](#ldy) | [LSR](#lsr) | [MVN](#mvn) | [MVP](#mvp) | [NOP](#nop) |
| [ORA](#ora) | [PEA](#pea) | [PEI](#pei) | [PER](#per) | [PHA](#pha) | [PHB](#phb) | [PHD](#phd) | [PHK](#phk) | [PHP](#php) | [PHX](#phx) |
| [PHY](#phy) | [PLA](#pla) | [PLB](#plb) | [PLD](#pld) | [PLP](#plp) | [PLX](#plx) | [PLY](#ply) | [REP](#rep) | [ROL](#rol) | [ROR](#ror) |
| [RTI](#rti) | [RTL](#rtl) | [RTS](#rts) | [SBC](#sbc) | [SEC](#sec) | [SED](#sed) | [SEI](#sei) | [SEP](#sep) | [STA](#sta) | [STP](#stp) |
| [STX](#stx) | [STY](#sty) | [STZ](#stz) | [TAX](#tax) | [TAY](#tay) | [TCD](#tcd) | [TCS](#tcs) | [TDC](#tdc) | [TRB](#trb) | [TSB](#tsb) |
| [TSC](#tsc) | [TSX](#tsx) | [TXA](#txa) | [TXS](#txs) | [TXY](#txy) | [TYA](#tya) | [TYX](#tyx) | [WAI](#wai) | [WDM](#wdm) | [XBA](#xba) |
| [XCE](#xce) |

## Instructions By Category

|Category       |Instructions   |
|---------------|---------------|
| Arithmetic    | [ADC](#adc) , [SBC](#sbc) |
| Boolean       | [AND](#and) , [EOR](#eor) , [ORA](#ora) |
| Shift         | [ASL](#asl) , [LSR](#lsr) , [ROL](#rol) , [ROR](#ror) |
| Branch        | [BCC](#bcc) , [BCS](#bcs) , [BEQ](#beq) , [BMI](#bmi) , [BNE](#bne) , [BPL](#bpl) , [BRA](#bra) , [BRK](#brk) , [BRL](#brl) , [BVC](#bvc) , [BVS](#bvs) |
| Test          | [BIT](#bit) , [TRB](#trb) , [TSB](#tsb) |
| Flags         | [CLC](#clc) , [CLD](#cld) , [CLI](#cli) , [CLV](#clv) , [REP](#rep) , [SEC](#sec) , [SED](#sed) , [SEI](#sei) , [SEP](#sep) |
| Compare       | [CMP](#cmp) , [CPX](#cpx) , [CPY](#cpy) |
| Interrupt     | [COP](#cop) , [WAI](#wai) |
| Inc/Dec       | [DEC](#dec) , [DEX](#dex) , [DEY](#dey) , [INC](#inc) , [INX](#inx) , [INY](#iny) |
| Flow          | [JMP](#jmp) , [JSL](#jsl) , [JSR](#jsr) , [NOP](#nop) , [RTI](#rti) , [RTL](#rtl) , [RTS](#rts) , [WDM](#wdm) |
| Load          | [LDA](#lda) , [LDX](#ldx) , [LDY](#ldy) |
| Block Move    | [MVN](#mvn) , [MVP](#mvp) |
| Stack         | [PEA](#pea) , [PEI](#pei) , [PER](#per) , [PHA](#pha) , [PHB](#phb) , [PHD](#phd) , [PHK](#phk) , [PHP](#php) , [PHX](#phx) , [PHY](#phy) , [PLA](#pla) , [PLB](#plb) , [PLD](#pld) , [PLP](#plp) , [PLX](#plx) , [PLY](#ply) |
| Store         | [STA](#sta) , [STP](#stp) , [STX](#stx) , [STY](#sty) , [STZ](#stz) |
| Register Swap | [TAX](#tax) , [TAY](#tay) , [TCD](#tcd) , [TCS](#tcs) , [TDC](#tdc) , [TSC](#tsc) , [TSX](#tsx) , [TXA](#txa) , [TXS](#txs) , [TXY](#txy) , [TYA](#tya) , [TYX](#tyx) , [XBA](#xba) , [XCE](#xce) |

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

Add with Carry

ADC adds the accumulator (.A), the supplied operand, and the Carry bit (0 or 1).
The result is stored in .A.

Since Carry is always added in, you should always remember to use CLC (Clear
Carry) before performing an addition operation. When adding larger numbers (16,
24, 32, or more bits), you can use the Carry flag to chain additions.

Here is an example of a 16-bit add, when in 8 bit mode:

```asm
CLC
LDA Addend1
ADC Addend2
STA Result1
BCC done
LDA Addend1+1  ; Reads the high byte of the addend
ADC Addend2+1  ; (the +1 refers to the *address* of Addend, not the value)
STA Result1+1  ;
done:
; the final result is at Result1
```

Flags:

* .n is set when the high bit of .A is set. This indicates a negative number
when using Two's Complement signed values.
* .v (overflow) is set when the sum exceeds the maximum *signed* value for .A.
(More on that below). * .n is set when the high bit is 1.
* .z is set when the result is zero. This is useful for loop counters and can be
tested with BEQ and BNE. (BEQ and BNE test the Zero bit, which is also the
"equal" bit when performing subtraction or Compare operations.)
* .c is set when the unsigned result exceeds the register's capacity (255 or
65535).


#### Overflow vs Carry

The CPU detects addition that goes past the 7 or 15 bit boundary of a signed
number, as well as the 8 bit boundary of an unsigned number.

In 8-bit mode, when you add two positive numbers that result in a sum
higher than 127 or add two negative numbers that result in a sum below -128, you
will get a signed overflow, and the v flag will be set.

When the sum of the two numbers exceeeds 255 or 65535, then the Carry flag will
be set. This bit can be added to the next higher byte with ADC #0.

```asm
CLC
LDA #$7F
ADC #$10
BRK
```


[top](#instructions-by-opcode)

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


[top](#instructions-by-opcode)

### ASL

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
ASL            acc           0A  1   2           n.....zc .
ASL $10        dir           06  2   7-2*m+w     n.....zc .
ASL $10,X      dir,X         16  2   8-2*m+w     n.....zc .
ASL $9876      abs           0E  3   8-2*m       n.....zc .
ASL $9876,X    abs,X         1E  3   9-2*m       n.....zc .
```


[top](#instructions-by-opcode)

### BCC

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
BCC LABEL      rel8          90  2   2+t+t*e*p   ........ .
```


[top](#instructions-by-opcode)

### BCS

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
BCS LABEL      rel8          B0  2   2+t+t*e*p   ........ .
```


[top](#instructions-by-opcode)

### BEQ

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
BEQ LABEL      rel8          F0  2   2+t+t*e*p   ........ .
```


[top](#instructions-by-opcode)

### BIT

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
BIT #$54       imm           89  3-m 3-m         ......z. .
BIT $10        dir           24  2   4-m+w       nv....z. .
BIT $10,X      dir,X         34  2   5-m+w       nv....z. .
BIT $9876      abs           2C  3   5-m         nv....z. .
BIT $9876,X    abs,X         3C  3   6-m-x+x*p   nv....z. .
```


[top](#instructions-by-opcode)

### BMI

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
BMI LABEL      rel8          30  2   2+t+t*e*p   ........ .
```


[top](#instructions-by-opcode)

### BNE

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
BNE LABEL      rel8          D0  2   2+t+t*e*p   ........ .
```


[top](#instructions-by-opcode)

### BPL

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
BPL LABEL      rel8          10  2   2+t+t*e*p   ........ .
```


[top](#instructions-by-opcode)

### BRA

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
BRA LABEL      rel8          80  2   3+e*p       ........ .
```


[top](#instructions-by-opcode)

### BRK

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
BRK            imp           00  1   8-e         ....di.. .
```


[top](#instructions-by-opcode)

### BRL

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
BRL LABEL      rel16         82  3   4           ........ .
```


[top](#instructions-by-opcode)

### BVC

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
BVC LABEL      rel8          50  2   2+t+t*e*p   ........ .
```


[top](#instructions-by-opcode)

### BVS

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
BVS LABEL      rel8          70  2   2+t+t*e*p   ........ .
```


[top](#instructions-by-opcode)

### CLC

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
CLC            imp           18  1   2           .......c .
```


[top](#instructions-by-opcode)

### CLD

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
CLD            imp           D8  1   2           ....d... .
```


[top](#instructions-by-opcode)

### CLI

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
CLI            imp           58  1   2           .....i.. .
```


[top](#instructions-by-opcode)

### CLV

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
CLV            imp           B8  1   2           .v...... .
```


[top](#instructions-by-opcode)

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


[top](#instructions-by-opcode)

### COP

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
COP #$12       imm           02  2   8-e         ....di.. .
```


[top](#instructions-by-opcode)

### CPX

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
CPX #$54       imm           E0  3-x 3-x         n.....zc .
CPX $10        dir           E4  2   4-x+w       n.....zc .
CPX $9876      abs           EC  3   5-x         n.....zc .
```


[top](#instructions-by-opcode)

### CPY

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
CPY #$54       imm           C0  3-x 3-x         n.....zc .
CPY $10        dir           C4  2   4-x+w       n.....zc .
CPY $9876      abs           CC  3   5-x         n.....zc .
```


[top](#instructions-by-opcode)

### DEC

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
DEC            acc           3A  1   2           n.....z. .
DEC $10        dir           C6  2   7-2*m+w     n.....z. .
DEC $10,X      dir,X         D6  2   8-2*m+w     n.....z. .
DEC $9876      abs           CE  3   8-2*m       n.....z. .
DEC $9876,X    abs,X         DE  3   9-2*m       n.....z. .
```


[top](#instructions-by-opcode)

### DEX

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
DEX            imp           CA  1   2           n.....z. .
```


[top](#instructions-by-opcode)

### DEY

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
DEY            imp           88  1   2           n.....z. .
```


[top](#instructions-by-opcode)

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


[top](#instructions-by-opcode)

### INC

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
INC            acc           1A  1   2           n.....z. .
INC $10        dir           E6  2   7-2*m+w     n.....z. .
INC $10,X      dir,X         F6  2   8-2*m+w     n.....z. .
INC $9876      abs           EE  3   8-2*m       n.....z. .
INC $9876,X    abs,X         FE  3   9-2*m       n.....z. .
```


[top](#instructions-by-opcode)

### INX

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
INX            imp           E8  1   2           n.....z. .
```


[top](#instructions-by-opcode)

### INY

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
INY            imp           C8  1   2           n.....z. .
```


[top](#instructions-by-opcode)

### JMP

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
JMP $1234      abs           4C  3   3           ........ .
JMP $FEDCBA    long          5C  4   4           ........ .
JMP ($1234)    (abs)         6C  3   5           ........ .
JMP ($1234,X)  (abs,X)       7C  3   6           ........ .
JMP [$1234]    [abs]         DC  3   6           ........ .
```


[top](#instructions-by-opcode)

### JSL

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
JSL $123456    long          22  4   8           ........ .
```


[top](#instructions-by-opcode)

### JSR

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
JSR $1234      abs           20  3   6           ........ .
JSR ($1234,X)  (abs,X)       FC  3   8           ........ .
```


[top](#instructions-by-opcode)

### LDA

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
LDA #$54       imm           A9  3-m 3-m         n.....z. .
LDA $10        dir           A5  2   4-m+w       n.....z. .
LDA $10,X      dir,X         B5  2   5-m+w       n.....z. .
LDA $32,S      stk,S         A3  2   5-m         n.....z. .
LDA $9876      abs           AD  3   5-m         n.....z. .
LDA $9876,X    abs,X         BD  3   6-m-x+x*p   n.....z. .
LDA $9876,Y    abs,Y         B9  3   6-m-x+x*p   n.....z. .
LDA $FEDBCA    long          AF  4   6-m         n.....z. .
LDA $FEDCBA,X  long,X        BF  4   6-m         n.....z. .
LDA ($10)      (dir)         B2  2   6-m+w       n.....z. .
LDA ($10),Y    (dir),Y       B1  2   7-m+w-x+x*p n.....z. .
LDA ($10,X)    (dir,X)       A1  2   7-m+w       n.....z. .
LDA ($32,S),Y  (stk,S),Y     B3  2   8-m         n.....z. .
LDA [$10]      [dir]         A7  2   7-m+w       n.....z. .
LDA [$10],Y    [dir],Y       B7  2   7-m+w       n.....z. .
```


[top](#instructions-by-opcode)

### LDX

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
LDX #$54       imm           A2  3-x 3-x         n.....z. .
LDX $10        dir           A6  2   4-x+w       n.....z. .
LDX $10,Y      dir,Y         B6  2   5-x+w       n.....z. .
LDX $9876      abs           AE  3   5-x         n.....z. .
LDX $9876,Y    abs,Y         BE  3   6-2*x+x*p   n.....z. .
```


[top](#instructions-by-opcode)

### LDY

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
LDY #$54       imm           A0  3-x 3-x         n.....z. .
LDY $10        dir           A4  2   4-x+w       n.....z. .
LDY $10,X      dir,X         B4  2   5-x+w       n.....z. .
LDY $9876      abs           AC  3   5-x         n.....z. .
LDY $9876,X    abs,X         BC  3   6-2*x+x*p   n.....z. .
```


[top](#instructions-by-opcode)

### LSR

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
LSR            acc           4A  1   2           n.....zc .
LSR $10        dir           46  2   7-2*m+w     n.....zc .
LSR $10,X      dir,X         56  2   8-2*m+w     n.....zc .
LSR $9876      abs           4E  3   8-2*m       n.....zc .
LSR $9876,X    abs,X         5E  3   9-2*m       n.....zc .
```


[top](#instructions-by-opcode)

### MVN

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
MVN #$12,#$34  src,dest      54  3   7           ........ .
```


[top](#instructions-by-opcode)

### MVP

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
MVP #$12,#$34  src,dest      44  3   7           ........ .
```


[top](#instructions-by-opcode)

### NOP

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
NOP            imp           EA  1   2           ........ .
```


[top](#instructions-by-opcode)

### ORA

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
ORA #$54       imm           09  3-m 3-m         n.....z. .
ORA $10        dir           05  2   4-m+w       n.....z. .
ORA $10,X      dir,X         15  2   5-m+w       n.....z. .
ORA $32,S      stk,S         03  2   5-m         n.....z. .
ORA $9876      abs           0D  3   5-m         n.....z. .
ORA $9876,X    abs,X         1D  3   6-m-x+x*p   n.....z. .
ORA $9876,Y    abs,Y         19  3   6-m-x+x*p   n.....z. .
ORA $FEDBCA    long          0F  4   6-m         n.....z. .
ORA $FEDCBA,X  long,X        1F  4   6-m         n.....z. .
ORA ($10)      (dir)         12  2   6-m+w       n.....z. .
ORA ($10),Y    (dir),Y       11  2   7-m+w-x+x*p n.....z. .
ORA ($10,X)    (dir,X)       01  2   7-m+w       n.....z. .
ORA ($32,S),Y  (stk,S),Y     13  2   8-m         n.....z. .
ORA [$10]      [dir]         07  2   7-m+w       n.....z. .
ORA [$10],Y    [dir],Y       17  2   7-m+w       n.....z. .
```


[top](#instructions-by-opcode)

### PEA

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
PEA #$1234     imm           F4  3   5           ........ .
```


[top](#instructions-by-opcode)

### PEI

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
PEI $12        dir           D4  2   6+w         ........ .
```


[top](#instructions-by-opcode)

### PER

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
PER LABEL      imm           62  3   6           ........ .
```


[top](#instructions-by-opcode)

### PHA

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
PHA            imp           48  
<!-- For PDF formatting -->
<div class="page-break"></div>
