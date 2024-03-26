
# Appendix F: The 65C816 Processor

**Table of Contents**

1. [Overview](#overview)
2. [Compatibility with the 65C02](#compatibility-with-the-65c02)
3. [Registers](#registers)
4. [Status Flags](#status-flags)
5. [16 bit mode](#16-bit-mode)
6. [Address Modes](#address-modes)
7. [Vectors](#vectors)
8. [Instruction Tables](#instruction-tables)

## Overview

This document is a brief introduction and quick reference for the 65C816
Microprocessor. For more details, see the [65C816 data
sheet](https://www.westerndesigncenter.com/wdc/documentation/w65c816s.pdf) or
[Programming the 65816: Including the 6502, 65C02, and 65802](https://www.amazon.com/Programming-65816-Including-65C02-65802-ebook/dp/B01855HL7Q).

The WDC65C816 CPU is an 8/16 bit CPU and a follow-up to the 65C02 processor. The
familiar 65C02 instructions and address modes are retained, and some new ones
are added.

The CPU can optionally operate in 16-bit mode, extending the utility of math
instruction (16-bit adds!) and the coverage of .X and .Y indexed modes to 64KB.

Zero Page has been renamed to Direct Page, and Direct Page can now be relocated
anywhere in the first 64K of RAM. As a result, all of the Zero Page instructions
are now "Direct" instructions and can operate anywhere in the X16's address
range.

Likewise, the Stack can also be relocated, and the stack pointer is now 16 bits.
This allows for a much larger stack, and the combination of stack and DP
relocation offer interesting multitasking opportunities.

## Compatibility with the 65C02

The 65C916 CPU is generally compatible with the 65C02 instruction set, with the
exception  of the `BBRx`, `BBSx`, `RMBx`, and `SMBx` instructions. We recommend
programmers avoid these instructions when writing X16 softwware, using the more
conventional Boolean logic instructions, instead.

## Registers

| Notation  | Name             | Description     |
|-----------|------------------|-----------------|
| A         | Accumulator      | The accumulator. It stores the result of moth math and logical operations.  |
| X         | X Index          | .X is mostly used as a counter and to offset addresses with X indexed modes |
| Y         | Y Index          | .Y is mostly used as a counter and to offset addresses with Y indexed modes |
| S         | Stack Pointer    | SP points to the next open position on the stack.                           |
| DB or DBR | Data Bank        | Data bank is the default bank for operations that use a 16 bit address.     |
| K or  PBR | Program Bank     | The default address for 16 bit JMP and JSR oprerations. Can only be set with a 24 bit JMP or JSR. |
| P         | Processor Status | The flags. |
| PC        | Program Counter  | The address of the current CPU instruction |

.A, .X, and .Y can be 8 or 16 bits wide, based on the flag settings (see below).

The Stack Pointer (.S) is 16 bits wide in Native mode and 8 bits wide (and fixed
to the $100-1FF range) in Emulation mode.

.DB and .K are the bank registers, allowing programs and data to occupy separate
64K banks on computers with more than 64K of RAM. (The X16 does not use the bank
registers, instead using addresses $00 and $01 for banking.)

## Status Flags

The native mode flags are as follows:

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

In emulation mode, the **m** and **x** flags are always set to 1.

Here are the 6502 and 65C02 registers, for comparison:

`nv1b dizc`

  n = Negative  
  v = oVerflow  
  1 = this bit is always 1  
  b = brk: set during a BRK instruction interrupt  
  d = Decimal Mode  
  i = Interupts Disabled  
  z = Zero  
  c = Carry  

Note the missing **b** flag on the 65C816. This is no longer needed in native
mode, since the BRK instruction now has its own vector. 

The **e** flag can only accessed via the XCE instruction, which swaps Carry and
the Emulation flag.

The other flags can all be manipulated with SEP and REP, and the various
branch instructions (BEQ, BCS, etc) test some of the flags. The rest
can only be tested indirectly through the stack.

When a BRK or IRQ is triggered in _emulation_ mode, a ghost **b** flag
will be pushed to the stack instead of the **x** flag. This can be used
to test for a BRK vs IRQ in the Interrupt handler.

## 16 bit mode

The 65C816 CPU boots up in emulation mode. This locks the register width to
8 bits and locks out certain operations.

If you want to use the '816 features, including 16-bit operation, you will
need to enable _native_ mode. Clearing **e** switches the CPU to native mode.
However, it's not as simple as just setting a flag. The **e** flag can only
be accessed through the XCE instruction, which swaps the Carry and Emulation
flags.

To switch to native mode, use the following steps:

```
CLC  ; clear the Carry bit
XCE  ; swap the Emulation and Carry bit
```

To switch back to emulation mode, _set_ the Carry flag and perform an XCE again.

```
SEC  ; Set Carry
XCE  ; and push the 1 into the Emulation flag.
```

Once **e** is cleared, the **m** and **x** flags can be set to 1 or 0 to control
the register width.

When the **m** flag is *clear*, Accumulator operations and memory reads and writes
will be 16-bit operations. The CPU reads two bytes at a time with LDA, writes
two bytes at a time with STA, and all math involving .A is 16 bits wide.

Likewise, whenn **x** is clear, the .X and .Y index registers are 16 bits wide.
INX and INY will now count up to 65535, and indexed instructions like `LDA addr,X`
can now cover 64K.

You can use `REP #$10` to enable 16-bit index registers, and `REP #$20` to
enable 16-bit memory and Accumulator. `SEP #$10` or `SEP #$20` will switch back
to 8-bit operation. You can also combine the operand and use `SEP #$30` or 
`REP #$30` to flip both bits at once.

And now we reach the 16-bit assembly trap: the actual assembly opcodes are the
same, regardless of the **x** and **m** flags. This means the assembler needs
to track the state of these flags internally, so it can correctly write one or
two bytes when assembling immediate mode instructions like LDA #$01.

You can help the assembler out by using _hints_. Different assemblers have different
hinting systems, so we will focus on 64TASS and cc65.

[64TASS](https://sourceforge.net/projects/tass64/) accepts `.as` (.A short) and
`.al` (.A long) to  tell the assembler to store 8 bits or 16 bits in an immediate
mode operand. For LDX and LDY, use the `.xs` and `.xl` hints.

The hints for [ca65](https://cc65.github.io/) are `.a8`, `.a16`, `.i8`, and `.i16`

Note that this has no effect on _absolute_ or _indirect_ addressing modes, such
as `LDA $1234` and `LDA ($1000)`, since the operand for these modes is always
16 bits.

To make it easy to remember the modes, just remember that **e**, **m**, and **x**
all _emulate_ 65C02 behavior when _set_.

****

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
| 16 bit relative address         | $1234     | BRL can jump by 32K bytes.                                         |
| Block Move                      | #$12,#$34 | Operands are the bank numbers for block move/copy.                 |

## Vectors

The 65816 has two different sets of interrupt vectors. In emulation mode, the
vectors are the same as the 65C02. In native mode (.e = 0), the native vectors
are used. This allows you to switch to the desired operation mode, based on the
operating mode of your interrupt handlers.

The Commander X16 operates mostly in emulation mode, so native mode interrupts
on the X16 will switch to emulation mode, then simply call the 8-bit interrupt
handlers.

The vectors are:

| Name  | Emu   | Native |
|-------|-------|--------|
| COP   | FFF4  | 00FFE4 |
| BRK   | FFFE  | 00FFE6 |
| ABORT | FFF8  | 00FFE8 |
| NMI   | FFFA  | 00FFEA |
| RESET | FFFC  |        |
| IRQ   | FFFE  | 00FFEE |

The 65C02 shares the same interrupt for BRK and IRQ, and the **b** flag tells
the interrupt handler whether to execute a break or interrupt.

In emulation mode, the 65C816 pushes a modified version of the flags to the
stack. The BRK instruction actually pushes a 1 in bit 4, which can then be
tested in the Interrupt Service Routine. In native mode, however, the flags are
pushed verbatim, since BRK has its own handler.

There is also no native RESET vector, since the CPU always boots to emulation
mode. The CPU always starts at the address stored in $FFFC.

## Instruction Tables

!include Markdown/table_65C816.md

<!-- For PDF formatting -->
<div class="page-break"></div>
