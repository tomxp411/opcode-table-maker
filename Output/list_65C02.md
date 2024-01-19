## Opcodes By name

[ADC](#add)
[AND](#logical-and)
[ASL LSR ROL ROR](#bit-shifting)
[BBRx BBSx](#branch-on-bit)
[BCC BCS BEQ BMI BNE BPL BVC BVS BRA](#branch)
[BIT](#test-bit)
[BRK NOP STP WAI](#misc)
[CLC CLD CLI CLV SEC SED SEI](#flags)
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
MODE         SYNTAX      HEX LEN CYCLES FLAGS    
Immediate    ADC #$12    $69  2     2   CZ---VN
Zero Page    ADC $12     $65  2     3   CZ---VN
Zero Page,X  ADC $12,X   $75  2     4   CZ---VN
Absolute     ADC $1234   $6D  3     4   CZ---VN
Absolute,X   ADC $1234,X $7D  3     4   CZ---VN
Absolute,Y   ADC $1234,Y $79  3     4   CZ---VN
Indirect,X   ADC ($12,X) $61  2     6   CZ---VN
Indirect,Y   ADC ($12),Y $71  2     5   CZ---VN
ZP Indirect  ADC ($12)   $72  2     5   CZ---VN
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
MODE         SYNTAX      HEX LEN CYCLES FLAGS    
Immediate    AND #$12    $29  2     2   -Z----N
Zero Page    AND $12     $25  2     3   -Z----N
Zero Page,X  AND $12,X   $35  2     4   -Z----N
Absolute     AND $1234   $2D  3     4   -Z----N
Absolute,X   AND $1234,X $3D  3     4   -Z----N
Absolute,Y   AND $1234,Y $39  3     4   -Z----N
Indirect,X   AND ($12,X) $21  2     6   -Z----N
Indirect,Y   AND ($12),Y $31  2     5   -Z----N
ZP Indirect  AND ($12)   $32  2     5   -Z----N
```


---
[top](#)


### Bit Shifting

```text
MODE         SYNTAX      HEX LEN CYCLES FLAGS    
Accumulator  ASL A       $0A  1     2   CZ----N
Zero Page    ASL $12     $06  2     5   CZ----N
Zero Page,X  ASL $12,X   $16  2     6   CZ----N
Absolute     ASL $1234   $0E  3     6   CZ----N
Absolute,X   ASL $1234,X $1E  3   6/7   CZ----N
Accumulator  LSR A       $4A  1     2   -Z----N
Zero Page    LSR $12     $46  2     5   -Z----N
Zero Page,X  LSR $12,X   $56  2     6   -Z----N
Absolute     LSR $1234   $4E  3     6   -Z----N
Absolute,X   LSR $1234,X $5E  3   6/7   -Z----N
Accumulator  ROL A       $2A  1     2   CZ----N
Zero Page    ROL $12     $26  2     5   CZ----N
Zero Page,X  ROL $12,X   $36  2     6   CZ----N
Absolute     ROL $1234   $2E  3     6   CZ----N
Absolute,X   ROL $1234,X $3E  3   6/7   CZ----N
Accumulator  ROR A       $6A  1     2   CZ----N
Zero Page    ROR $12     $66  2     5   CZ----N
Zero Page,X  ROR $12,X   $76  2     6   CZ----N
Absolute     ROR $1234   $7E  3     6   CZ----N
Absolute,X   ROR $1234,X $6E  3   6/7   CZ----N
```


---
[top](#)


### Branch on Bit

```text
MODE         SYNTAX      HEX LEN CYCLES FLAGS    
ZP Relative  BBR0 $1234  $0F  3     5   -z-----
ZP Relative  BBR1 $1234  $1F  3     5   -z-----
ZP Relative  BBR2 $1234  $2F  3     5   -z-----
ZP Relative  BBR3 $1234  $3F  3     5   -z-----
ZP Relative  BBR4 $1234  $4F  3     5   -z-----
ZP Relative  BBR5 $1234  $5F  3     5   -z-----
ZP Relative  BBR6 $1234  $6F  3     5   -z-----
ZP Relative  BBR7 $1234  $7F  3     5   -z-----
ZP Relative  BBS0 $1234  $8F  3     5   -z-----
ZP Relative  BBS1 $1234  $9F  3     5   -z-----
ZP Relative  BBS2 $1234  $AF  3     5   -z-----
ZP Relative  BBS3 $1234  $BF  3     5   -z-----
ZP Relative  BBS4 $1234  $CF  3     5   -z-----
ZP Relative  BBS5 $1234  $DF  3     5   -z-----
ZP Relative  BBS6 $1234  $EF  3     5   -z-----
ZP Relative  BBS7 $1234  $FF  3     5   -z-----
```


---
[top](#)


### Branch

```text
MODE         SYNTAX      HEX LEN CYCLES FLAGS    
Relative     BCC $1234   $90  2   2/3   -z-----
Relative     BCS $1234   $B0  2   2/3   -z-----
Relative     BEQ $1234   $F0  2   2/3   -z-----
Relative     BMI $1234   $30  2   2/3   -z-----
Relative     BNE $1234   $D0  2   2/3   -z-----
Relative     BPL $1234   $10  2   2/3   -z-----
Relative     BVC $1234   $50  2   2/3   -z-----
Relative     BVS $1234   $70  2   2/3   -z-----
Relative     BRA $1234   $80  2   3/4   -z-----
```


---
[top](#)


### Test Bit

```text
MODE         SYNTAX      HEX LEN CYCLES FLAGS    
Zero Page    BIT $12     $24  2     3   -Z---VN
Absolute     BIT $1234   $2C  3     4   -Z---VN
Immediate    BIT #$12    $89  2     2   -Z-----
Zero Page,X  BIT $12,X   $34  2     4   -Z---VN
Absolute,X   BIT $1234,X $3C  3     4   -Z---VN
```


---
[top](#)


### Misc

```text
MODE         SYNTAX      HEX LEN CYCLES FLAGS    
Implied      BRK         $00  1     7   -z-DB--
Implied      NOP         $EA  1     2   -z-----
Implied      STP         $DB  1     3   -z-----
Implied      WAI         $CB  1     3   -z-----
```


---
[top](#)


### Flags

```text
MODE         SYNTAX      HEX LEN CYCLES FLAGS    
Implied      CLC         $18  1     2   Cz-----
Implied      CLD         $D8  1     2   -z-D---
Implied      CLI         $58  1     2   -zI----
Implied      CLV         $B8  1     2   -z---V-
Implied      SEC         $38  1     2   Cz-----
Implied      SED         $F8  1     2   -z-D---
Implied      SEI         $78  1     2   -zI----
```


---
[top](#)


### Stack

```text
MODE         SYNTAX      HEX LEN CYCLES FLAGS    
Implied      PHA         $48  1     3   -z-----
Implied      PLA         $68  1     4   -Z----N
Implied      PHP         $08  1     3   -z-----
Implied      PLP         $28  1     4   CZIDBVN
Implied      PHX         $DA  1     3   -z-----
Implied      PHY         $5A  1     3   -z-----
Implied      PLX         $FA  1     4   -Z----N
Implied      PLY         $7A  1     4   -Z----N
Implied      RTI         $40  1     6   -z-----
Implied      RTS         $60  1     6   -z-----
```


---
[top](#)


### Transfer

```text
MODE         SYNTAX      HEX LEN CYCLES FLAGS    
Implied      TAX         $AA  1     2   -Z----N
Implied      TXA         $8A  1     2   -Z----N
Implied      TAY         $A8  1     2   -Z----N
Implied      TYA         $98  1     2   -Z----N
Implied      TSX         $BA  1     2   -Z----N
Implied      TXS         $9A  1     2   -z-----
```


---
[top](#)


### Compare

```text
MODE         SYNTAX      HEX LEN CYCLES FLAGS    
Immediate    CMP #$12    $C9  2     2   CZ----N
Zero Page    CMP $12     $C5  2     3   CZ----N
Zero Page,X  CMP $12,X   $D5  2     4   CZ----N
Absolute     CMP $1234   $CD  3     4   CZ----N
Absolute,X   CMP $1234,X $DD  3     4   CZ----N
Absolute,Y   CMP $1234,Y $D9  3     4   CZ----N
Indirect,X   CMP ($12,X) $C1  2     6   CZ----N
Indirect,Y   CMP ($12),Y $D1  2     5   CZ----N
ZP Indirect  CMP ($12)   $D2  2     5   CZ----N
Immediate    CPX #$12    $E0  2     2   CZ----N
Zero Page    CPX $12     $E4  2     3   CZ----N
Absolute     CPX $1234   $EC  3     4   CZ----N
Immediate    CPY #$12    $C0  2     2   CZ----N
Zero Page    CPY $12     $C4  2     3   CZ----N
Absolute     CPY $1234   $CC  3     4   CZ----N
```


---
[top](#)


### Inc/Dec

```text
MODE         SYNTAX      HEX LEN CYCLES FLAGS    
Zero Page    DEC $12     $C6  2     5   -Z----N
Zero Page,X  DEC $12,X   $D6  2     6   -Z----N
Absolute     DEC $1234   $CE  3     6   -Z----N
Absolute,X   DEC $1234,X $DE  3     7   -Z----N
Accumulator  DEC A       $3A  1     2   -Z----N
Implied      DEX         $CA  1     2   -Z----N
Implied      DEY         $88  1     2   -Z----N
Implied      INX         $E8  1     2   -Z----N
Implied      INY         $C8  1     2   -Z----N
Zero Page    INC $12     $E6  2     5   -Z----N
Zero Page,X  INC $12,X   $F6  2     6   -Z----N
Absolute     INC $1234   $EE  3     6   -Z----N
Absolute,X   INC $1234,X $FE  3     7   -Z----N
Accumulator  INC A       $1A  1     2   -Z----N
```


---
[top](#)


### Exclusive OR

```text
MODE         SYNTAX      HEX LEN CYCLES FLAGS    
Immediate    EOR #$12    $49  2     2   -Z----N
Zero Page    EOR $12     $45  2     3   -Z----N
Zero Page,X  EOR $12,X   $55  2     4   -Z----N
Absolute     EOR $1234   $4D  3     4   -Z----N
Absolute,X   EOR $1234,X $5D  3     4   -Z----N
Absolute,Y   EOR $1234,Y $59  3     4   -Z----N
Indirect,X   EOR ($12,X) $41  2     6   -Z----N
Indirect,Y   EOR ($12),Y $51  2     5   -Z----N
ZP Indirect  EOR ($12)   $52  2     5   -Z----N
```


---
[top](#)


### Jump

```text
MODE         SYNTAX      HEX LEN CYCLES FLAGS    
Absolute     JMP $1234   $4C  3     3   -z-----
Indirect     JMP ($1234) $6C  3     5   -z-----
Absolute,X   JMP $1234,X $7C  3     6   -z-----
Absolute     JSR $1234   $20  3     6   -z-----
```


---
[top](#)


### Load

```text
MODE         SYNTAX      HEX LEN CYCLES FLAGS    
Immediate    LDA #$12    $A9  2     2   -Z----N
Zero Page    LDA $12     $A5  2     3   -Z----N
Zero Page,X  LDA $12,X   $B5  2     4   -Z----N
Absolute     LDA $1234   $AD  3     4   -Z----N
Absolute,X   LDA $1234,X $BD  3     4   -Z----N
Absolute,Y   LDA $1234,Y $B9  3     4   -Z----N
Indirect,X   LDA ($12,X) $A1  2     6   -Z----N
Indirect,Y   LDA ($12),Y $B1  2     5   -Z----N
ZP Indirect  LDA ($12)   $B2  2     5   -Z----N
Immediate    LDX #$12    $A2  2     2   -Z----N
Zero Page    LDX $12     $A6  2     3   -Z----N
Zero Page,Y  LDX $12,Y   $B6  2     4   -Z----N
Absolute     LDX $1234   $AE  3     4   -Z----N
Absolute,Y   LDX $1234,Y $BE  3     4   -Z----N
Immediate    LDY #$12    $A0  2     2   -Z----N
Zero Page    LDY $12     $A4  2     3   -Z----N
Zero Page,X  LDY $12,X   $B4  2     4   -Z----N
Absolute     LDY $1234   $AC  3     4   -Z----N
Absolute,X   LDY $1234,X $BC  3     4   -Z----N
```


---
[top](#)


### OR

```text
MODE         SYNTAX      HEX LEN CYCLES FLAGS    
Immediate    ORA #$12    $09  2     2   -Z----N
Zero Page    ORA $12     $05  2     3   -Z----N
Zero Page,X  ORA $12,X   $15  2     4   -Z----N
Absolute     ORA $1234   $0D  3     4   -Z----N
Absolute,X   ORA $1234,X $1D  3     4   -Z----N
Absolute,Y   ORA $1234,Y $19  3     4   -Z----N
Indirect,X   ORA ($12,X) $01  2     6   -Z----N
Indirect,Y   ORA ($12),Y $11  2     5   -Z----N
ZP Indirect  ORA ($12)   $12  2     5   -Z----N
```


---
[top](#)


### RMB

```text
MODE         SYNTAX      HEX LEN CYCLES FLAGS    
Zero Page    RMB0 $12    $07  2     5   -z-----
Zero Page    RMB1 $12    $17  2     5   -z-----
Zero Page    RMB2 $12    $27  2     5   -z-----
Zero Page    RMB3 $12    $37  2     5   -z-----
Zero Page    RMB4 $12    $47  2     5   -z-----
Zero Page    RMB5 $12    $57  2     5   -z-----
Zero Page    RMB6 $12    $67  2     5   -z-----
Zero Page    RMB7 $12    $77  2     5   -z-----
```


---
[top](#)


### SMB

```text
MODE         SYNTAX      HEX LEN CYCLES FLAGS    
Zero Page    SMB0 $12    $87  2     5   -z-----
Zero Page    SMB1 $12    $97  2     5   -z-----
Zero Page    SMB2 $12    $A7  2     5   -z-----
Zero Page    SMB3 $12    $B7  2     5   -z-----
Zero Page    SMB4 $12    $C7  2     5   -z-----
Zero Page    SMB5 $12    $D7  2     5   -z-----
Zero Page    SMB6 $12    $E7  2     5   -z-----
Zero Page    SMB7 $12    $F7  2     5   -z-----
```


---
[top](#)


### Subtract

```text
MODE         SYNTAX      HEX LEN CYCLES FLAGS    
Immediate    SBC #$12    $E9  2     2   CZ---VN
Zero Page    SBC $12     $E5  2     3   CZ---VN
Zero Page,X  SBC $12,X   $F5  2     4   CZ---VN
Absolute     SBC $1234   $ED  3     4   CZ---VN
Absolute,X   SBC $1234,X $FD  3     4   CZ---VN
Absolute,Y   SBC $1234,Y $F9  3     4   CZ---VN
Indirect,X   SBC ($12,X) $E1  2     6   CZ---VN
Indirect,Y   SBC ($12),Y $F1  2     5   CZ---VN
ZP Indirect  SBC ($12)   $F2  2     5   CZ---VN
```


---
[top](#)


### Store

```text
MODE         SYNTAX      HEX LEN CYCLES FLAGS    
Zero Page    STA $12     $85  2     3   -z-----
Zero Page,X  STA $12,X   $95  2     4   -z-----
Absolute     STA $1234   $8D  3     4   -z-----
Absolute,X   STA $1234,X $9D  3     5   -z-----
Absolute,Y   STA $1234,Y $99  3     5   -z-----
Indirect,X   STA ($12,X) $81  2     6   -z-----
Indirect,Y   STA ($12),Y $91  2     6   -z-----
ZP Indirect  STA ($12)   $92  2     5   -z-----
Zero Page    STX $12     $86  2     3   -z-----
Zero Page,Y  STX $12,Y   $96  2     4   -z-----
Absolute     STX $1234   $8E  3     4   -z-----
Zero Page    STY $12     $84  2     3   -z-----
Zero Page,X  STY $12,X   $94  2     4   -z-----
Absolute     STY $1234   $8C  3     4   -z-----
Zero Page    STZ $12     $64  2     3   -z-----
Zero Page,X  STZ $12,X   $74  2     4   -z-----
Absolute     STZ $1234   $9C  3     4   -z-----
Absolute,X   STZ $1234,X $9E  3     5   -z-----
```


---
[top](#)


### Test Reset Bit

```text
MODE         SYNTAX      HEX LEN CYCLES FLAGS    
Zero Page    TRB $12     $14  2     5   -Z-----
Absolute     TRB $1234   $1C  3     5   -Z-----
Zero Page    TRB $12     $04  2     5   -Z-----
Absolute     TRB $1234   $0C  3     5   -Z-----
```


---
[top](#)

