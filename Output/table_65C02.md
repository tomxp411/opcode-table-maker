## Opcodes By Number
|            | x0          | x1          | x2          | x3          | x4          | x5          | x6          | x7          | x8          | x9          | xA          | xB          | xC          | xD          | xE          | xF          |
|------------|------------|------------|------------|------------|------------|------------|------------|------------|------------|------------|------------|------------|------------|------------|------------|------------|
|0x           |[BRK](#misc)|[ORA](#or)|||[TRB](#test-reset-bit)|[ORA](#or)|[ASL](#arithmetic-shift)|[RMB0](#rmb)|[PHP](#stack)|[ORA](#or)|[ASL](#arithmetic-shift)||[TRB](#test-reset-bit)|[ORA](#or)|[ASL](#arithmetic-shift)|[BBR0](#branch-on-bit)|
|1x           |[BPL](#branch)|[ORA](#or)|[ORA](#or)||[TRB](#test-reset-bit)|[ORA](#or)|[ASL](#arithmetic-shift)|[RMB1](#rmb)|[CLC](#clearset-flags)|[ORA](#or)|[INC](#incdec)||[TRB](#test-reset-bit)|[ORA](#or)|[ASL](#arithmetic-shift)|[BBR1](#branch-on-bit)|
|2x           |[JSR](#jump)|[AND](#logical-and)|||[BIT](#test-bit)|[AND](#logical-and)|[ROL](#rotate-bits)|[RMB2](#rmb)|[PLP](#stack)|[AND](#logical-and)|[ROL](#rotate-bits)||[BIT](#test-bit)|[AND](#logical-and)|[ROL](#rotate-bits)|[BBR2](#branch-on-bit)|
|3x           |[BMI](#branch)|[AND](#logical-and)|[AND](#logical-and)||[BIT](#test-bit)|[AND](#logical-and)|[ROL](#rotate-bits)|[RMB3](#rmb)|[SEC](#clearset-flags)|[AND](#logical-and)|[DEC](#incdec)||[BIT](#test-bit)|[AND](#logical-and)|[ROL](#rotate-bits)|[BBR3](#branch-on-bit)|
|4x           |[RTI](#stack)|[EOR](#exclusive-or)||||[EOR](#exclusive-or)|[LSR](#logical-shift)|[RMB4](#rmb)|[PHA](#stack)|[EOR](#exclusive-or)|[LSR](#logical-shift)||[JMP](#jump)|[EOR](#exclusive-or)|[LSR](#logical-shift)|[BBR4](#branch-on-bit)|
|5x           |[BVC](#branch)|[EOR](#exclusive-or)|[EOR](#exclusive-or)|||[EOR](#exclusive-or)|[LSR](#logical-shift)|[RMB5](#rmb)|[CLI](#clearset-flags)|[EOR](#exclusive-or)|[PHY](#stack)|||[EOR](#exclusive-or)|[LSR](#logical-shift)|[BBR5](#branch-on-bit)|
|6x           |[RTS](#stack)|[ADC](#add)|||[STZ](#store)|[ADC](#add)|[ROR](#rotate-bits)|[RMB6](#rmb)|[PLA](#stack)|[ADC](#add)|[ROR](#rotate-bits)||[JMP](#jump)|[ADC](#add)|[ROR](#rotate-bits)|[BBR6](#branch-on-bit)|
|7x           |[BVS](#branch)|[ADC](#add)|[ADC](#add)||[STZ](#store)|[ADC](#add)|[ROR](#rotate-bits)|[RMB7](#rmb)|[SEI](#clearset-flags)|[ADC](#add)|[PLY](#stack)||[JMP](#jump)|[ADC](#add)|[ROR](#rotate-bits)|[BBR7](#branch-on-bit)|
|8x           |[BRA](#branch)|[STA](#store)|||[STY](#store)|[STA](#store)|[STX](#store)|[SMB0](#smb)|[DEY](#incdec)|[BIT](#test-bit)|[TXA](#transfer)||[STY](#store)|[STA](#store)|[STX](#store)|[BBS0](#branch-on-bit)|
|9x           |[BCC](#branch)|[STA](#store)|[STA](#store)||[STY](#store)|[STA](#store)|[STX](#store)|[SMB1](#smb)|[TYA](#transfer)|[STA](#store)|[TXS](#transfer)||[STZ](#store)|[STA](#store)|[STZ](#store)|[BBS1](#branch-on-bit)|
|Ax           |[LDY](#load)|[LDA](#load)|[LDX](#load)||[LDY](#load)|[LDA](#load)|[LDX](#load)|[SMB2](#smb)|[TAY](#transfer)|[LDA](#load)|[TAX](#transfer)||[LDY](#load)|[LDA](#load)|[LDX](#load)|[BBS2](#branch-on-bit)|
|Bx           |[BCS](#branch)|[LDA](#load)|[LDA](#load)||[LDY](#load)|[LDA](#load)|[LDX](#load)|[SMB3](#smb)|[CLV](#clearset-flags)|[LDA](#load)|[TSX](#transfer)||[LDY](#load)|[LDA](#load)|[LDX](#load)|[BBS3](#branch-on-bit)|
|Cx           |[CPY](#compare)|[CMP](#compare)|||[CPY](#compare)|[CMP](#compare)|[DEC](#incdec)|[SMB4](#smb)|[INY](#incdec)|[CMP](#compare)|[DEX](#incdec)|[WAI](#misc)|[CPY](#compare)|[CMP](#compare)|[DEC](#incdec)|[BBS4](#branch-on-bit)|
|Dx           |[BNE](#branch)|[CMP](#compare)|[CMP](#compare)|||[CMP](#compare)|[DEC](#incdec)|[SMB5](#smb)|[CLD](#clearset-flags)|[CMP](#compare)|[PHX](#stack)|[STP](#misc)||[CMP](#compare)|[DEC](#incdec)|[BBS5](#branch-on-bit)|
|Ex           |[CPX](#compare)|[SBC](#subtract)|||[CPX](#compare)|[SBC](#subtract)|[INC](#incdec)|[SMB6](#smb)|[INX](#incdec)|[SBC](#subtract)|[NOP](#misc)||[CPX](#compare)|[SBC](#subtract)|[INC](#incdec)|[BBS6](#branch-on-bit)|
|Fx           |[BEQ](#branch)|[SBC](#subtract)|[SBC](#subtract)|||[SBC](#subtract)|[INC](#incdec)|[SMB7](#smb)|[SED](#clearset-flags)|[SBC](#subtract)|[PLX](#stack)|||[SBC](#subtract)|[INC](#incdec)|[BBS7](#branch-on-bit)|
## Opcodes By name

[ADC](#add)
[AND](#logical-and)
[ASL](#arithmetic-shift)
[LSR](#logical-shift)
[ROL ROR](#rotate-bits)
[BBRx BBSx](#branch-on-bit)
[BCC BCS BEQ BMI BNE BPL BVC BVS BRA](#branch)
[BIT](#test-bit)
[BRK NOP STP WAI](#misc)
[CLC CLD CLI CLV SEC SED SEI](#clearset-flags)
[PHA PLA PHP PLP PHX PHY PLX PLY RTI RTS](#stack)
[TAX TXA TAY TYA TSX TXS](#transfer)
[CMP CPX CPY](#compare)
[DEC DEX DEY INX INY INC](#incdec)
[EOR](#exclusive-or)
[JMP JSR](#jump)
[LDA LDX LDY](#load)
[ORA](#or)
[RMBx](#rmb)
[SMBx](#smb)
[SBC](#subtract)
[STA STX STY STZ](#store)
[TRB](#test-reset-bit)

### Add

```text
SYNTAX       HEX  LEN  CYCLES  FLAGS    
ADC #$12     $69  2       2    CZ---VN
ADC $12      $65  2       3    CZ---VN
ADC $12,X    $75  2       4    CZ---VN
ADC $1234    $6D  3       4    CZ---VN
ADC $1234,X  $7D  3       4    CZ---VN
ADC $1234,Y  $79  3       4    CZ---VN
ADC ($12,X)  $61  2       6    CZ---VN
ADC ($12),Y  $71  2       5    CZ---VN
ADC ($12)    $72  2       5    CZ---VN
```

Add a number to the accumulator <br/>
This is an 8-bit add. Use the Carry (C) or Overflow (V) flags to determine <br/>
whether the result was too large for an 8 bit number <br/>
 <br/>
Result is stored in A <br/>
C is set when result is more than 255 ($FF) <br/>
Z is set when result is zero <br/>
V is set when signed result exceeds -128 to 127 <br/>
N is set when result is negative (bit 7=1) <br/>

---
[top](#)


### Logical AND

```text
SYNTAX       HEX  LEN  CYCLES  FLAGS    
AND #$12     $29  2       2    -Z----N
AND $12      $25  2       3    -Z----N
AND $12,X    $35  2       4    -Z----N
AND $1234    $2D  3       4    -Z----N
AND $1234,X  $3D  3       4    -Z----N
AND $1234,Y  $39  3       4    -Z----N
AND ($12,X)  $21  2       6    -Z----N
AND ($12),Y  $31  2       5    -Z----N
AND ($12)    $32  2       5    -Z----N
```


---
[top](#)


### Arithmetic Shift

```text
SYNTAX       HEX  LEN  CYCLES  FLAGS    
ASL A        $0A  1       2    CZ----N
ASL $12      $06  2       5    CZ----N
ASL $12,X    $16  2       6    CZ----N
ASL $1234    $0E  3       6    CZ----N
ASL $1234,X  $1E  3     6/7    CZ----N
```


---
[top](#)


### Logical Shift

```text
SYNTAX       HEX  LEN  CYCLES  FLAGS    
LSR A        $4A  1       2    -Z----N
LSR $12      $46  2       5    -Z----N
LSR $12,X    $56  2       6    -Z----N
LSR $1234    $4E  3       6    -Z----N
LSR $1234,X  $5E  3     6/7    -Z----N
```


---
[top](#)


### Rotate Bits

```text
SYNTAX       HEX  LEN  CYCLES  FLAGS    
ROL A        $2A  1       2    CZ----N
ROL $12      $26  2       5    CZ----N
ROL $12,X    $36  2       6    CZ----N
ROL $1234    $2E  3       6    CZ----N
ROL $1234,X  $3E  3     6/7    CZ----N
ROR A        $6A  1       2    CZ----N
ROR $12      $66  2       5    CZ----N
ROR $12,X    $76  2       6    CZ----N
ROR $1234    $7E  3       6    CZ----N
ROR $1234,X  $6E  3     6/7    CZ----N
```


---
[top](#)


### Branch on Bit

```text
SYNTAX       HEX  LEN  CYCLES  FLAGS    
BBR0 $1234   $0F  3       5    -z-----
BBR1 $1234   $1F  3       5    -z-----
BBR2 $1234   $2F  3       5    -z-----
BBR3 $1234   $3F  3       5    -z-----
BBR4 $1234   $4F  3       5    -z-----
BBR5 $1234   $5F  3       5    -z-----
BBR6 $1234   $6F  3       5    -z-----
BBR7 $1234   $7F  3       5    -z-----
BBS0 $1234   $8F  3       5    -z-----
BBS1 $1234   $9F  3       5    -z-----
BBS2 $1234   $AF  3       5    -z-----
BBS3 $1234   $BF  3       5    -z-----
BBS4 $1234   $CF  3       5    -z-----
BBS5 $1234   $DF  3       5    -z-----
BBS6 $1234   $EF  3       5    -z-----
BBS7 $1234   $FF  3       5    -z-----
```


---
[top](#)


### Branch

```text
SYNTAX       HEX  LEN  CYCLES  FLAGS    
BCC $1234    $90  2     2/3    -z-----
BCS $1234    $B0  2     2/3    -z-----
BEQ $1234    $F0  2     2/3    -z-----
BMI $1234    $30  2     2/3    -z-----
BNE $1234    $D0  2     2/3    -z-----
BPL $1234    $10  2     2/3    -z-----
BVC $1234    $50  2     2/3    -z-----
BVS $1234    $70  2     2/3    -z-----
BRA $1234    $80  2     3/4    -z-----
```


---
[top](#)


### Test Bit

```text
SYNTAX       HEX  LEN  CYCLES  FLAGS    
BIT $12      $24  2       3    -Z---VN
BIT $1234    $2C  3       4    -Z---VN
BIT #$12     $89  2       2    -Z-----
BIT $12,X    $34  2       4    -Z---VN
BIT $1234,X  $3C  3       4    -Z---VN
```


---
[top](#)


### Misc

```text
SYNTAX       HEX  LEN  CYCLES  FLAGS    
BRK          $00  1       7    -z-DB--
NOP          $EA  1       2    -z-----
STP          $DB  1       3    -z-----
WAI          $CB  1       3    -z-----
```


---
[top](#)


### Clear/Set Flags

```text
SYNTAX       HEX  LEN  CYCLES  FLAGS    
CLC          $18  1       2    Cz-----
CLD          $D8  1       2    -z-D---
CLI          $58  1       2    -zI----
CLV          $B8  1       2    -z---V-
SEC          $38  1       2    Cz-----
SED          $F8  1       2    -z-D---
SEI          $78  1       2    -zI----
```


---
[top](#)


### Stack

```text
SYNTAX       HEX  LEN  CYCLES  FLAGS    
PHA          $48  1       3    -z-----
PLA          $68  1       4    -Z----N
PHP          $08  1       3    -z-----
PLP          $28  1       4    CZIDBVN
PHX          $DA  1       3    -z-----
PHY          $5A  1       3    -z-----
PLX          $FA  1       4    -Z----N
PLY          $7A  1       4    -Z----N
RTI          $40  1       6    -z-----
RTS          $60  1       6    -z-----
```


---
[top](#)


### Transfer

```text
SYNTAX       HEX  LEN  CYCLES  FLAGS    
TAX          $AA  1       2    -Z----N
TXA          $8A  1       2    -Z----N
TAY          $A8  1       2    -Z----N
TYA          $98  1       2    -Z----N
TSX          $BA  1       2    -Z----N
TXS          $9A  1       2    -z-----
```


---
[top](#)


### Compare

```text
SYNTAX       HEX  LEN  CYCLES  FLAGS    
CMP #$12     $C9  2       2    CZ----N
CMP $12      $C5  2       3    CZ----N
CMP $12,X    $D5  2       4    CZ----N
CMP $1234    $CD  3       4    CZ----N
CMP $1234,X  $DD  3       4    CZ----N
CMP $1234,Y  $D9  3       4    CZ----N
CMP ($12,X)  $C1  2       6    CZ----N
CMP ($12),Y  $D1  2       5    CZ----N
CMP ($12)    $D2  2       5    CZ----N
CPX #$12     $E0  2       2    CZ----N
CPX $12      $E4  2       3    CZ----N
CPX $1234    $EC  3       4    CZ----N
CPY #$12     $C0  2       2    CZ----N
CPY $12      $C4  2       3    CZ----N
CPY $1234    $CC  3       4    CZ----N
```


---
[top](#)


### Inc/Dec

```text
SYNTAX       HEX  LEN  CYCLES  FLAGS    
DEC $12      $C6  2       5    -Z----N
DEC $12,X    $D6  2       6    -Z----N
DEC $1234    $CE  3       6    -Z----N
DEC $1234,X  $DE  3       7    -Z----N
DEC A        $3A  1       2    -Z----N
DEX          $CA  1       2    -Z----N
DEY          $88  1       2    -Z----N
INX          $E8  1       2    -Z----N
INY          $C8  1       2    -Z----N
INC $12      $E6  2       5    -Z----N
INC $12,X    $F6  2       6    -Z----N
INC $1234    $EE  3       6    -Z----N
INC $1234,X  $FE  3       7    -Z----N
INC A        $1A  1       2    -Z----N
```


---
[top](#)


### Exclusive OR

```text
SYNTAX       HEX  LEN  CYCLES  FLAGS    
EOR #$12     $49  2       2    -Z----N
EOR $12      $45  2       3    -Z----N
EOR $12,X    $55  2       4    -Z----N
EOR $1234    $4D  3       4    -Z----N
EOR $1234,X  $5D  3       4    -Z----N
EOR $1234,Y  $59  3       4    -Z----N
EOR ($12,X)  $41  2       6    -Z----N
EOR ($12),Y  $51  2       5    -Z----N
EOR ($12)    $52  2       5    -Z----N
```


---
[top](#)


### Jump

```text
SYNTAX       HEX  LEN  CYCLES  FLAGS    
JMP $1234    $4C  3       3    -z-----
JMP ($1234)  $6C  3       5    -z-----
JMP $1234,X  $7C  3       6    -z-----
JSR $1234    $20  3       6    -z-----
```


---
[top](#)


### Load

```text
SYNTAX       HEX  LEN  CYCLES  FLAGS    
LDA #$12     $A9  2       2    -Z----N
LDA $12      $A5  2       3    -Z----N
LDA $12,X    $B5  2       4    -Z----N
LDA $1234    $AD  3       4    -Z----N
LDA $1234,X  $BD  3       4    -Z----N
LDA $1234,Y  $B9  3       4    -Z----N
LDA ($12,X)  $A1  2       6    -Z----N
LDA ($12),Y  $B1  2       5    -Z----N
LDA ($12)    $B2  2       5    -Z----N
LDX #$12     $A2  2       2    -Z----N
LDX $12      $A6  2       3    -Z----N
LDX $12,Y    $B6  2       4    -Z----N
LDX $1234    $AE  3       4    -Z----N
LDX $1234,Y  $BE  3       4    -Z----N
LDY #$12     $A0  2       2    -Z----N
LDY $12      $A4  2       3    -Z----N
LDY $12,X    $B4  2       4    -Z----N
LDY $1234    $AC  3       4    -Z----N
LDY $1234,X  $BC  3       4    -Z----N
```


---
[top](#)


### OR

```text
SYNTAX       HEX  LEN  CYCLES  FLAGS    
ORA #$12     $09  2       2    -Z----N
ORA $12      $05  2       3    -Z----N
ORA $12,X    $15  2       4    -Z----N
ORA $1234    $0D  3       4    -Z----N
ORA $1234,X  $1D  3       4    -Z----N
ORA $1234,Y  $19  3       4    -Z----N
ORA ($12,X)  $01  2       6    -Z----N
ORA ($12),Y  $11  2       5    -Z----N
ORA ($12)    $12  2       5    -Z----N
```


---
[top](#)


### RMB

```text
SYNTAX       HEX  LEN  CYCLES  FLAGS    
RMB0 $12     $07  2       5    -z-----
RMB1 $12     $17  2       5    -z-----
RMB2 $12     $27  2       5    -z-----
RMB3 $12     $37  2       5    -z-----
RMB4 $12     $47  2       5    -z-----
RMB5 $12     $57  2       5    -z-----
RMB6 $12     $67  2       5    -z-----
RMB7 $12     $77  2       5    -z-----
```


---
[top](#)


### SMB

```text
SYNTAX       HEX  LEN  CYCLES  FLAGS    
SMB0 $12     $87  2       5    -z-----
SMB1 $12     $97  2       5    -z-----
SMB2 $12     $A7  2       5    -z-----
SMB3 $12     $B7  2       5    -z-----
SMB4 $12     $C7  2       5    -z-----
SMB5 $12     $D7  2       5    -z-----
SMB6 $12     $E7  2       5    -z-----
SMB7 $12     $F7  2       5    -z-----
```


---
[top](#)


### Subtract

```text
SYNTAX       HEX  LEN  CYCLES  FLAGS    
SBC #$12     $E9  2       2    CZ---VN
SBC $12      $E5  2       3    CZ---VN
SBC $12,X    $F5  2       4    CZ---VN
SBC $1234    $ED  3       4    CZ---VN
SBC $1234,X  $FD  3       4    CZ---VN
SBC $1234,Y  $F9  3       4    CZ---VN
SBC ($12,X)  $E1  2       6    CZ---VN
SBC ($12),Y  $F1  2       5    CZ---VN
SBC ($12)    $F2  2       5    CZ---VN
```


---
[top](#)


### Store

```text
SYNTAX       HEX  LEN  CYCLES  FLAGS    
STA $12      $85  2       3    -z-----
STA $12,X    $95  2       4    -z-----
STA $1234    $8D  3       4    -z-----
STA $1234,X  $9D  3       5    -z-----
STA $1234,Y  $99  3       5    -z-----
STA ($12,X)  $81  2       6    -z-----
STA ($12),Y  $91  2       6    -z-----
STA ($12)    $92  2       5    -z-----
STX $12      $86  2       3    -z-----
STX $12,Y    $96  2       4    -z-----
STX $1234    $8E  3       4    -z-----
STY $12      $84  2       3    -z-----
STY $12,X    $94  2       4    -z-----
STY $1234    $8C  3       4    -z-----
STZ $12      $64  2       3    -z-----
STZ $12,X    $74  2       4    -z-----
STZ $1234    $9C  3       4    -z-----
STZ $1234,X  $9E  3       5    -z-----
```


---
[top](#)


### Test Reset Bit

```text
SYNTAX       HEX  LEN  CYCLES  FLAGS    
TRB $12      $14  2       5    -Z-----
TRB $1234    $1C  3       5    -Z-----
TRB $12      $04  2       5    -Z-----
TRB $1234    $0C  3       5    -Z-----
```


---
[top](#)

