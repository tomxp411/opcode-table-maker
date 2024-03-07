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
PHA            imp           48  1   4-m         ........ .
```


[top](#instructions-by-opcode)

### PHB

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
PHB            imp           8B  1   3           ........ .
```


[top](#instructions-by-opcode)

### PHD

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
PHD            imp           0B  1   4           ........ .
```


[top](#instructions-by-opcode)

### PHK

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
PHK            imp           4B  1   3           ........ .
```


[top](#instructions-by-opcode)

### PHP

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
PHP            imp           08  1   3           ........ .
```


[top](#instructions-by-opcode)

### PHX

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
PHX            imp           DA  1   4-x         ........ .
```


[top](#instructions-by-opcode)

### PHY

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
PHY            imp           5A  1   4-x         ........ .
```


[top](#instructions-by-opcode)

### PLA

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
PLA            imp           68  1   5-m         n.....z. .
```


[top](#instructions-by-opcode)

### PLB

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
PLB            imp           AB  1   4           n.....z. .
```


[top](#instructions-by-opcode)

### PLD

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
PLD            imp           2B  1   5           n.....z. .
```


[top](#instructions-by-opcode)

### PLP

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
PLP            imp           28  1   4           nvmxdizc .
```


[top](#instructions-by-opcode)

### PLX

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
PLX            imp           FA  1   5-x         n.....z. .
```


[top](#instructions-by-opcode)

### PLY

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
PLY            imp           7A  1   5-x         n.....z. .
```


[top](#instructions-by-opcode)

### REP

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
REP #$12       imm           C2  2   3           nvmxdizc .
```


[top](#instructions-by-opcode)

### ROL

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
ROL            acc           2A  1   2           n.....zc .
ROL $10        dir           26  2   7-2*m+w     n.....zc .
ROL $10,X      dir,X         36  2   8-2*m+w     n.....zc .
ROL $9876      abs           2E  3   8-2*m       n.....zc .
ROL $9876,X    abs,X         3E  3   9-2*m       n.....zc .
```


[top](#instructions-by-opcode)

### ROR

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
ROR            acc           6A  1   2           n.....zc .
ROR $10        dir           66  2   7-2*m+w     n.....zc .
ROR $10,X      dir,X         76  2   8-2*m+w     n.....zc .
ROR $9876      abs           6E  3   8-2*m       n.....zc .
ROR $9876,X    abs,X         7E  3   9-2*m       n.....zc .
```


[top](#instructions-by-opcode)

### RTI

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
RTI            imp           40  1   7-e         nvmxdizc .
```


[top](#instructions-by-opcode)

### RTL

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
RTL            imp           6B  1   6           ........ .
```


[top](#instructions-by-opcode)

### RTS

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
RTS            imp           60  1   6           ........ .
```


[top](#instructions-by-opcode)

### SBC

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
SBC #$54       imm           E9  3-m 3-m         nv....zc .
SBC $10        dir           E5  2   4-m+w       nv....zc .
SBC $10,X      dir,X         F5  2   5-m+w       nv....zc .
SBC $32,S      stk,S         E3  2   5-m         nv....zc .
SBC $9876      abs           ED  3   5-m         nv....zc .
SBC $9876,X    abs,X         FD  3   6-m-x+x*p   nv....zc .
SBC $9876,Y    abs,Y         F9  3   6-m-x+x*p   nv....zc .
SBC $FEDBCA    long          EF  4   6-m         nv....zc .
SBC $FEDCBA,X  long,X        FF  4   6-m         nv....zc .
SBC ($10)      (dir)         F2  2   6-m+w       nv....zc .
SBC ($10),Y    (dir),Y       F1  2   7-m+w-x+x*p nv....zc .
SBC ($10,X)    (dir,X)       E1  2   7-m+w       nv....zc .
SBC ($32,S),Y  (stk,S),Y     F3  2   8-m         nv....zc .
SBC [$10]      [dir]         E7  2   7-m+w       nv....zc .
SBC [$10],Y    [dir],Y       F7  2   7-m+w       nv....zc .
```


[top](#instructions-by-opcode)

### SEC

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
SEC            imp           38  1   2           .......c .
```


[top](#instructions-by-opcode)

### SED

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
SED            imp           F8  1   2           ....d... .
```


[top](#instructions-by-opcode)

### SEI

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
SEI            imp           78  1   2           .....i.. .
```


[top](#instructions-by-opcode)

### SEP

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
SEP #$12       imm           E2  2   3           nvmxdizc .
```


[top](#instructions-by-opcode)

### STA

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
STA $10        dir           85  2   4-m+w       ........ .
STA $10,X      dir,X         95  2   5-m+w       ........ .
STA $32,S      stk,S         83  2   5-m         ........ .
STA $9876      abs           8D  3   5-m         ........ .
STA $9876,X    abs,X         9D  3   6-m         ........ .
STA $9876,Y    abs,Y         99  3   6-m         ........ .
STA $FEDBCA    long          8F  4   6-m         ........ .
STA $FEDCBA,X  long,X        9F  4   6-m         ........ .
STA ($10)      (dir)         92  2   6-m+w       ........ .
STA ($10),Y    (dir),Y       91  2   7-m+w       ........ .
STA ($10,X)    (dir,X)       81  2   7-m+w       ........ .
STA ($32,S),Y  (stk,S),Y     93  2   8-m         ........ .
STA [$10]      [dir]         87  2   7-m+w       ........ .
STA [$10],Y    [dir],Y       97  2   7-m+w       ........ .
```


[top](#instructions-by-opcode)

### STP

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
STP            imp           DB  1   3           ........ .
```


[top](#instructions-by-opcode)

### STX

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
STX $10        dir           86  2   4-x+w       ........ .
STX $10,Y      dir,Y         96  2   5-x+w       ........ .
STX $9876      abs           8E  3   5-x         ........ .
```


[top](#instructions-by-opcode)

### STY

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
STY $10        dir           84  2   4-x+w       ........ .
STY $10,X      dir,X         94  2   5-x+w       ........ .
STY $9876      abs           8C  3   5-x         ........ .
```


[top](#instructions-by-opcode)

### STZ

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
STZ $10        dir           64  2   4-m+w       ........ .
STZ $10,X      dir,X         74  2   5-m+w       ........ .
STZ $9876      abs           9C  3   5-m         ........ .
STZ $9876,X    abs,X         9E  3   6-m         ........ .
```


[top](#instructions-by-opcode)

### TAX

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
TAX            imp           AA  1   2           n.....z. .
```


[top](#instructions-by-opcode)

### TAY

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
TAY            imp           A8  1   2           n.....z. .
```


[top](#instructions-by-opcode)

### TCD

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
TCD            imp           5B  1   2           n.....z. .
```


[top](#instructions-by-opcode)

### TCS

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
TCS            imp           1B  1   2           ........ .
```


[top](#instructions-by-opcode)

### TDC

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
TDC            imp           7B  1   2           n.....z. .
```


[top](#instructions-by-opcode)

### TRB

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
TRB $10        dir           14  2   7-2*m+w     ......z. .
TRB $9876      abs           1C  3   8-2*m       ......z. .
```


[top](#instructions-by-opcode)

### TSB

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
TSB $10        dir           04  2   7-2*m+w     ......z. .
TSB $9876      abs           0C  3   8-2*m       ......z. .
```


[top](#instructions-by-opcode)

### TSC

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
TSC            imp           3B  1   2           n.....z. .
```


[top](#instructions-by-opcode)

### TSX

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
TSX            imp           BA  1   2           n.....z. .
```


[top](#instructions-by-opcode)

### TXA

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
TXA            imp           8A  1   2           n.....z. .
```


[top](#instructions-by-opcode)

### TXS

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
TXS            imp           9A  1   2           ........ .
```


[top](#instructions-by-opcode)

### TXY

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
TXY            imp           9B  1   2           n.....z. .
```


[top](#instructions-by-opcode)

### TYA

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
TYA            imp           98  1   2           n.....z. .
```


[top](#instructions-by-opcode)

### TYX

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
TYX            imp           BB  1   2           n.....z. .
```


[top](#instructions-by-opcode)

### WAI

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
WAI            imp           CB  1   3           ........ .
```


[top](#instructions-by-opcode)

### WDM

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
WDM            imm           42  2   2           ........ .
```


[top](#instructions-by-opcode)

### XBA

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
XBA            imp           EB  1   3           n.....z. .
```


[top](#instructions-by-opcode)

### XCE

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
XCE            imp           FB  1   2           .......c e
```


[top](#instructions-by-opcode)

