## Opcodes By Number

|            | x0          | x1          | x2          | x3          | x4          | x5          | x6          | x7          | x8          | x9          | xA          | xB          | xC          | xD          | xE          | xF          |
|------------|------------|------------|------------|------------|------------|------------|------------|------------|------------|------------|------------|------------|------------|------------|------------|------------|
|0x           |[BRK](#brk)|[ORA](#or)|||[TRB](#trb)|[ORA](#or)|[ASL](#asl)|[RMB0](#rmbx)|[PHP](#phx)|[ORA](#or)|[ASL](#asl)||[TRB](#trb)|[ORA](#or)|[ASL](#asl)|[BBR0](#bbrx)|
|1x           |[BPL](#bra)|[ORA](#or)|[ORA](#or)||[TRB](#trb)|[ORA](#or)|[ASL](#asl)|[RMB1](#rmbx)|[CLC](#clc)|[ORA](#or)|[INC](#inc)||[TRB](#trb)|[ORA](#or)|[ASL](#asl)|[BBR1](#bbrx)|
|2x           |[JSR](#jsr)|[AND](#and)|||[BIT](#bit)|[AND](#and)|[ROL](#rol)|[RMB2](#rmbx)|[PLP](#plx)|[AND](#and)|[ROL](#rol)||[BIT](#bit)|[AND](#and)|[ROL](#rol)|[BBR2](#bbrx)|
|3x           |[BMI](#bra)|[AND](#and)|[AND](#and)||[BIT](#bit)|[AND](#and)|[ROL](#rol)|[RMB3](#rmbx)|[SEC](#sec)|[AND](#and)|[DEC](#dec)||[BIT](#bit)|[AND](#and)|[ROL](#rol)|[BBR3](#bbrx)|
|4x           |[RTI](#rti)|[EOR](#eor)||||[EOR](#eor)|[LSR](#lsr)|[RMB4](#rmbx)|[PHA](#phx)|[EOR](#eor)|[LSR](#lsr)||[JMP](#jmp)|[EOR](#eor)|[LSR](#lsr)|[BBR4](#bbrx)|
|5x           |[BVC](#bra)|[EOR](#eor)|[EOR](#eor)|||[EOR](#eor)|[LSR](#lsr)|[RMB5](#rmbx)|[CLI](#cli)|[EOR](#eor)|[PHY](#phx)|||[EOR](#eor)|[LSR](#lsr)|[BBR5](#bbrx)|
|6x           |[RTS](#rts)|[ADC](#adc)|||[STZ](#stz)|[ADC](#adc)|[ROR](#ror)|[RMB6](#rmbx)|[PLA](#plx)|[ADC](#adc)|[ROR](#ror)||[JMP](#jmp)|[ADC](#adc)|[ROR](#ror)|[BBR6](#bbrx)|
|7x           |[BVS](#bra)|[ADC](#adc)|[ADC](#adc)||[STZ](#stz)|[ADC](#adc)|[ROR](#ror)|[RMB7](#rmbx)|[SEI](#sei)|[ADC](#adc)|[PLY](#plx)||[JMP](#jmp)|[ADC](#adc)|[ROR](#ror)|[BBR7](#bbrx)|
|8x           |[BRA](#bra)|[STA](#sta)|||[STY](#sty)|[STA](#sta)|[STX](#stx)|[SMB0](#smbx)|[DEY](#dec)|[BIT](#bit)|[TXA](#txx)||[STY](#sty)|[STA](#sta)|[STX](#stx)|[BBS0](#bbsx)|
|9x           |[BCC](#bra)|[STA](#sta)|[STA](#sta)||[STY](#sty)|[STA](#sta)|[STX](#stx)|[SMB1](#smbx)|[TYA](#txx)|[STA](#sta)|[TXS](#txx)||[STZ](#stz)|[STA](#sta)|[STZ](#stz)|[BBS1](#bbsx)|
|Ax           |[LDY](#ldy)|[LDA](#lda)|[LDX](#ldx)||[LDY](#ldy)|[LDA](#lda)|[LDX](#ldx)|[SMB2](#smbx)|[TAY](#txx)|[LDA](#lda)|[TAX](#txx)||[LDY](#ldy)|[LDA](#lda)|[LDX](#ldx)|[BBS2](#bbsx)|
|Bx           |[BCS](#bra)|[LDA](#lda)|[LDA](#lda)||[LDY](#ldy)|[LDA](#lda)|[LDX](#ldx)|[SMB3](#smbx)|[CLV](#clv)|[LDA](#lda)|[TSX](#txx)||[LDY](#ldy)|[LDA](#lda)|[LDX](#ldx)|[BBS3](#bbsx)|
|Cx           |[CPY](#cpy)|[CMP](#cmp)|||[CPY](#cpy)|[CMP](#cmp)|[DEC](#dec)|[SMB4](#smbx)|[INY](#inc)|[CMP](#cmp)|[DEX](#dec)|[WAI](#wai)|[CPY](#cpy)|[CMP](#cmp)|[DEC](#dec)|[BBS4](#bbsx)|
|Dx           |[BNE](#bra)|[CMP](#cmp)|[CMP](#cmp)|||[CMP](#cmp)|[DEC](#dec)|[SMB5](#smbx)|[CLD](#cld)|[CMP](#cmp)|[PHX](#phx)|[STP](#stp)||[CMP](#cmp)|[DEC](#dec)|[BBS5](#bbsx)|
|Ex           |[CPX](#cpx)|[SBC](#sbc)|||[CPX](#cpx)|[SBC](#sbc)|[INC](#inc)|[SMB6](#smbx)|[INX](#inc)|[SBC](#sbc)|[NOP](#nop)||[CPX](#cpx)|[SBC](#sbc)|[INC](#inc)|[BBS6](#bbsx)|
|Fx           |[BEQ](#bra)|[SBC](#sbc)|[SBC](#sbc)|||[SBC](#sbc)|[INC](#inc)|[SMB7](#smbx)|[SED](#sed)|[SBC](#sbc)|[PLX](#plx)|||[SBC](#sbc)|[INC](#inc)|[BBS7](#bbsx)|

## Opcodes By Name

|     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| [ADC](#adc) | [AND](#and) | [ASL](#asl) | [BBRx](#bbrx) | [BBSx](#bbsx) | [BCC](#bra) | [BCS](#bra) | [BEQ](#bra) | [BIT](#bit) | [BMI](#bra) | [BNE](#bra) | [BPL](#bra) | [BRA](#bra) | [BRK](#brk) | [BVC](#bra) | [BVS](#bra) |
| [CLC](#clc) | [CLD](#cld) | [CLI](#cli) | [CLV](#clv) | [CMP](#cmp) | [CPX](#cpx) | [CPY](#cpy) | [DEC](#dec) | [DEX](#dec) | [DEY](#dec) | [EOR](#eor) | [INC](#inc) | [INX](#inc) | [INY](#inc) | [JMP](#jmp) | [JSR](#jsr) |
| [LDA](#lda) | [LDX](#ldx) | [LDY](#ldy) | [LSR](#lsr) | [NOP](#nop) | [ORA](#or) | [PHA](#phx) | [PHP](#phx) | [PHX](#phx) | [PHY](#phx) | [PLA](#plx) | [PLP](#plx) | [PLX](#plx) | [PLY](#plx) | [RMBx](#rmbx) | [ROL](#rol) |
| [ROR](#ror) | [RTI](#rti) | [RTS](#rts) | [SBC](#sbc) | [SEC](#sec) | [SED](#sed) | [SEI](#sei) | [SMBx](#smbx) | [STA](#sta) | [STP](#stp) | [STX](#stx) | [STY](#sty) | [STZ](#stz) | [TAX](#txx) | [TAY](#txx) | [TRB](#trb) |
| [TSX](#txx) | [TXA](#txx) | [TXS](#txx) | [TYA](#txx) | [WAI](#wai) |

## Opcodes By Category

|     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
|  Arithmetic | [ADC](#adc) | [SBC](#sbc) |
|  Boolean | [AND](#and) | [ORA](#or) | [EOR](#eor) |
|  Bit Shift | [ASL](#asl) | [LSR](#lsr) | [ROL](#rol) | [ROR](#ror) |
|  Branch | [BBRx](#bbrx) | [BBSx](#bbsx) |
|  Test Bit | [BIT](#bit) | [TRB](#trb) |
|  Branching | [BCC](#bra) | [BCS](#bra) | [BEQ](#bra) | [BMI](#bra) | [BNE](#bra) | [BPL](#bra) | [BVC](#bra) | [BVS](#bra) | [BRA](#bra) | [JMP](#jmp) | [JSR](#jsr) | [RTS](#rts) | [RTI](#rti) |
|  Misc | [BRK](#brk) | [NOP](#nop) | [STP](#stp) | [WAI](#wai) |
|  Flags | [CLC](#clc) | [CLD](#cld) | [CLI](#cli) | [CLV](#clv) | [SEC](#sec) | [SED](#sed) | [SEI](#sei) |
|  Compare | [CMP](#cmp) | [CPX](#cpx) | [CPY](#cpy) |
|  Increment/Decrement | [DEC](#dec) | [DEX](#dec) | [DEY](#dec) | [INX](#inc) | [INY](#inc) | [INC](#inc) |
|  Load Data | [LDA](#lda) | [LDX](#ldx) | [LDY](#ldy) |
|  Stack | [PHA](#phx) | [PHP](#phx) | [PHX](#phx) | [PHY](#phx) | [PLA](#plx) | [PLP](#plx) | [PLX](#plx) | [PLY](#plx) |
|  Transfer | [TAX](#txx) | [TXA](#txx) | [TAY](#txx) | [TYA](#txx) | [TSX](#txx) | [TXS](#txx) |
|  Store Data | [STA](#sta) | [STX](#stx) | [STY](#sty) | [STZ](#stz) |
|  Bit Operations | [RMBx](#rmbx) | [SMBx](#smbx) |

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
ADC ($12)    ZP Indirect    $72   2     5     CZ---VN +c
```

Add a number to the Accumulator and stores the result in A.

Use the Carry (C) or Overflow (V) flags to determine whether the result was too
large for an 8 bit number.

If C is set before operation, then 1 will be added to the result.
 
C is set when result is more than 255 ($FF)<br/>
Z is set when result is zero<br/>
V is set when signed result is too large. (Goes below -128 or above 127).<br/>
N is set when result is negative (bit 7=1)<br/>

+c new for 65C02


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
AND ($12)    ZP Indirect    $32   2     5     -Z----N +c
```

Bitwise AND the provided value with the Accumulator.

- Sets N (Negative) flag if the bit 7 of the result is 1, and otherewise
clears it.
- Sets Z (Zero) is the result is zero, and otherwise clears it<br/>

`AND #$FF` will leave A unaffected (but still set the flags).<br/>
`AND #$00` will clear A. 
`AND #$0F` will clear the high nibble of A, leaving a value of $00 to $0F
in A. 

| M | A | Result |
|---|---|--------|
| 0 | 0 |   0    |
| 0 | 1 |   0    |
| 1 | 0 |   0    |
| 1 | 1 |   1    |

+c new for 65C02


---
[top](#)


### ASL

Arithmetic Shift Left


```text
SYNTAX       MODE           HEX  LEN  CYCLES  FLAGS    
ASL A        Accumulator    $0A   1     2     CZ----N +c
ASL $12      Zero Page      $06   2     5     CZ----N +c
ASL $12,X    Zero Page,X    $16   2     6     CZ----N +c
ASL $1234    Absolute       $0E   3     6     CZ----N +c
ASL $1234,X  Absolute,X     $1E   3    6/7    CZ----N +p
```

Shifts all bits to the left by one position, through the Carry bit.

The Carry bit is shifted into bit 0.<br/>
Bit 7 is shifted into Carry.<br/>

[LSR](#lsr) works the same way, but shifts to the right, through the carry bit.

[ROL](#rol) is similar, except that ROL shifts bit 7 directly into bit 0 and to
Carry.

+p Adds a cycle if ,X crosses a page boundary.<br/>
+c New for the 65C02<br/>


---
[top](#)


### BBRx

Branch on Bit Reset


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

Branch to LABEL if bit x of zero page address is 0 where x is the number of the 
specific bit (0-7).

Specific to the 65C02 (*unavailable on the 65C816*)

#### Example

```asm
  check_flag:
    BBR3 zeropage_flag, flag_not_set
  flag_set:
    NOP
    ...
  flag_not_set:
    NOP
    ...
```
The above BBR3 looks at value in zeropage_flag (here it's a label to an actual
zero page address) and if bit 3 of the value is *zero* the branch would be
taken to `@flag_not_set`.


---
[top](#)


### BBSx

Branch on Bit Set


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


Branch to LABEL if bit x of zero page address is 1 where x is the number 
of the specific bit (0-7).

Specific to the 65C02 (*unavailable on the 65C816*)

#### Example (ca65)

```
  @check_flag:
    BBS3 zeropage_flag, @flag_set
  @flag_not_set:
    NOP
    ...
  @flag_set:
    NOP
    ...
```

The above BBR3 looks at value in zeropage_flag (here it's a label to an actual
zero page address) and if bit 3 of the value is *zero* the branch would be
taken to `@flag_set`.


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

- Sets Z (Zero) flag based on an AND of value provided to the Accumulator.
- Sets N (Negative) flag to the value of bit 7 at the provided address.
- Sets V (Overflow) flag to the value of bit 6 at the provided addres.


---
[top](#)


### BRA

Branch Instructions


```text
SYNTAX       MODE           HEX  LEN  CYCLES  FLAGS    
BCC $1234    Relative       $90   2    2/3    ------- +p Carry Clear
BCS $1234    Relative       $B0   2    2/3    ------- +p Carry Set
BEQ $1234    Relative       $F0   2    2/3    ------- +p Equal: Zero bit set
BMI $1234    Relative       $30   2    2/3    ------- +p Negative bit set
BNE $1234    Relative       $D0   2    2/3    ------- +p Not Equal: Zero bit clear
BPL $1234    Relative       $10   2    2/3    ------- +p Negative bit not set
BVC $1234    Relative       $50   2    2/3    ------- +p oVerflow Clear
BVS $1234    Relative       $70   2    2/3    ------- +p oVerflow Set
BRA $1234    Relative       $80   2    3/4    ------- +p Always
```

The branch instructions take the branch when the related flag is Set (1) or 
Clear (0). 

When combined with CMP, this is the 6502's "IF THEN" construct.

```
LDA $1234  ; Reads the value of address $1234
CMP #$20   ; Compares it with the literal $20 (32)
BEQ Match  ; If they are equal, move to the label "Match".
```

The operand is a _relative_ address, based on the Program Counter at the start
of the next opcode. As a result, you can only branch 127 bytes forward or 128
bytes back. However, most assemblers take a label or an address literal. So
the assembled value will be computed based on the PC and the entered value.

For example, if the PC is $1000, the statement `BCS $1023` will be `$B0 $21`.

+p: Execution takes one additional cycle when moving across a page boundary.


---
[top](#)


### BRK

Break: Software Interrupt


```text
SYNTAX       MODE           HEX  LEN  CYCLES  FLAGS    
BRK          Implied        $00   1     7     ---DB-- 
```

BRK is a software interrupt. With any interrupt several things happen: 

1. The Program Counter is incremented by 2 bytes. 
2. The new PC and flags are pushed onto the stack.
3. The B flag is set.
4. The D (Decimal) flag is cleared, forcing the CPU into binary mode.
5. The CPU reads the address from the NMI vector at $FFFE and jumps there.

On the X16, BRK will jump out of the running program to the machine monitor. 
You can then examine the state of the CPU registers and memory. 

The B flag is used to distinguish a BRK from an NMI. An interrupt triggered by
asserting the NMI pin does not set the B flag, and so the X16 does a warm boot
of BASIC, rather than jumping to MONitor.


---
[top](#)


### CLC

Clear Carry


```text
SYNTAX       MODE           HEX  LEN  CYCLES  FLAGS    
CLC          Implied        $18   1     2     C------ 
```

Clears the Carry flag. This is useful before ADC to prevent an extra 1 during
addition. C is also often used in KERNAL routines to alter the operation of the 
routine or return certain information.


---
[top](#)


### CLD

Clear Decimal Flag


```text
SYNTAX       MODE           HEX  LEN  CYCLES  FLAGS    
CLD          Implied        $D8   1     2     ---D--- 
```

Clears the Decimal flag. This switches the CPU back to binary operation if it
was previously in BCD mode.


---
[top](#)


### CLI

Clear Interrupt Disable


```text
SYNTAX       MODE           HEX  LEN  CYCLES  FLAGS    
CLI          Implied        $58   1     2     --I---- 
```

Clear Interrupt disable. This allows IRQ interrupts to proceed normally. NMI
and RST are always enabled.

Use SEI to disable interrupts


---
[top](#)


### CLV

Clear oVerflow


```text
SYNTAX       MODE           HEX  LEN  CYCLES  FLAGS    
CLV          Implied        $B8   1     2     -----V- 
```

Clear the Overflow (V) flag after an arithmetic operation, such as ADC or SBC.


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
CMP ($12)    ZP Indirect    $D2   2     5     CZ----N +c
```

Compares the value in the Accumulator (A) with the given value. It sets flags
based on subtracting A - _Value_.

- Sets C (Carry) flag if the value in A is >= given value
- Clears C (Carry) flag if the value in A is < given value
- Sets Z (Zero) flag if the values are equal
- Clears Z (Zero) flag if the values are not equal
- Sets N (Negative) flag if value in A is < given value


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

Compares the value in the X register with the given value. It sets flags
based on subtracting X - _Value_.

- Sets C (Carry) flag if the value in X is >= given value
- Clears C (Carry) flag if the value in X is < given value
- Sets Z (Zero) flag if the values are equal
- Clears Z (Zero) flag if the values are not equal
- Sets N (Negative) flag if value in X is < given value

+c new for 65C02


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

Compares the value in the Y register with the given value. It sets flags
based on subtracting Y - _Value_.

- Sets C (Carry) flag if the value in Y is >= given value
- Clears C (Carry) flag if the value in Y is < given value
- Sets Z (Zero) flag if the values are equal
- Clears Z (Zero) flag if the values are not equal
- Sets N (Negative) flag if value in Y is < given value


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

Decrement value by one: this subtracts 1 from memory or the designated register,
leaving the new value in its place.

`DEC` with an operand operates on memory.

`DEX` operates on the X register<br/>
`DEY` operates on the Y register<br/>
`DEC A` or `DEC` operates on the Accumulator. 

- Sets N (Negative) flag if the two's compliment value is negative
- Sets Z (Zero) flag is the value is zero

**Example**

You can peform a 16-bit DEC by chaining two DECs together, testing the low
byte before decrementing the high byte:

```
;16 bit decrement
      LDA Num_Low
      BNE Dec16_1
      DEC Num_High
LABEL DEC Num_Low
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
EOR ($12)    ZP Indirect    $52   2     5     -Z----N +c
```


Perform an exclusive OR of the given value in A 
(the accumulator), storing the result in A.

The exclusive OR version of [ORA](#ora).

- Sets N (Negative) flag if the two's compliment value is negative
- Sets Z (Zero) flag is the value is zero

Exclusive OR returns a 1 bit for each bit that is different in the values 
tested. It returns a 0 for each bit that is the same.

`EOR #$00` has no effect on A, but still sets the Z and N flags.<br/>
`EOR #$FF` inverts the bits in A.<br/>

| M | A | Result |
|---|---|--------|
| 0 | 0 |   0    |
| 0 | 1 |   1    |
| 1 | 0 |   1    |
| 1 | 1 |   0    |

+c new for 65C02


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

Increment by one: this adds 1 to memory or the designated register, leaving the
new value in its place.

- Sets N (Negative) flag if the two's compliment value is negative
- Sets Z (Zero) flag is the value is zero

`INC oper` operates on memory.<br/>
`INX` operates on the X register.<br/>
`INY` operates on the Y register.<br/>
`INC A` or `INC` with no operand operates on the Accumulator.<br/>

**Example**

You can peform a 16-bit INC by chaining two INCs together, testing the low
byte after incrementing it. 

```
;16 bit increment
         INC Addr_Low
         BNE Inc16_1
         INC Addr_High
Inc16_1: ...
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

Jump to specified memory location and begin execution
from this point.

Note for indirect jumps: The CPU does not correctly retrieve the second byte
of the pointer from the next page, so you should never use a pointer address
on the last byte of a page. ie: $12FE.

#### (Absolute,X) and Jump Tables

(Absolute,X) is an addition mode for the 65C02 and is
commonly used for implementing jump tables.

So we might have something like:

```
important_jump_table:
  .word routine1
  .word routine2
...

LDX #$02
JMP (important_jump_table,x)
```

The above would jump to the address of `routine2`, and is much faster than 
the old 6502 method of pushing the two bytes onto the stack and performing an
RTS.


---
[top](#)


### JSR

Jump to Subroutine


```text
SYNTAX       MODE           HEX  LEN  CYCLES  FLAGS    
JSR $1234    Absolute       $20   3     6     ------- 
```

Stores the address of the Program Counter to the stack.<br/>
Jump to specified memory location and begin execution from this point.<br/>

This is used to run subroutines in user programs, as well as running KERNAL
routines. RTS is used at the end of the routine to return to the instruction
immediately after the JSR.

Be careful to always match JSR and RTS, as imbalanced JSR/RTS operations will
either overflow or underflow the stack.


---
[top](#)


### LDA

Read memory to Accumulator


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
LDA ($12)    ZP Indirect    $B2   2     5     -Z----N +c
```

Place the given value from memory into the accumulator (A).

- Sets N (Negative) flag if the two's compliment value is negative
- Sets Z (Zero) flag is the value is zero

+c New for the 65C02<br/>


---
[top](#)


### LDX

Read memory to X Index Register


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


### LDY

Read memory to Y Index Register


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


### LSR

Logical Shift Right


```text
SYNTAX       MODE           HEX  LEN  CYCLES  FLAGS    
LSR A        Accumulator    $4A   1     2     -Z----N 
LSR $12      Zero Page      $46   2     5     -Z----N 
LSR $12,X    Zero Page,X    $56   2     6     -Z----N 
LSR $1234    Absolute       $4E   3     6     -Z----N 
LSR $1234,X  Absolute,X     $5E   3    6/7    -Z----N [^2]
```



---
[top](#)


### NOP

No Operation


```text
SYNTAX       MODE           HEX  LEN  CYCLES  FLAGS    
NOP          Implied        $EA   1     2     ------- 
```

NOP simply does nothing for 2 clock cycles. No registers are affected, and no
memory reads or writes occur. This can be used to delay the clock by 2 ticks.

It's also a useful way to blank out unwanted instructions in memory or in
a machine language program on disk. By changing the byte values of the opcode
and operands to $EA, you can effectively cancel out an instruction.


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
ORA ($12)    ZP Indirect    $12   2     5     -Z----N +c
```

Perform a logical OR of the given value in A 
(the Accumulator), storing the result in A.

See [EOR](#eor) for the exclusive-OR version.

- Sets N (Negative) flag if the two's compliment value is negative
- Sets Z (Zero) flag is the value is zero

+c new for 65C02


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
```



---
[top](#)


### RMBx

Memory Bit Operations


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


### ROL

Rotate Left


```text
SYNTAX       MODE           HEX  LEN  CYCLES  FLAGS    
ROL A        Accumulator    $2A   1     2     CZ----N 
ROL $12      Zero Page      $26   2     5     CZ----N 
ROL $12,X    Zero Page,X    $36   2     6     CZ----N 
ROL $1234    Absolute       $2E   3     6     CZ----N 
ROL $1234,X  Absolute,X     $3E   3    6/7    CZ----N [^2]
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
ROR $1234,X  Absolute,X     $6E   3    6/7    CZ----N [^2]
```



---
[top](#)


### RTI

Return from Interrupt


```text
SYNTAX       MODE           HEX  LEN  CYCLES  FLAGS    
RTI          Implied        $40   1     6     ------- 
```

Return from an interrupt by popping three values off the stack.
The first is for the status register (P) followed by the two bytes of the 
program counter.

Note that unlike [RTS](#rts), the popped address is the actual
return address (rather than address-1).


---
[top](#)


### RTS

Return from Subroutine


```text
SYNTAX       MODE           HEX  LEN  CYCLES  FLAGS    
RTS          Implied        $60   1     6     ------- 
```

Typically used at the end of a subroutine. It jumps 
back to the address after the [JSR](#jsr) that called it
by popping the top 2 bytes off the stack and transferring
control to that address +1.


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
SBC ($12)    ZP Indirect    $F2   2     5     CZ---VN +c
```

Subtract the operand from A and places the result in A.

When Carry is 0, an additional 1 is subtracted.

There is no "Subtract without carry". To do that, use SEC first to set the Carry
flag. 

If D=1, subtraction is Binary Coded Decimal. If D=0 then subtraction is binary.

C is clear when result is less than 0. (ie: Borrow took place)<br/>
Z is set when result is zero<br/>
V is set when signed result goes below -128 or above 127.<br/>
N is set when result is negative (bit 7=1)<br/>

+c new for 65C02


---
[top](#)


### SEC

Set Carry


```text
SYNTAX       MODE           HEX  LEN  CYCLES  FLAGS    
SEC          Implied        $38   1     2     C------ 
```

Sets the Carry flag. This is used before SBC to prevent an extra subtract. C
is also often used in KERNAL routines to alter the operation of the routine
or return certain information.


---
[top](#)


### SED

Set Decimal


```text
SYNTAX       MODE           HEX  LEN  CYCLES  FLAGS    
SED          Implied        $F8   1     2     ---D--- 
```

Sets the Decimal flag. This will put the CPU in BCD mode, which affects the
behavior of ADC and SBC.

In binary mode, adding 1 to $09 will set the Accumulator to $0F.<br/>
In BCD mode, adding 1 to $09 will set the Accumulator to $10.<br/>

Using BCD allows for easier conversion of binary numbers to decimal. BCD also
allows for storing decimal numbers without loss of precision due to power-of-2
rounding.


---
[top](#)


### SEI

Set Interrupt Disable


```text
SYNTAX       MODE           HEX  LEN  CYCLES  FLAGS    
SEI          Implied        $78   1     2     --I---- 
```

Sets or clears the Interrupt Disable flag. When I is set, the CPU will not
execute IRQ interrupts, even if the line is asserted. Use CLI to re-enable
interrupts.


---
[top](#)


### SMBx

Set Memory Bit


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


### STA

Store Accumulator contents to memory


```text
SYNTAX       MODE           HEX  LEN  CYCLES  FLAGS    
STA $12      Zero Page      $85   2     3     ------- 
STA $12,X    Zero Page,X    $95   2     4     ------- 
STA $1234    Absolute       $8D   3     4     ------- 
STA $1234,X  Absolute,X     $9D   3     5     ------- 
STA $1234,Y  Absolute,Y     $99   3     5     ------- 
STA ($12,X)  Indirect,X     $81   2     6     ------- 
STA ($12),Y  Indirect,Y     $91   2     6     ------- 
STA ($12)    ZP Indirect    $92   2     5     ------- +c
```


+c new for 65C02


---
[top](#)


### STP

Stop


```text
SYNTAX       MODE           HEX  LEN  CYCLES  FLAGS    
STP          Implied        $DB   1     3     ------- +c
```

Stops (or halts) the processor and places it in a lower power state until a
hardware reset occurs. For the X16 emulator, when the debugger is enabled 
using the `-debug` command-line parameter, the STP instruction will break into 
the debugger automatically.

If debugging is not enabled, the emulator will prompt the user to close the 
emulator or reset the emulation. 

+c New for the 65C02


---
[top](#)


### STX

Save X Index Register contents to memory


```text
SYNTAX       MODE           HEX  LEN  CYCLES  FLAGS    
STX $12      Zero Page      $86   2     3     ------- 
STX $12,Y    Zero Page,Y    $96   2     4     ------- 
STX $1234    Absolute       $8E   3     4     ------- 
```



---
[top](#)


### STY

Save Y Index Register contents to memory


```text
SYNTAX       MODE           HEX  LEN  CYCLES  FLAGS    
STY $12      Zero Page      $84   2     3     ------- 
STY $12,X    Zero Page,X    $94   2     4     ------- 
STY $1234    Absolute       $8C   3     4     ------- 
```



---
[top](#)


### STZ

Set memory to zero


```text
SYNTAX       MODE           HEX  LEN  CYCLES  FLAGS    
STZ $12      Zero Page      $64   2     3     ------- 
STZ $12,X    Zero Page,X    $74   2     4     ------- 
STZ $1234    Absolute       $9C   3     4     ------- 
STZ $1234,X  Absolute,X     $9E   3     5     ------- 
```



---
[top](#)


### TRB

Test and reset bit


```text
SYNTAX       MODE           HEX  LEN  CYCLES  FLAGS    
TRB $12      Zero Page      $14   2     5     -Z----- 
TRB $1234    Absolute       $1C   3     5     -Z----- 
TRB $12      Zero Page      $04   2     5     -Z----- 
TRB $1234    Absolute       $0C   3     5     -Z----- 
```


---
[top](#)


### Txx

Transfer between registers


```text
SYNTAX       MODE           HEX  LEN  CYCLES  FLAGS    
TAX          Implied        $AA   1     2     -Z----N 
TXA          Implied        $8A   1     2     -Z----N 
TAY          Implied        $A8   1     2     -Z----N 
TYA          Implied        $98   1     2     -Z----N 
TSX          Implied        $BA   1     2     -Z----N 
TXS          Implied        $9A   1     2     ------- 
```



---
[top](#)


### WAI

Wait


```text
SYNTAX       MODE           HEX  LEN  CYCLES  FLAGS    
WAI          Implied        $CB   1     3     ------- +c
```


Effectively stops the processor until a hardware interrupt occurs. The intterupt
is processed immediately, and execution resumes in the Interrupt handler. 

NMI, IRQ, and RST (Reset) will recover from the WAI condition.

Normally, an instruction completes its operation before actually handling an 
interrupt. But if WAI has executed, the CPU does not need to defer the
interrupt, and so the interrupt can be handled immediately.

+c New for the 65C02


---
[top](#)

