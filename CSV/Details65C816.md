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
  LDA Addend1+1  ; Reads the high byte of the addend 
  ADC Addend2+1  ; (the +1 refers to the *address* of Addend, not the value)
  STA Result1+1  ; 
done:
  ; the final result is at Result1
```

Flags:

* **n** is set when the high bit of .A is set. This indicates a negative number
when using Two's Complement signed values.
* **v** (overflow) is set when the sum exceeds the maximum *signed* value for .A.
(More on that below). * **n** is set when the high bit is 1.
* **z** is set when the result is zero. This is useful for loop counters and can be
  tested with BEQ and BNE. (BEQ and BNE test the Zero bit, which is also the
  "equal" bit when performing subtraction or Compare operations.)
* **c** is set when the unsigned result exceeds the register's capacity (255 or
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
Logical AND

Perform a logical AND operation with the operand and .A

AND compares each bit of the operands and sets the result bit to 1 only when the
matching bit of each operand is 1.

Truth table for AND:

```text
Operand 1: 1100
Operand 2: 1010
Result:    1000
```

Flags:

* **n** is set when the high bit of the result is 1
* **z** is set when the result is Zero

AND does not set the overflow or carry flags.

See also: [ORA](#ora), [EOR](#eor)

### ASL
Arithmetic Shift Left

ASL shifts the target left one place. It shifts the high bit of the operand into
the Carry flag and a zero into the low bit.

See also: [LSR](#lsr), [ROL](#rol), [ROR](#ror)

### BCC
Branch on Carry Clear

Jumps to the target address when the Carry flag (**c**) is Zero. This is useful in
multi-byte math, where you will use the Carry flag to decide whether to add or
subtract the higher bytes in a 16 or 32-bit number.

### BCS
Branch on Carry Set

Jumps to the target address when the Carry flag is 1. This is useful in
multi-byte math, where you will use the Carry flag to decide whether to add or
subtract the higher bytes in a 16 or 32-bit number.

A branch operation uses an 8 bit signed value internally, starting from the
instruction after the branch. So the branch destination can be 126 bytes before
or 128 bytes after the branch instruction.

### BEQ
Branch on Equal.

Jumps to the target address when the Zero flag is 1. While this is most commonly
used after a compare (CMP) operation, it's also useful to test if a number is
zero after a Load operation, or to test if a loop is complete after a DEC
operation.

A branch operation uses an 8 bit signed value internally, starting from the
instruction after the branch. So the branch destination can be 126 bytes before
or 128 bytes after the branch instruction.

### BIT
Bit Test

Tests the operand against the Accumulator. The ALU does an AND
operation internally, and The **n**, **v**, and **z** flags are set accordingly.
The Accumulator is *not* modified after the operation.

### BMI
Branch on Minus

Jumps to the specified address when the Negative flag (**n**) is set.

**n** is set when ALU operations result in a negative number, or when the high bit
of an ALU operation is 1.

A branch operation uses an 8 bit signed value internally, starting from the
instruction after the branch. So the branch destination can be 126 bytes before
or 128 bytes after the branch instruction.

### BNE
Branch on Not Equal.

Jumps to the target address when the Zero flag is 0. While this is most commonly
used after a compare (CMP) operation, it's also useful to test if a number is
zero after a Load operation, or to test if a loop is complete after a DEC
operation.

A branch operation uses an 8 bit signed value internally, starting from the
instruction after the branch. So the branch destination can be 126 bytes before
or 128 bytes after the branch instruction.

### BPL
Branch on Plus

Jumps to the specified address when the Negative flag (**n**) is clear.

**n** is clear when ALU operations result in a positive number, or when the high bit
of an ALU operation is 0.

### BRA
Branch Always

Jumps to the specified address.

A branch operation uses an 8 bit signed value internally, starting from the
instruction after the branch. So the branch destination can be 126 bytes before
or 128 bytes after the branch instruction.

### BRK
Break

Perform a break interrupt. The exact behavior changes slightly, based on whether
the CPU is in native or emulation mode. (e is 1 in emulation mode.)

In emulation mode:

1. .PC (Program Counter) is incremented by 2 bytes.
1. .PC is pushed onto the stack.
1. .P (flags) is pushed to the stack.
1. The **b** flag is set.
1. The **d** (Decimal) flag is cleared, forcing the CPU into binary mode.
1. The CPU reads the address from the IRQ vector at $FFFE and jumps there.

In native mode:

1. .PC is incremented by 2 bytes
1. .X (Program Bank) is pushed the stack
1. .PC is pushed to the stack
1. .P (flags) is pushed to the stack
1. The **d** (Decimal) flag is cleared, forcing the CPU into binary mode.
1. The CPU reads the address from the BRK vector at $00FFE6 and jumps there.


See the [Vectors](#vectors) section for the break vector.

### BRL
Branch Long

BRL is a 16 bit _branch_ instruction, meaning assembly creates a relative
address. Unlike BRA and the other branch instructions, BRL uses a 16-bit
address, which allows for an offset of -32768 to 32767 bytes away from the
instruction _following_ The BRL.

Note that when assembling code, you will supply an absolute address to the
assembler. The assembler will subtract the supplied address from the Program
Counter and generate a relative address. This is true for all branch
instructions.

### BVC
Branch on Overflow Clear

Branches to the specified address when the Overflow bit is 0.

### BVS
Branch on Overflow Set

Branches to the specified address when the Overflow bit is 0.

### CLC
Clear Carry

Clears the Carry bit in the flags. You'll usually use CLC before addition and
SEC before subtraction. You'll also want to use CLC or SEC appropriately before
calling certain KERNAL routines that use the **c** bit as an input value.

### CLD
Clear Decimal

Clears the Decimal flag, returning the CPU to 8-bit or 16-bit binary operation.

When Decimal is set, the CPU will store numbers in Binary Coded Decimal format.
Clearing this flag restores the CPU to binary \(base 16\) operation. See
[Decimal Mode](#decimal-mode) for more information.

### CLI
Clear Interrupt Flag

The Interrupt flag (**i**) _stops_ the CPU from servicing IRQ interrupts. When
**i** is set, the CPU will not respond to to the IRQ pin. When **i** is clear,
the CPU will respond to the IRQ pin going low by jumping to the address stored
in the IRQ vector.

See [BRK}(#brk) for more information on interrupt handling.

### CLV
Clear Overflow

Overflow is _set_ when the result of an addition operation goes up through $80
or subtraction goes down through $80.

CLV clears the overflow flag. There is no "SEV" instruction, but overflow can be
set with SEP #$40.

### CMP
Compare

Compares the Accumulator with memory. This sets the **n**, **z**, and **c**
flags as follows:

* A = Operand, **z** is set.
* A < Operand, **n** is set.
* A >= Operand, **c** is set.

You can use teh Branch instructions (BEQ, BNE, BPL, BMI, BCC, BCS) to jump to
different parts of your program based on the results of CMP. Here are some BASIC
comparisons and the equivalent assembly language steps:

```asm65816
; IF A = N THEN 1000
CMP N
BEQ $1000

; IF A <> N THEN 1000
CMP N
BNE $1000

; IF A < N THEN 1000
CMP N
BMI $1000

; IF A >= N THEN 1000
CMP N
BPL $1000

; IF A > N THEN 1000
   CMP N
   BEQ skip
   BCS $1000
skip:

; IF A <= N THEN 1000
  CMP N
  BEQ $1000
  BMI $1000
```

As you can see, a > test and a <= test both require two branches, since **c**
can be set by both equal and greater-than results.

### COP
COP interrupt.

COP is another from of interrupt, which uses a unique vector. The intent
COP is to switch to a Co-Processor, which would be activated by the code at
(FFE4) or (FFF4).

### CPX
Compare X Register

This compares the X register to an operand and sets the flags accordingly.

See [CMP](#cmp) for more information.

### CPY
Compare Y Register

This compares the Y register to an operand and sets the flags accordingly.

See [CMP](#cmp) for more information.

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