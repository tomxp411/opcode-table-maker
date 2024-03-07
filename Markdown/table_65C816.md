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
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
INX            imp           E8  1   2           n.....z. .
```

details go here

### INY

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
INY            imp           C8  1   2           n.....z. .
```

details go here

### JMP

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
JMP $1234      abs           4C  3   3           ........ .
JMP $FEDCBA    long          5C  4   4           ........ .
JMP ($1234)    (abs)         6C  3   5           ........ .
JMP ($1234,X)  (abs,X)       7C  3   6           ........ .
JMP [$1234]    [abs]         DC  3   6           ........ .
```

details go here

### JSL

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
JSL $123456    long          22  4   8           ........ .
```

details go here

### JSR

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
JSR $1234      abs           20  3   6           ........ .
JSR ($1234,X)  (abs,X)       FC  3   8           ........ .
```

details go here

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

details go here

### LDX

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
LDX #$54       imm           A2  3-x 3-x         n.....z. .
LDX $10        dir           A6  2   4-x+w       n.....z. .
LDX $10,Y      dir,Y         B6  2   5-x+w       n.....z. .
LDX $9876      abs           AE  3   5-x         n.....z. .
LDX $9876,Y    abs,Y         BE  3   6-2*x+x*p   n.....z. .
```

details go here

### LDY

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
LDY #$54       imm           A0  3-x 3-x         n.....z. .
LDY $10        dir           A4  2   4-x+w       n.....z. .
LDY $10,X      dir,X         B4  2   5-x+w       n.....z. .
LDY $9876      abs           AC  3   5-x         n.....z. .
LDY $9876,X    abs,X         BC  3   6-2*x+x*p   n.....z. .
```

details go here

### LSR

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
LSR            acc           4A  1   2           n.....zc .
LSR $10        dir           46  2   7-2*m+w     n.....zc .
LSR $10,X      dir,X         56  2   8-2*m+w     n.....zc .
LSR $9876      abs           4E  3   8-2*m       n.....zc .
LSR $9876,X    abs,X         5E  3   9-2*m       n.....zc .
```

details go here

### MVN

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
MVN #$12,#$34  src,dest      54  3   7           ........ .
```

details go here

### MVP

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
MVP #$12,#$34  src,dest      44  3   7           ........ .
```

details go here

### NOP

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
NOP            imp           EA  1   2           ........ .
```

details go here

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

details go here

### PEA

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
PEA #$1234     imm           F4  3   5           ........ .
```

details go here

### PEI

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
PEI $12        dir           D4  2   6+w         ........ .
```

details go here

### PER

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
PER LABEL      imm           62  3   6           ........ .
```

details go here

### PHA

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
PHA            imp           48  1   4-m         ........ .
```

details go here

### PHB

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
PHB            imp           8B  1   3           ........ .
```

details go here

### PHD

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
PHD            imp           0B  1   4           ........ .
```

details go here

### PHK

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
PHK            imp           4B  1   3           ........ .
```

details go here

### PHP

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
PHP            imp           08  1   3           ........ .
```

details go here

### PHX

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
PHX            imp           DA  1   4-x         ........ .
```

details go here

### PHY

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
PHY            imp           5A  1   4-x         ........ .
```

details go here

### PLA

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
PLA            imp           68  1   5-m         n.....z. .
```

details go here

### PLB

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
PLB            imp           AB  1   4           n.....z. .
```

details go here

### PLD

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
PLD            imp           2B  1   5           n.....z. .
```

details go here

### PLP

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
PLP            imp           28  1   4           nvmxdizc .
```

details go here

### PLX

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
PLX            imp           FA  1   5-x         n.....z. .
```

details go here

### PLY

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
PLY            imp           7A  1   5-x         n.....z. .
```

details go here

### REP

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
REP #$12       imm           C2  2   3           nvmxdizc .
```

details go here

