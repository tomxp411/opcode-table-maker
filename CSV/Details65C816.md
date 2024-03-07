### ADC
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

### AND
### ASL
### BCC
### BCS
### BEQ
### BIT
### BMI
### BNE
### BPL
### BRA
### BRK
### BRL
### BVC
### BVS
### CLC
### CLD
### CLI
### CLV
### CMP
### COP
### CPX
### CPY
### DEC
### DEX
### DEY
### EOR
### INC
### INX
### INY
### JMP
### JSL
### JSR
### LDA
### LDX
### LDY
### LSR
### MVN
### MVP
### NOP
### ORA
### PEA
### PEI
### PER
### PHA
### PHB
### PHD
### PHK
### PHP
### PHX
### PHY
### PLA
### PLB
### PLD
### PLP
### PLX
### PLY
### REP
### ROL
### ROR
### RTI
### RTL
### RTS
### SBC
### SEC
### SED
### SEI
### SEP
### STA
### STP
### STX
### STY
### STZ
### TAX
### TAY
### TCD
### TCS
### TDC
### TRB
### TSB
### TSC
### TSX
### TXA
### TXS
### TXY
### TYA
### TYX
### WAI
### WDM
### XBA
### XCE