## Opcodes By Number
|            | x0          | x1          | x2          | x3          | x4          | x5          | x6          | x7          | x8          | x9          | xA          | xB          | xC          | xD          | xE          | xF          |
|------------|------------|------------|------------|------------|------------|------------|------------|------------|------------|------------|------------|------------|------------|------------|------------|------------|
|0x           |[BRK](#misc)|[ORA](#or)|||[TRB](#test-reset-bit)|[ORA](#or)|[ASL](#asl)|[RMB0](#reset-memory-bit)|[PHP](#phx)|[ORA](#or)|[ASL](#asl)||[TRB](#test-reset-bit)|[ORA](#or)|[ASL](#asl)|[BBR0](#branch-on-bit-reset)|
|1x           |[BPL](#bxx)|[ORA](#or)|[ORA](#or)||[TRB](#test-reset-bit)|[ORA](#or)|[ASL](#asl)|[RMB1](#reset-memory-bit)|[CLC](#flags)|[ORA](#or)|[INC](#inc)||[TRB](#test-reset-bit)|[ORA](#or)|[ASL](#asl)|[BBR1](#branch-on-bit-reset)|
|2x           |[JSR](#jsr)|[AND](#and)|||[BIT](#bit)|[AND](#and)|[ROL](#rol)|[RMB2](#reset-memory-bit)|[PLP](#plx)|[AND](#and)|[ROL](#rol)||[BIT](#bit)|[AND](#and)|[ROL](#rol)|[BBR2](#branch-on-bit-reset)|
|3x           |[BMI](#bxx)|[AND](#and)|[AND](#and)||[BIT](#bit)|[AND](#and)|[ROL](#rol)|[RMB3](#reset-memory-bit)|[SEC](#flags)|[AND](#and)|[DEC](#dec)||[BIT](#bit)|[AND](#and)|[ROL](#rol)|[BBR3](#branch-on-bit-reset)|
|4x           |[RTI](#rtx)|[EOR](#eor)||||[EOR](#eor)|[LSR](#lsr)|[RMB4](#reset-memory-bit)|[PHA](#phx)|[EOR](#eor)|[LSR](#lsr)||[JMP](#jmp)|[EOR](#eor)|[LSR](#lsr)|[BBR4](#branch-on-bit-reset)|
|5x           |[BVC](#bxx)|[EOR](#eor)|[EOR](#eor)|||[EOR](#eor)|[LSR](#lsr)|[RMB5](#reset-memory-bit)|[CLI](#flags)|[EOR](#eor)|[PHY](#phx)|||[EOR](#eor)|[LSR](#lsr)|[BBR5](#branch-on-bit-reset)|
|6x           |[RTS](#rtx)|[ADC](#adc)|||[STZ](#store-z)|[ADC](#adc)|[ROR](#ror)|[RMB6](#reset-memory-bit)|[PLA](#plx)|[ADC](#adc)|[ROR](#ror)||[JMP](#jmp)|[ADC](#adc)|[ROR](#ror)|[BBR6](#branch-on-bit-reset)|
|7x           |[BVS](#bxx)|[ADC](#adc)|[ADC](#adc)||[STZ](#store-z)|[ADC](#adc)|[ROR](#ror)|[RMB7](#reset-memory-bit)|[SEI](#flags)|[ADC](#adc)|[PLY](#plx)||[JMP](#jmp)|[ADC](#adc)|[ROR](#ror)|[BBR7](#branch-on-bit-reset)|
|8x           |[BRA](#bxx)|[STA](#store-a)|||[STY](#store-y)|[STA](#store-a)|[STX](#store-x)|[SMB0](#set-memory-bit)|[DEY](#dec)|[BIT](#bit)|[TXA](#plx)||[STY](#store-y)|[STA](#store-a)|[STX](#store-x)|[BBS0](#branch-on-bit-set)|
|9x           |[BCC](#bxx)|[STA](#store-a)|[STA](#store-a)||[STY](#store-y)|[STA](#store-a)|[STX](#store-x)|[SMB1](#set-memory-bit)|[TYA](#plx)|[STA](#store-a)|[TXS](#plx)||[STZ](#store-z)|[STA](#store-a)|[STZ](#store-z)|[BBS1](#branch-on-bit-set)|
|Ax           |[LDY](#load-y)|[LDA](#load-a)|[LDX](#load-x)||[LDY](#load-y)|[LDA](#load-a)|[LDX](#load-x)|[SMB2](#set-memory-bit)|[TAY](#plx)|[LDA](#load-a)|[TAX](#plx)||[LDY](#load-y)|[LDA](#load-a)|[LDX](#load-x)|[BBS2](#branch-on-bit-set)|
|Bx           |[BCS](#bxx)|[LDA](#load-a)|[LDA](#load-a)||[LDY](#load-y)|[LDA](#load-a)|[LDX](#load-x)|[SMB3](#set-memory-bit)|[CLV](#flags)|[LDA](#load-a)|[TSX](#plx)||[LDY](#load-y)|[LDA](#load-a)|[LDX](#load-x)|[BBS3](#branch-on-bit-set)|
|Cx           |[CPY](#cpy)|[CMP](#cmp)|||[CPY](#cpy)|[CMP](#cmp)|[DEC](#dec)|[SMB4](#set-memory-bit)|[INY](#inc)|[CMP](#cmp)|[DEX](#dec)|[WAI](#misc)|[CPY](#cpy)|[CMP](#cmp)|[DEC](#dec)|[BBS4](#branch-on-bit-set)|
|Dx           |[BNE](#bxx)|[CMP](#cmp)|[CMP](#cmp)|||[CMP](#cmp)|[DEC](#dec)|[SMB5](#set-memory-bit)|[CLD](#flags)|[CMP](#cmp)|[PHX](#phx)|[STP](#misc)||[CMP](#cmp)|[DEC](#dec)|[BBS5](#branch-on-bit-set)|
|Ex           |[CPX](#cpx)|[SBC](#sbc)|||[CPX](#cpx)|[SBC](#sbc)|[INC](#inc)|[SMB6](#set-memory-bit)|[INX](#inc)|[SBC](#sbc)|[NOP](#misc)||[CPX](#cpx)|[SBC](#sbc)|[INC](#inc)|[BBS6](#branch-on-bit-set)|
|Fx           |[BEQ](#bxx)|[SBC](#sbc)|[SBC](#sbc)|||[SBC](#sbc)|[INC](#inc)|[SMB7](#set-memory-bit)|[SED](#flags)|[SBC](#sbc)|[PLX](#plx)|||[SBC](#sbc)|[INC](#inc)|[BBS7](#branch-on-bit-set)|

## Opcodes By Name

|     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| [ADC](#adc) | [SBC](#sbc) | [AND](#and) | [ORA](#or) | [EOR](#eor) | [ASL](#asl) | [LSR](#lsr) | [ROL](#rol) | [ROR](#ror) | [BCC](#bxx) | [BCS](#bxx) | [BEQ](#bxx) | [BMI](#bxx) | [BNE](#bxx) | [BPL](#bxx) | [BVC](#bxx) |
| [BVS](#bxx) | [BRA](#bxx) | [BIT](#bit) | [BRK](#misc) | [NOP](#misc) | [STP](#misc) | [WAI](#misc) | [CLC](#flags) | [CLD](#flags) | [CLI](#flags) | [CLV](#flags) | [SEC](#flags) | [SED](#flags) | [SEI](#flags) | [PHA](#phx) | [PHP](#phx) |
| [PHX](#phx) | [PHY](#phx) | [PLA](#plx) | [PLP](#plx) | [PLX](#plx) | [PLY](#plx) | [TAX](#plx) | [TXA](#plx) | [TAY](#plx) | [TYA](#plx) | [TSX](#plx) | [TXS](#plx) | [CMP](#cmp) | [CPX](#cpx) | [CPY](#cpy) | [DEC](#dec) |
| [DEX](#dec) | [DEY](#dec) | [INX](#inc) | [INY](#inc) | [INC](#inc) | [JMP](#jmp) | [JSR](#jsr) | [RTS](#rtx) | [RTI](#rtx) | [LDA](#load-a) | [LDX](#load-x) | [LDY](#load-y) | [STA](#store-a) | [STX](#store-x) | [STY](#store-y) | [STZ](#store-z) |
| [BBRx](#branch-on-bit-reset) | [BBSx](#branch-on-bit-set) | [RMBx](#reset-memory-bit) | [SMBx](#set-memory-bit) | [TRB](#test-reset-bit) |

## Opcodes By Category

|     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
|  Arithmetic | [ADC](#adc) | [SBC](#sbc) 
|  Boolean | [AND](#and) | [ORA](#or) | [EOR](#eor) 
|  Bit Shift | [ASL](#asl) | [LSR](#lsr) | [ROL](#rol) | [ROR](#ror) 
|  Branching | [BCC](#bxx) | [BCS](#bxx) | [BEQ](#bxx) | [BMI](#bxx) | [BNE](#bxx) | [BPL](#bxx) | [BVC](#bxx) | [BVS](#bxx) | [BRA](#bxx) | [JMP](#jmp) | [JSR](#jsr) | [RTS](#rtx) | [RTI](#rtx) 
|  Test Bit | [BIT](#bit) 
|  Misc | [BRK](#misc) | [NOP](#misc) | [STP](#misc) | [WAI](#misc) 
|  Flags | [CLC](#flags) | [CLD](#flags) | [CLI](#flags) | [CLV](#flags) | [SEC](#flags) | [SED](#flags) | [SEI](#flags) 
|  Stack | [PHA](#phx) | [PHP](#phx) | [PHX](#phx) | [PHY](#phx) | [PLA](#plx) | [PLP](#plx) | [PLX](#plx) | [PLY](#plx) | [TAX](#plx) | [TXA](#plx) | [TAY](#plx) | [TYA](#plx) | [TSX](#plx) | [TXS](#plx) 
|  Compare | [CMP](#cmp) | [CPX](#cpx) | [CPY](#cpy) 
|  Increment/Decrement | [DEC](#dec) | [DEX](#dec) | [DEY](#dec) 
|  IIncrement/Decrement | [INX](#inc) | [INY](#inc) | [INC](#inc) 
|  Load | [LDA](#load-a) | [LDX](#load-x) | [LDY](#load-y) 
|  Store | [STA](#store-a) | [STX](#store-x) | [STY](#store-y) | [STZ](#store-z) 
|  Branch | [BBRx](#branch-on-bit-reset) | [BBSx](#branch-on-bit-set) 
|  Memory Bit Operations | [RMBx](#reset-memory-bit) | [SMBx](#set-memory-bit) | [TRB](#test-reset-bit) 
|

### ADC
Add with Carry
```text
SYNTAX       MODE           HEX  LEN  CYCLES  FLAGS    
ADC #$12     Immediate      $69   2     2     CZ---VN
ADC $12      Zero Page      $65   2     3     CZ---VN
ADC $12,X    Zero Page,X    $75   2     4     CZ---VN
ADC $1234    Absolute       $6D   3     4     CZ---VN
ADC $1234,X  Absolute,X     $7D   3     4     CZ---VN
ADC $1234,Y  Absolute,Y     $79   3     4     CZ---VN
ADC ($12,X)  Indirect,X     $61   2     6     CZ---VN
ADC ($12),Y  Indirect,Y     $71   2     5     CZ---VN
ADC ($12)    ZP Indirect    $72   2     5     CZ---VN
```

Add a number to the accumulator. <br/>
Result is stored in A <br/>
 <br/>
This is an 8-bit add. Use the Carry (C) or Overflow (V) flags to determine <br/>
whether the result was too large for an 8 bit number. <br/>
 <br/>
If C is set before operation, then 1 will be added to the result. <br/>
 <br/>
C is set when result is more than 255 ($FF) <br/>
Z is set when result is zero <br/>
V is set when signed result crosses -128/+127 <br/>
N is set when result is negative (bit 7=1) <br/>

---
[top](#)


### AND
Logical And
```text
SYNTAX       MODE           HEX  LEN  CYCLES  FLAGS    
AND #$12     Immediate      $29   2     2     -Z----N
AND $12      Zero Page      $25   2     3     -Z----N
AND $12,X    Zero Page,X    $35   2     4     -Z----N
AND $1234    Absolute       $2D   3     4     -Z----N
AND $1234,X  Absolute,X     $3D   3     4     -Z----N
AND $1234,Y  Absolute,Y     $39   3     4     -Z----N
AND ($12,X)  Indirect,X     $21   2     6     -Z----N
AND ($12),Y  Indirect,Y     $31   2     5     -Z----N
AND ($12)    ZP Indirect    $32   2     5     -Z----N
```

Bitwise AND the provided value with the accumulator. <br/>
  - Sets N (Negative) flag if the bit 7 of the result is 1, and otherewise clears it <br/>
  - Sets Z (Zero) is the result is zero, and otherwise clears it <br/>

---
[top](#)


### ASL
Arithmetic Shift Left
```text
SYNTAX       MODE           HEX  LEN  CYCLES  FLAGS    
ASL A        Accumulator    $0A   1     2     CZ----N
ASL $12      Zero Page      $06   2     5     CZ----N
ASL $12,X    Zero Page,X    $16   2     6     CZ----N
ASL $1234    Absolute       $0E   3     6     CZ----N
ASL $1234,X  Absolute,X     $1E   3    6/7    CZ----N
```


---
[top](#)


### BIT
Test Bit
```text
SYNTAX       MODE           HEX  LEN  CYCLES  FLAGS    
BIT $12      Zero Page      $24   2     3     -Z---VN
BIT $1234    Absolute       $2C   3     4     -Z---VN
BIT #$12     Immediate      $89   2     2     -Z-----
BIT $12,X    Zero Page,X    $34   2     4     -Z---VN
BIT $1234,X  Absolute,X     $3C   3     4     -Z---VN
```


---
[top](#)


### Branch on Bit Reset

```text
SYNTAX       MODE           HEX  LEN  CYCLES  FLAGS    
BBR0 $1234   ZP Relative    $0F   3     5     -------
BBR1 $1234   ZP Relative    $1F   3     5     -------
BBR2 $1234   ZP Relative    $2F   3     5     -------
BBR3 $1234   ZP Relative    $3F   3     5     -------
BBR4 $1234   ZP Relative    $4F   3     5     -------
BBR5 $1234   ZP Relative    $5F   3     5     -------
BBR6 $1234   ZP Relative    $6F   3     5     -------
BBR7 $1234   ZP Relative    $7F   3     5     -------
```


---
[top](#)


### Branch on Bit Set

```text
SYNTAX       MODE           HEX  LEN  CYCLES  FLAGS    
BBS0 $1234   ZP Relative    $8F   3     5     -------
BBS1 $1234   ZP Relative    $9F   3     5     -------
BBS2 $1234   ZP Relative    $AF   3     5     -------
BBS3 $1234   ZP Relative    $BF   3     5     -------
BBS4 $1234   ZP Relative    $CF   3     5     -------
BBS5 $1234   ZP Relative    $DF   3     5     -------
BBS6 $1234   ZP Relative    $EF   3     5     -------
BBS7 $1234   ZP Relative    $FF   3     5     -------
```


---
[top](#)


### Bxx
Branch Instructions
```text
SYNTAX       MODE           HEX  LEN  CYCLES  FLAGS    
BCC $1234    Relative       $90   2    2/3    -------
BCS $1234    Relative       $B0   2    2/3    -------
BEQ $1234    Relative       $F0   2    2/3    -------
BMI $1234    Relative       $30   2    2/3    -------
BNE $1234    Relative       $D0   2    2/3    -------
BPL $1234    Relative       $10   2    2/3    -------
BVC $1234    Relative       $50   2    2/3    -------
BVS $1234    Relative       $70   2    2/3    -------
BRA $1234    Relative       $80   2    3/4    -------
```


---
[top](#)


### CMP
Compare A to memory
```text
SYNTAX       MODE           HEX  LEN  CYCLES  FLAGS    
CMP #$12     Immediate      $C9   2     2     CZ----N
CMP $12      Zero Page      $C5   2     3     CZ----N
CMP $12,X    Zero Page,X    $D5   2     4     CZ----N
CMP $1234    Absolute       $CD   3     4     CZ----N
CMP $1234,X  Absolute,X     $DD   3     4     CZ----N
CMP $1234,Y  Absolute,Y     $D9   3     4     CZ----N
CMP ($12,X)  Indirect,X     $C1   2     6     CZ----N
CMP ($12),Y  Indirect,Y     $D1   2     5     CZ----N
CMP ($12)    ZP Indirect    $D2   2     5     CZ----N
```


---
[top](#)


### CPX
Compare X to memory
```text
SYNTAX       MODE           HEX  LEN  CYCLES  FLAGS    
CPX #$12     Immediate      $E0   2     2     CZ----N
CPX $12      Zero Page      $E4   2     3     CZ----N
CPX $1234    Absolute       $EC   3     4     CZ----N
```


---
[top](#)


### CPY
Compare Y to memory
```text
SYNTAX       MODE           HEX  LEN  CYCLES  FLAGS    
CPY #$12     Immediate      $C0   2     2     CZ----N
CPY $12      Zero Page      $C4   2     3     CZ----N
CPY $1234    Absolute       $CC   3     4     CZ----N
```


---
[top](#)


### DEC
Decrement Value
```text
SYNTAX       MODE           HEX  LEN  CYCLES  FLAGS    
DEC $12      Zero Page      $C6   2     5     -Z----N
DEC $12,X    Zero Page,X    $D6   2     6     -Z----N
DEC $1234    Absolute       $CE   3     6     -Z----N
DEC $1234,X  Absolute,X     $DE   3     7     -Z----N
DEC A        Accumulator    $3A   1     2     -Z----N
DEX          Implied        $CA   1     2     -Z----N
DEY          Implied        $88   1     2     -Z----N
```


---
[top](#)


### EOR
Exclusive OR
```text
SYNTAX       MODE           HEX  LEN  CYCLES  FLAGS    
EOR #$12     Immediate      $49   2     2     -Z----N
EOR $12      Zero Page      $45   2     3     -Z----N
EOR $12,X    Zero Page,X    $55   2     4     -Z----N
EOR $1234    Absolute       $4D   3     4     -Z----N
EOR $1234,X  Absolute,X     $5D   3     4     -Z----N
EOR $1234,Y  Absolute,Y     $59   3     4     -Z----N
EOR ($12,X)  Indirect,X     $41   2     6     -Z----N
EOR ($12),Y  Indirect,Y     $51   2     5     -Z----N
EOR ($12)    ZP Indirect    $52   2     5     -Z----N
```


---
[top](#)


### Flags
Set and Clear Flags
```text
SYNTAX       MODE           HEX  LEN  CYCLES  FLAGS    
CLC          Implied        $18   1     2     C------
CLD          Implied        $D8   1     2     ---D---
CLI          Implied        $58   1     2     --I----
CLV          Implied        $B8   1     2     -----V-
SEC          Implied        $38   1     2     C------
SED          Implied        $F8   1     2     ---D---
SEI          Implied        $78   1     2     --I----
```


---
[top](#)


### INC
Increment Value
```text
SYNTAX       MODE           HEX  LEN  CYCLES  FLAGS    
INX          Implied        $E8   1     2     -Z----N
INY          Implied        $C8   1     2     -Z----N
INC $12      Zero Page      $E6   2     5     -Z----N
INC $12,X    Zero Page,X    $F6   2     6     -Z----N
INC $1234    Absolute       $EE   3     6     -Z----N
INC $1234,X  Absolute,X     $FE   3     7     -Z----N
INC A        Accumulator    $1A   1     2     -Z----N
```


---
[top](#)


### JMP
Jump to new address
```text
SYNTAX       MODE           HEX  LEN  CYCLES  FLAGS    
JMP $1234    Absolute       $4C   3     3     -------
JMP ($1234)  Indirect       $6C   3     5     -------
JMP $1234,X  Absolute,X     $7C   3     6     -------
```


---
[top](#)


### JSR
Jump to subroutine
```text
SYNTAX       MODE           HEX  LEN  CYCLES  FLAGS    
JSR $1234    Absolute       $20   3     6     -------
```


---
[top](#)


### LSR
Logical Shift Right
```text
SYNTAX       MODE           HEX  LEN  CYCLES  FLAGS    
LSR A        Accumulator    $4A   1     2     -Z----N
LSR $12      Zero Page      $46   2     5     -Z----N
LSR $12,X    Zero Page,X    $56   2     6     -Z----N
LSR $1234    Absolute       $4E   3     6     -Z----N
LSR $1234,X  Absolute,X     $5E   3    6/7    -Z----N
```


---
[top](#)


### Load A

```text
SYNTAX       MODE           HEX  LEN  CYCLES  FLAGS    
LDA #$12     Immediate      $A9   2     2     -Z----N
LDA $12      Zero Page      $A5   2     3     -Z----N
LDA $12,X    Zero Page,X    $B5   2     4     -Z----N
LDA $1234    Absolute       $AD   3     4     -Z----N
LDA $1234,X  Absolute,X     $BD   3     4     -Z----N
LDA $1234,Y  Absolute,Y     $B9   3     4     -Z----N
LDA ($12,X)  Indirect,X     $A1   2     6     -Z----N
LDA ($12),Y  Indirect,Y     $B1   2     5     -Z----N
LDA ($12)    ZP Indirect    $B2   2     5     -Z----N
```


---
[top](#)


### Load X

```text
SYNTAX       MODE           HEX  LEN  CYCLES  FLAGS    
LDX #$12     Immediate      $A2   2     2     -Z----N
LDX $12      Zero Page      $A6   2     3     -Z----N
LDX $12,Y    Zero Page,Y    $B6   2     4     -Z----N
LDX $1234    Absolute       $AE   3     4     -Z----N
LDX $1234,Y  Absolute,Y     $BE   3     4     -Z----N
```


---
[top](#)


### Load Y

```text
SYNTAX       MODE           HEX  LEN  CYCLES  FLAGS    
LDY #$12     Immediate      $A0   2     2     -Z----N
LDY $12      Zero Page      $A4   2     3     -Z----N
LDY $12,X    Zero Page,X    $B4   2     4     -Z----N
LDY $1234    Absolute       $AC   3     4     -Z----N
LDY $1234,X  Absolute,X     $BC   3     4     -Z----N
```


---
[top](#)


### Misc
Misc
```text
SYNTAX       MODE           HEX  LEN  CYCLES  FLAGS    
BRK          Implied        $00   1     7     ---DB--
NOP          Implied        $EA   1     2     -------
STP          Implied        $DB   1     3     -------
WAI          Implied        $CB   1     3     -------
```


---
[top](#)


### OR
Logical OR
```text
SYNTAX       MODE           HEX  LEN  CYCLES  FLAGS    
ORA #$12     Immediate      $09   2     2     -Z----N
ORA $12      Zero Page      $05   2     3     -Z----N
ORA $12,X    Zero Page,X    $15   2     4     -Z----N
ORA $1234    Absolute       $0D   3     4     -Z----N
ORA $1234,X  Absolute,X     $1D   3     4     -Z----N
ORA $1234,Y  Absolute,Y     $19   3     4     -Z----N
ORA ($12,X)  Indirect,X     $01   2     6     -Z----N
ORA ($12),Y  Indirect,Y     $11   2     5     -Z----N
ORA ($12)    ZP Indirect    $12   2     5     -Z----N
```

Perform a logical OR of the given value in A <br/>
(the accumulator) <br/>
 <br/>
See [EOR](#eor) for the exclusive-OR version. <br/>
  - Sets N (Negative) flag if the two's compliment value is negative <br/>
  - Sets Z (Zero) flag is the value is zero <br/>

---
[top](#)


### PHx
Push to stack
```text
SYNTAX       MODE           HEX  LEN  CYCLES  FLAGS    
PHA          Implied        $48   1     3     -------
PHP          Implied        $08   1     3     -------
PHX          Implied        $DA   1     3     -------
PHY          Implied        $5A   1     3     -------
```


---
[top](#)


### PLx
Pull from stack
```text
SYNTAX       MODE           HEX  LEN  CYCLES  FLAGS    
PLA          Implied        $68   1     4     -Z----N
PLP          Implied        $28   1     4     CZIDBVN
PLX          Implied        $FA   1     4     -Z----N
PLY          Implied        $7A   1     4     -Z----N
TAX          Implied        $AA   1     2     -Z----N
TXA          Implied        $8A   1     2     -Z----N
TAY          Implied        $A8   1     2     -Z----N
TYA          Implied        $98   1     2     -Z----N
TSX          Implied        $BA   1     2     -Z----N
TXS          Implied        $9A   1     2     -------
```


---
[top](#)


### ROL
Rotate Left
```text
SYNTAX       MODE           HEX  LEN  CYCLES  FLAGS    
ROL A        Accumulator    $2A   1     2     CZ----N
ROL $12      Zero Page      $26   2     5     CZ----N
ROL $12,X    Zero Page,X    $36   2     6     CZ----N
ROL $1234    Absolute       $2E   3     6     CZ----N
ROL $1234,X  Absolute,X     $3E   3    6/7    CZ----N
```


---
[top](#)


### ROR
Rotate Right
```text
SYNTAX       MODE           HEX  LEN  CYCLES  FLAGS    
ROR A        Accumulator    $6A   1     2     CZ----N
ROR $12      Zero Page      $66   2     5     CZ----N
ROR $12,X    Zero Page,X    $76   2     6     CZ----N
ROR $1234    Absolute       $7E   3     6     CZ----N
ROR $1234,X  Absolute,X     $6E   3    6/7    CZ----N
```


---
[top](#)


### RTx
Return from Subroutine or Interrupt
```text
SYNTAX       MODE           HEX  LEN  CYCLES  FLAGS    
RTS          Implied        $60   1     6     -------
RTI          Implied        $40   1     6     -------
```


---
[top](#)


### Reset Memory Bit

```text
SYNTAX       MODE           HEX  LEN  CYCLES  FLAGS    
RMB0 $12     Zero Page      $07   2     5     -------
RMB1 $12     Zero Page      $17   2     5     -------
RMB2 $12     Zero Page      $27   2     5     -------
RMB3 $12     Zero Page      $37   2     5     -------
RMB4 $12     Zero Page      $47   2     5     -------
RMB5 $12     Zero Page      $57   2     5     -------
RMB6 $12     Zero Page      $67   2     5     -------
RMB7 $12     Zero Page      $77   2     5     -------
```


---
[top](#)


### SBC
Subtract With Carry
```text
SYNTAX       MODE           HEX  LEN  CYCLES  FLAGS    
SBC #$12     Immediate      $E9   2     2     CZ---VN
SBC $12      Zero Page      $E5   2     3     CZ---VN
SBC $12,X    Zero Page,X    $F5   2     4     CZ---VN
SBC $1234    Absolute       $ED   3     4     CZ---VN
SBC $1234,X  Absolute,X     $FD   3     4     CZ---VN
SBC $1234,Y  Absolute,Y     $F9   3     4     CZ---VN
SBC ($12,X)  Indirect,X     $E1   2     6     CZ---VN
SBC ($12),Y  Indirect,Y     $F1   2     5     CZ---VN
SBC ($12)    ZP Indirect    $F2   2     5     CZ---VN
```

Subtract the operand from A <br/>
Result is in A <br/>
If C=0 will subtract 1 more. <br/>
 <br/>
This is an 8-bit subtract. Use the Carry (C) or Overflow (V) flags to <br/>
determine whether a borrow took place. <br/>
 <br/>
If C is cleared before operation, then 1 will be subtracted from result. <br/>
 <br/>
C is clear when result is less than 0. <br/>
Z is set when result is zero <br/>
V is set when signed result crosses -128/+127 <br/>
N is set when result is negative (bit 7=1) <br/>

---
[top](#)


### Set Memory Bit

```text
SYNTAX       MODE           HEX  LEN  CYCLES  FLAGS    
SMB0 $12     Zero Page      $87   2     5     -------
SMB1 $12     Zero Page      $97   2     5     -------
SMB2 $12     Zero Page      $A7   2     5     -------
SMB3 $12     Zero Page      $B7   2     5     -------
SMB4 $12     Zero Page      $C7   2     5     -------
SMB5 $12     Zero Page      $D7   2     5     -------
SMB6 $12     Zero Page      $E7   2     5     -------
SMB7 $12     Zero Page      $F7   2     5     -------
```


---
[top](#)


### Store A

```text
SYNTAX       MODE           HEX  LEN  CYCLES  FLAGS    
STA $12      Zero Page      $85   2     3     -------
STA $12,X    Zero Page,X    $95   2     4     -------
STA $1234    Absolute       $8D   3     4     -------
STA $1234,X  Absolute,X     $9D   3     5     -------
STA $1234,Y  Absolute,Y     $99   3     5     -------
STA ($12,X)  Indirect,X     $81   2     6     -------
STA ($12),Y  Indirect,Y     $91   2     6     -------
STA ($12)    ZP Indirect    $92   2     5     -------
```


---
[top](#)


### Store X

```text
SYNTAX       MODE           HEX  LEN  CYCLES  FLAGS    
STX $12      Zero Page      $86   2     3     -------
STX $12,Y    Zero Page,Y    $96   2     4     -------
STX $1234    Absolute       $8E   3     4     -------
```


---
[top](#)


### Store Y

```text
SYNTAX       MODE           HEX  LEN  CYCLES  FLAGS    
STY $12      Zero Page      $84   2     3     -------
STY $12,X    Zero Page,X    $94   2     4     -------
STY $1234    Absolute       $8C   3     4     -------
```


---
[top](#)


### Store Z

```text
SYNTAX       MODE           HEX  LEN  CYCLES  FLAGS    
STZ $12      Zero Page      $64   2     3     -------
STZ $12,X    Zero Page,X    $74   2     4     -------
STZ $1234    Absolute       $9C   3     4     -------
STZ $1234,X  Absolute,X     $9E   3     5     -------
```


---
[top](#)


### Test Reset Bit

```text
SYNTAX       MODE           HEX  LEN  CYCLES  FLAGS    
TRB $12      Zero Page      $14   2     5     -Z-----
TRB $1234    Absolute       $1C   3     5     -Z-----
TRB $12      Zero Page      $04   2     5     -Z-----
TRB $1234    Absolute       $0C   3     5     -Z-----
```


---
[top](#)