### ROL

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
ROL            acc           2A  1   2           n.....zc .
ROL $10        dir           26  2   7-2*m+w     n.....zc .
ROL $10,X      dir,X         36  2   8-2*m+w     n.....zc .
ROL $9876      abs           2E  3   8-2*m       n.....zc .
ROL $9876,X    abs,X         3E  3   9-2*m       n.....zc .
```

details go here

### ROR

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
ROR            acc           6A  1   2           n.....zc .
ROR $10        dir           66  2   7-2*m+w     n.....zc .
ROR $10,X      dir,X         76  2   8-2*m+w     n.....zc .
ROR $9876      abs           6E  3   8-2*m       n.....zc .
ROR $9876,X    abs,X         7E  3   9-2*m       n.....zc .
```

details go here

### RTI

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
RTI            imp           40  1   7-e         nvmxdizc .
```

details go here

### RTL

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
RTL            imp           6B  1   6           ........ .
```

details go here

### RTS

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
RTS            imp           60  1   6           ........ .
```

details go here

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

details go here

### SEC

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
SEC            imp           38  1   2           .......c .
```

details go here

### SED

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
SED            imp           F8  1   2           ....d... .
```

details go here

### SEI

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
SEI            imp           78  1   2           .....i.. .
```

details go here

### SEP

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
SEP #$12       imm           E2  2   3           nvmxdizc .
```

details go here

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

details go here

### STP

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
STP            imp           DB  1   3           ........ .
```

details go here

### STX

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
STX $10        dir           86  2   4-x+w       ........ .
STX $10,Y      dir,Y         96  2   5-x+w       ........ .
STX $9876      abs           8E  3   5-x         ........ .
```

details go here

### STY

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
STY $10        dir           84  2   4-x+w       ........ .
STY $10,X      dir,X         94  2   5-x+w       ........ .
STY $9876      abs           8C  3   5-x         ........ .
```

details go here

### STZ

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
STZ $10        dir           64  2   4-m+w       ........ .
STZ $10,X      dir,X         74  2   5-m+w       ........ .
STZ $9876      abs           9C  3   5-m         ........ .
STZ $9876,X    abs,X         9E  3   6-m         ........ .
```

details go here

### TAX

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
TAX            imp           AA  1   2           n.....z. .
```

details go here

### TAY

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
TAY            imp           A8  1   2           n.....z. .
```

details go here

### TCD

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
TCD            imp           5B  1   2           n.....z. .
```

details go here

### TCS

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
TCS            imp           1B  1   2           ........ .
```

details go here

### TDC

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
TDC            imp           7B  1   2           n.....z. .
```

details go here

### TRB

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
TRB $10        dir           14  2   7-2*m+w     ......z. .
TRB $9876      abs           1C  3   8-2*m       ......z. .
```

details go here

### TSB

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
TSB $10        dir           04  2   7-2*m+w     ......z. .
TSB $9876      abs           0C  3   8-2*m       ......z. .
```

details go here

### TSC

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
TSC            imp           3B  1   2           n.....z. .
```

details go here

### TSX

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
TSX            imp           BA  1   2           n.....z. .
```

details go here

### TXA

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
TXA            imp           8A  1   2           n.....z. .
```

details go here

### TXS

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
TXS            imp           9A  1   2           ........ .
```

details go here

### TXY

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
TXY            imp           9B  1   2           n.....z. .
```

details go here

### TYA

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
TYA            imp           98  1   2           n.....z. .
```

details go here

### TYX

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
TYX            imp           BB  1   2           n.....z. .
```

details go here

### WAI

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
WAI            imp           CB  1   3           ........ .
```

details go here

### WDM

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
WDM            imm           42  2   2           ........ .
```

details go here

### XBA

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
XBA            imp           EB  1   3           n.....z. .
```

details go here

### XCE

```text
SYNTAX         MODE          HEX LEN CYCLES      FLAGS   
XCE            imp           FB  1   2           .......c e
```

details go here

