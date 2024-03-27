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
Boolean AND

Perform a logical AND operation with the operand and .A

AND compares each bit of the operands and sets the result bit to 1 only when the
matching bit of each operand is 1.

AND is useful for reading a group of bits from a byte. For example, `AND #$0F`
will clear the top nibble of .A, returning the bits from the lower nibble.

Truth table for AND:

```text
Operand 1: 1100
Operand 2: 1010
Result:    1000
```

Flags:

* **n** is set when the high bit of the result is 1
* **z** is set when the result is Zero

See also: [ORA](#ora), [EOR](#eor)

### ASL
Arithmetic Shift Left

ASL shifts the target left one place. It shifts the high bit of the operand into
the Carry flag and a zero into the low bit.

See also: [LSR](#lsr), [ROL](#rol), [ROR](#ror)

### BCC
Branch on Carry Clear

Jumps to the target address when the Carry flag (**c**) is Zero.

BCC can be used after add, subtract, or compare operations. After a compare,
**c** is as follows:

* When A < Operand, **c** is clear.
* When A >= Operand, **c** is set.

A branch operation uses an 8 bit signed value internally, starting from the
instruction after the branch. So the branch destination can be 126 bytes before
or 128 bytes after the branch instruction.

### BCS
Branch on Carry Set

Jumps to the target address when the Carry flag is 1. 

BCC can be used after add, subtract, or compare operations. After a compare,
**c** is as follows:

* When A < Operand, **c** is clear.
* When A >= Operand, **c** is set.

A branch operation uses an 8 bit signed value internally, starting from the
instruction after the branch. So the branch destination can be 126 bytes before
or 128 bytes after the branch instruction.

### BEQ
Branch on Equal.

Jumps to the target address when the Zero flag is 1. While this is most commonly
used after a compare (see [CMP](#cmp) ) operation, it's also useful to test if a
number is zero after a Load operation, or to test if a loop is complete after a
DEC operation.

A branch operation uses an 8 bit signed value internally, starting from the
instruction after the branch. So the branch destination can be 126 bytes before
or 128 bytes after the branch instruction.

### BIT
Bit Test

Tests the operand against the Accumulator. The ALU does an AND
operation internally, setting **z** if the result is 0. 

When **m**=1, **n** and **v** are set based on the value of bits 7 and 6 in
memory.

When **m**=0, **n** and **v** are set based on the value of bits 15 and 14 in
memory.

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

A branch operation uses an 8 bit signed value internally, starting from the
instruction after the branch. So the branch destination can be 126 bytes before
or 128 bytes after the branch instruction.

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

Since the Program Counter is incremented 

In emulation mode:

1. .PC (Program Counter) is incremented by 1 byte.
1. If the CPU is in Native mode, the Program Bank is pushed to the stack.
1. .PC is pushed onto the stack.
1. .P (flags) is pushed to the stack. (the **b** bit, bit 4, is set to 1.)
1. The **d** (Decimal) flag is cleared, forcing the CPU into binary mode.
1. The CPU reads the address from the IRQ vector at $FFFE and jumps there.

An IRQ is similar, except that IRQ clears bit 4 (**b**) during the push to the
stack. So an Interrupt Service Routine can read the last byte on the stack to
determine whether an emulation-mode interrupt is a BRK or IRQ.

On the X16, the IRQ services the keyboard, mouse, game pads, updates the clock,
blinks the cursor, and updates the LEDs.

In native mode:

1. .PC is incremented by 1 byte.
1. .X (Program Bank) is pushed the stack
1. .PC is pushed to the stack
1. .P (flags) is pushed to the stack
1. The **d** (Decimal) flag is cleared, forcing the CPU into binary mode.
1. The CPU reads the address from the BRK vector at $00FFE6 and jumps there.

Since the Native Mode has a distinct BRK vector, you do not need to query the
stack to dispatch a BRK vs IRQ interrupt. You can just handle each immediately.

The RTI instruction is used to return from an interrupt. It pulls the values
back off the stack (this varies, depending on the CPU mode) and returns to the
pushed PC address.

RTI 

See the [Vectors](#vectors) section for the break vector.

### BRL
Branch Long

BRL is a 16 bit _branch_ instruction, meaning assembly creates a relative
address. Unlike BRA and the other branch instructions, BRL uses a 16-bit
address, which allows for an offset of -32768 to 32767 bytes away from the
instruction _following_ The BRL.

Of course, due to wrapping of the 64K bank, this means that the entire 64K
region is accessible. Values below 0 will simply wrap around and start from
$FFFF, and values above $FFFF will wrap around to 0.

Since this is a _relatve_ branch, that means code assembled with BRL, instead of
JMP, can be moved around in memory without the need for re-assembly.

### BVC
Branch on Overflow Clear

Branches to the specified address when the Overflow bit is 0.

A branch operation uses an 8 bit signed value internally, starting from the
instruction after the branch. So the branch destination can be 126 bytes before
or 128 bytes after the branch instruction.

### BVS
Branch on Overflow Set

Branches to the specified address when the Overflow bit is 1.

A branch operation uses an 8 bit signed value internally, starting from the
instruction after the branch. So the branch destination can be 126 bytes before
or 128 bytes after the branch instruction.

### CLC
Clear Carry

Clears the Carry bit in the flags. You'll usually use CLC before addition and
SEC before subtraction. You'll also want to use CLC or SEC appropriately before
calling certain KERNAL routines that use the **c** bit as an input value.

### CLD
Clear Decimal

Clears the Decimal flag, returning the CPU to 8-bit or 16-bit binary operation.

When Decimal is set, the CPU will store numbers in Binary Coded Decimal format.
Clearing this flag restores the CPU to binary operation. See
[Decimal Mode](#decimal-mode) for more information.

### CLI
Clear Interrupt Flag

Clears the **i** flag, _allowing interrupts to be handled_. 

The **i** flag operates somewhat non-intuitively: when **i** is set (1), IRQ is
suppressed. When **i** is clear (0), interrupts are handled. So CLI _allows_
interrupts to be handled.

See [BRK}(#brk) for more information on interrupt handling.

### CLV
Clear Overflow

Overflow is _set_ when the result of an addition operation goes up through $80
or subtraction goes down through $80.

CLV clears the overflow flag. There is no "SEV" instruction, but overflow can be
set with SEP #$40.

### CMP
Compare

Compares the Accumulator with memory. This performs a subtract operation
between .A and the operand and sets the **n**, **z**, and **c** flags based on
the result. The Accumulator is not altered.

* WHen A = Operand, **z** is set.
* When A < Operand, **c** is clear.
* When A <> Operand, **z** is clear.
* When A >= Operand, **c** is set.

You can use the Branch instructions (BEQ, BNE, BPL, BMI, BCC, BCS) to jump to
different parts of your program based on the results of CMP. Here are some BASIC
comparisons and the equivalent assembly language steps.

```asm65816
; IF A = N THEN 1000
  CMP N
  BEQ $1000

; IF A <> N THEN 1000
  CMP N
  BNE $1000

; IF A < N THEN 1000
  CMP N
  BCC $1000

; IF A >= N THEN 1000
  CMP N
  BCS $1000

; IF A > N THEN 1000
  CMP N
  BEQ skip
  BCS $1000
skip:

; IF A <= N THEN 1000
  CMP N
  BEQ $1000
  BCC $1000
```

As you can see, some comparisons will require two distinct branch instructions.

Also, note that the Branch instructions (except BRL) require that the target
address be within 128 bytes of the instruciton after the branch. If you need to
branch further, the usual method is to invert the branch instruction and use a
JMP to take the branch.

For example, the following two branches behave the same, but the second one can
jump to any address on the computer, whereas the first can only jump -128/+127
bytes away:

```asm65816
short_branch:
  CMP N
  BEQ target 

longer_branch:
  CMP N
  BNE skip
  JMP target
skip:
```

### COP
COP interrupt.

COP is similar to BRK, but uses the FFE4 or FFF4 vectors. The intent is to COP
is to switch to a Co-Processor, but this can be used for any purpose on the X16
(including triggering a DMA controller, if that's what you want to do.)

### CPX
Compare X Register

This compares the X register to an operand and sets the flags accordingly.

See [CMP](#cmp) for more information.

### CPY
Compare Y Register

This compares the Y register to an operand and sets the flags accordingly.

See [CMP](#cmp) for more information.

### DEC
Decrement

Decrement .A or memory. The **z** flag is set when the value reaches zero. This
makes DEC, DEX, and DEY useful as a loop counter, by setting the number of
iterations, the repeated operation, then DEX followed by BNE.

**z** is set when the counter reaches zero.
**n** is set when the high bit gets set.

### DEX
Decrement .X

Decrement .X The **z** flag is set when the value reaches zero. This
makes DEC, DEX, and DEY useful as a loop counter, by setting the number of
iterations, the repeated operation, then DEX followed by BNE.

**z** is set when the counter reaches zero.
**n** is set when the high bit gets set.

### DEY
Decrement .Y

Decrement .X The **z** flag is set when the value reaches zero. This
makes DEC, DEX, and DEY useful as a loop counter, by setting the number of
iterations, the repeated operation, then DEX followed by BNE.

**z** is set when the counter reaches zero.
**n** is set when the high bit gets set.

### EOR
Exclusive OR

Perform an Exclusive OR operation with the operand and .A

EOR compares each bit of the operands and sets the result bit to 1 if one of the
two bits is 1. If both bits are 1, the result is 0. If both bits are 0, the
result is 0.

EOR is useful for _inverting_ the bits in a byte. `EOR #$FF` will flip an entire
byte. (This will always flip the low byte in .A. To flip both bytes when **m**
is 0, you would use `EOR #$FFFF`.)

Truth table for EOR:

```text
Operand 1: 1100
Operand 2: 1010
Result:    0110
```

### INC
Increment

Increment .A or memory

Adds 1 to the value in .A or the specified memory address. The **n** and **z**
flags are set, based on the resultant value.

INC is useful for reading strings and operating on large areas of memory,
especially with indirect and indexed addressing modes.

### INX
Increment .X

Increment the X register.

The following routine prints a null-terminated string (**a** should be 1.)

```asm65816
  LDX #$0
loop:
  LDA string_addr, X
  BEQ done
  JSR CHROUT
  INX
  BRA loop
done:
```

See [INC}(#inc)

### INY
Increment .Y

Increment the Y register.

See [INC}(#inc)

### JMP
Jump

Jump to a differnent address in memory, continuing program execution at the
specified address.

Instructions like `JMP ($1234,X)` make it possible to branch to a selectable
subroutine by setting X to the indesx into the vector table.

### JML
Jump Long

Jump to a differnent address in memory, continuing program execution at the
specified address. JML accepts a 24-bit address, allowing the program to change
program banks.

### JSL
Jmp to Subroutine Long

This is a 24-bit instruction, which can jump to a subroutine located in another
program bank.

Use the [RTL](#rtl) instruction to return to the instruction following the JSL.

### JSR
Jump to Subroutine

Jumps to a new operating address in memory. Also pushes the return address to
the stack, allowing an RTS insruction to pick up at the address following the
JSR.

The [RTS](#rts) instruction returns to the instruction following JSR.

The actual address pushed to the stack is the _before_ the next instruction.
This means that the CPU still needs to increment the PC by 1 step during the
RTS.

### LDA
Load Accumulator

Reads a value from memory into .A. This sets **n** and **z** appropriately,
allowing you to use BMI, BPL, BEQ, and BNE to act based on the value being read.

### LDX
Load X Register

Read a value into .X. This sets **n** and **z** appropriately, allowing you to
use BMI, BPL, BEQ, and BNE to act based on the value being read.

### LDY
Load X Register

Read a value into .Y. This sets **n** and **z** appropriately, allowing you to
use BMI, BPL, BEQ, and BNE to act based on the value being read.

### LSR
Logical Shift Right

Shifts all bits to the right by one position.

Bit 0 is shifted into Carry.;
0 shifted into the high bit (7 or 15, depending on the **m** flag.)

**Similar instructions:**;
[ASL](#asl) is the opposite instruction, shifting to the left.;
[ROR](#ror) rotates bit 0 through Carry to bit 7.;

+p Adds a cycle if ,X crosses a page boundary.;
+c New for the 65C02;

### MVN
Block Copy/Move Negative

This performs a block copy. Use MVN when the source and destination ranges
overlap and dest < source.

Copying anything other than page zero requires 16-bit index registers, so it's
wise to clear **m** and **x** with `REP #$30`. 

* Set .X to the source address
* Set .Y to the destination address
* Set .A to size-1
* MVN #source_bank, #dest_bank

### MVP
Block Copy/Move Positive

This performs a block copy. Use MVP when the source and destination ranges
overlap and dest > source.

Copying anything other than page zero requires 16-bit index registers, so it's
wise to clear **m** and **x** with `REP #$30`. 

* Set .X to the source_address + size - 1
* Set .Y to the destination_address
* Set .A to size-1
* MVP #source_bank, #dest_bank

### NOP
No Operation

The CPU performs no operation. This is useful when blocking out instructions, or
reserving space for later use. 

### ORA
Boolean OR

Perform a Boolean OR operation with the operand and .A

ORA compares each bit of the operands and sets the result bit to 1 if either or
both of the two bits is 1. If both bits are 0, the result is 0.

ORA is useful for *setting* a specific bit in a byte.

Truth table for ORA:

```text
Operand 1: 1100
Operand 2: 1010
Result:    1110
```

### PEA
Push Absolute

PEA, PEI, and PER push values to the stack *without* affecting registers.

PEA pushes the operand value onto the stack. The literal operand is used, rather
than an address. 

This seems inconsistent with the absolute address syntax, as PEA and PEI follow
their own syntax rules. 

### PEI
Push Effecive Indirect Address

PEI takes a _pointer_ as an operand. The value written to the stack is the two
bytes at the supplied address.

Example:
```
; data at $20 is $1234
PEI ($20)
; pushes $1234 onto the stack.
```

The written form of PEI is inconsistent with the usual indirect mode syntax, as
PEI and PEA follow their own syntax rules.

### PER
Push Effective PC Relative Indirect Address

PER pushes the address _relative to the program counter_. This allows you to
mark the current executing location and push that to the stack.

When used in conjunctin with BRL, PER can form a reloatable JSR instruction. 

Consider the following ca65 macro:

```asm65816
.macro bsr addr
   per .loword(:+ - 1)
   brl addr
   :
.endmacro
```

This gets the address following the BRL instruction and pushes that to the
stack. See [JSR](#jsr) to understand why the -1 is required.

### PHA
Push Accumulator

Pushes the Accumulator to the stack. This will push 1 byte when **m** is 1 and
two bytes when **m** is 0 (16-bit memory/.A mode.)

An 8-bit stack push writes data at the Stack Pointer address, then moves SP down
by 1 byte. 

A 16-bit push writes the high byte first, decrements the PC, then writes the low
byte, and decrements the PC again.

In Emulation mode, the Stack Pointer will always be an address in the $100-$1FF
range, so there is only room for 256 bytes on the stack. In native mode, the
stack can be anywhere in the first 64KB of RAM.

### PHB
Push Data Bank register.

The data bank register sets the top 8 bits used when reading data with LDA, LDX,
and LDY.

This is always an 8-bit operation.

### PHD
Push Direct Page

Pushes the 16-bit Direct Page register to the stack. This is useful for
preserving the location of .D before relocating Direct Page for another use
(such as an operating system routine.)

### PHK
Push Program Bank

Pushes the Program Bank register to the stack. The Program Bank is the top 8
bits of the 24-bit Program Counter address.

### PHP
Push Program Status (Flags)

The CPU writes the flags in the order `nvmx dizc`. (**e** does
not get written to the stack.)

Note: the 6502 and 65C02 use bit 4 (**x** on the '816) for the Break flag. While
**b** does get written to the stack in a BRK operation, bit 4 in .P always
reflects the state of the 8-bit-index flag. Since the flags differ slightly in
behavior, make sure your Interrupt handler code reads from the stack, not the .P
bits, when dispatching a IRQ/BRK interrupt.

### PHX
Push X Register

Pushes the X register to the stack. This will push 1 byte when **x** is 1 and
two bytes when **x** is 0 (16-bit index mode.)

An 8-bit stack push writes data at the Stack Pointer address, then moves SP down
by 1 byte. A 16-bit stack push moves the stack pointer down 2 bytes.

### PHY
Push Y Register

Pushes the Y register to the stack. This will push 1 byte when **y** is 1 and
two bytes when **y** is 0 (16-bit index mode.)

An 8-bit stack push writes data at the Stack Pointer address, then moves SP down
by 1 byte. A 16-bit stack push moves the stack pointer down 2 bytes.

### PLA
Pull Accumulator

Pulls the Accumulator from the stack.

In the opposite of PHA, the PLA instruction reads the current value from the
stack and _increments_ the stack pointer by 1 or 2 bytes.

The number of bytes read is based on the value of the **m** flag.

### PLB
Pull Data Bank Register

Pull the Data Bank register from the stack.

In the opposite of PHB, the PLB instruction reads the current value from the
stack and _increments_ the stack pointer by 1 byte.

### PLD
Pull Direct Page Register

This pulls a word from the stack and loads it into the Direct Page register. 

That value can be placed on the stack in several ways, such as PHA, PHX, or PEA.

### PLP
Pull Prgram Status Byte (flags)

This reads the flags back from the stack. Since the flags affect the state of
the **m** and **x** register-width flags, this should be performed *before* a
PLA, PLX, or PLY operation.

### PLX
Pull X Register

Pulls the X Register from the stack.

In the opposite of PHX, the PLX instruction reads the current value from the
stack and _increments_ the stack pointer by 1 or 2 bytes.

The number of bytes read is based on the value of the **x** flag.

### PLY
Pull Y Register

Pulls the Y Register from the stack.

In the opposite of PHY, the PLY instruction reads the current value from the
stack and _increments_ the stack pointer by 1 or 2 bytes.

The number of bytes read is based on the value of the **x** flag.

### REP
Reset Program Status Bit

This clears (to 0) flags in the Program Status Byte. The 1 bits in the will be
cleared in the flags, so REP #$30 will set the **a** and **x** bits low.

### ROL
Rotate Left

Shifts bits in the accumulator or memory left one bit. The Carry bit (**c**) is
shifted into bit 0. The high bit (7 or 15) is shifted into **c**.

### ROR
Rotate Right

Shifts bits in the accumulator or memory right one bit. The Carry bit (**c**) is
shifted into the high bit (15 or 7). The low bit (0) is shifted into **c**.

### RTI
Return From Interrupt

This returns control to the executing program. The following steps happen, in
order:

1. The CPU pulls the flags from the stack (including **m** and **x**, which
   switch to 8/16 bit mode, as appropriate.
2. The CPU pulls the Program Counter from the stack.
3. If the CPU is in native mode, the CPU pulls the Program Bank register.

### RTL
Return From Subroutine Long

This returns to the caller at the end of a subroutine. This should be used to
return to the instruction following a [JSL](#jsl) instruction.

This reads 3 bytes from the stack and loads them into the Program Counter and
Program Bank register. The next instruction executed will then be the
instruction after the JSL that jumped to the subroutine.

### RTS
Return From Subroutine

Return to to a calling routine after a [JSR](#jsr).

RTS reads a 2 byte address from the stack and loads that address into the
Program Counter. The next instruction executed will then be the
instruction after the JSR that jumped to the subroutine.

### SBC
Subtract With Carry

Subtract a value from .A. The result is left in .A.

When performing subtraction, the Carry bit indicates a Borrow and operates in
reverse from addition: when **c** is 0, SBC subtracts one from the final result,
to account for the borrow.

After the operation, **c** will be set to 0 if a borrow took place and 1 if it
did not.

When **m** is 0, this will be a 16 bit add, and the CPU will read two bytes from
memory.

Since there is no "subtract with no carry", you should always use SEC before the
first SBC in a sequence, to ensure that the Carry bit is _set_, going into a
subtraction.

### SEC
Set Carry

Sets the Carry bit to 1

### SED
Set Decimal

Sets the Decimal bit to 1, setting the CPU to BCD mode.

When Decimal is set, the CPU will store numbers in Binary Coded Decimal format.
Clearing this flag restores the CPU to binary operation. See
[Decimal Mode](#decimal-mode) for more information.

In binary mode, adding 1 to $09 will set the Accumulator to $0A. In BCD mode,
adding 1 to $09 will set the Accumulator to $10.

Using BCD allows for easier conversion of binary numbers to decimal. BCD also
allows for storing decimal numbers without loss of precision due to power-of-2
rounding.

An add or subtract (ADC or SBC) is required to actually trigger BCD conversion.
So if you have a number like $1A on the accumulator and you SED, you can convert
.A to $20 with the instruction `ADC #$00`.

### SEI
Set IRQ Disable

Sets **i**, which inhibits IRQ handling. When **i** is set, the CPU will not
respond to the IRQ pin. When **i** is clear, the CPU will perform an interrupt
when the IRQ pin is asserted.

The **i** flag operates somewhat non-intuitively: when **i** is set (1), IRQ is
suppressed. When **i** is clear (0), interrupts are handled. So CLI _allows_
interrupts to be handled and SEI _blocks_ interrupt handling.

See [BRK](#brk) for a brief description of interrupts.

### SEP
Set Processor Status Bit

Reset Program Status Bit

This sets (to 1) a flag in the Program Status Byte. The operand value will be
loaded into the flags, so SEP #$30 will set the **a** and **x** bits high.

### STA
Store Accumulator to Memory

Stores the value in .A to a memory address.

When **m** is 0, the value saved will be a 16-bit number, using two bytes of
memory. When **m** is 1, the value will be an 8-bit number, using one byte of
RAM.

### STP
Stop the Clock

Halts the CPU. The CPU will no longer process instructions until the Reset pin
is asserted.

### STX
Store Index X to Memory

Stores the value in .X to a memory address.

When the flag **x** is 0, the value saved will be a 16-bit number, using two
bytes of memory. When **x** is 1, the value will be an 8-bit number, using one
byte of RAM.

### STY
Store Index Y to Memory

Stores the value in .Y to a memory address.

When the flag **x** is 0, the value saved will be a 16-bit number, using two
bytes of memory. When **x** is 1, the value will be an 8-bit number, using one
byte of RAM.

### STZ
Store Sero to Memory

Stores a zero to a memory address.

When **m** is 0, the value saved will be a 16-bit number, using two bytes of
memory. When **m** is 1, the value will be an 8-bit number, using one byte of
RAM.

### TAX
Transfer Accumulator to Index X

Copies the contents of .A to .X. 

### TAY
Transfer Accumulator to Index Y

Copies the contents of .A to .Y.

### TCD
Transfer C Accumulator to Direct Register

This copies the 16-bit value from the 16-bit Accumulator to the Direct Register,
allowing you to relocate Direct Page anywhere in the first 64K of RAM.

This is one of the times that the 16-bit Accumulator is called .C, as it always
operates on a 16-bit value, regardless of the state of the **m** flag.

### TCS
Transfer C Accumulator to Stack Pointer

This copies the 16-bit value from the 16-bit Accumulator to the Stack Pointer,
allowing you to relocate the stack anywhere in the first 64K of RAM.

This is one of the times that the 16-bit Accumulator is called .C, as it always
operates on a 16-bit value, regardless of the state of the **m** flag.

### TDC
Transfer Direct Register to C Accumulator

Copies the value of the Direct Register to the Accumulator.

This is one of the times that the 16-bit Accumulator is called .C, as it always
operates on a 16-bit value, regardless of the state of the **m** flag.

### TRB
Test and Reset Bit

TRB does two things with one operation: it tests specified bits in a memory
location, and it clears (resets) those bits after the test.

First, TRB performs a logical AND between the memory address specified and the
Accmulator. If the result of the AND is zero, the **z** flag will be set. 

Second, TRB clears bits in the memory value based on the bit mask in the
accmulator. Any bit that is 1 in .A will be changed to 0 in memory.

So to _clear_ a bit in a memory value, set that value to 1 in .A, like this:

```
; memory at $2000 contains $84
LDA #$80
TRB $2000
; memory at $2000 now contains $04, and z flag is clear

; memory at $1234 contains $20
LDA #$01
TRB $1234
; memory at $1234 contains $20 and z flag is set
; because $20 AND $01 == 0.
```

### TSB
Test and Set Bit

TSB does two things with one operation: it tests specified bits in a memory
location, and it clears (resets) those bits after the test.

First, TSB performs a logical AND between the memory address specified and the
Accmulator. If the result of the AND is zero, the **z** flag will be set. 

TSB also _sets_ the bits that are 1 in the accumulator, similar to an OR
operation.

### TSC
Transfer Stack Pointer to C accumulator

Copies the Stack Pointer to the 16-bit Accumulator.

This is one of the times that the 16-bit Accumulator is called .C, as it always
operates on a 16-bit value, regardless of the state of the **m** flag.

### TSX
Transfer Stack Pointer X Register

Copies the Stack Pointer to the X register.

### TXA
Transfer X Register to Accumulator

Copies the value in .X to .A

### TXS
Transfer X Register to Stack Pointer

Copies the X register to the Stack Pointer. This is used to reset the stack to a
known location, usually at boot or when context-switching.

### TXY
Transfer X Register to Accumulator

Copies the value in .X to .Y

### TYA
Transfer Y Register to Accumulator

Copies the value in .Y to .A

### TYX
Transfer Y Register to X Register

Copies the value in .Y to .X

### WAI
Wait For Interrupt

Stops the CPU until the next interrupt is triggered. This allows the CPU to
respond to an interrupt immediately, rather than waiting for an instruction to
complete.

### WDM
WDM

WDM is a 2 byte NOP: the WDM opcode and the operand byte following are both
read, but not executed.

The WDM opcode is reserved for future use and should be avoided in 65C816
programs.

### XBA
Exchange B and A Accumulator

Swaps the values in .A and .B. This exchanges the high and low bytes of the
Accumulator. XBA functions the same in both 8 and 16 bit modes.

### XCE
Exchange Carry and Emulation Flags

This allows the CPU to switch between Native and Emulation modes. 

To switch into native mode: 

```asm65816
CLC
XCE
```

To switch to 65C02 emulation mode:

```asm65816
SEC
XCE
```
