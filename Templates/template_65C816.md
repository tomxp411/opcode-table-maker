
# Appendix E: The 65C816 Processor

**Table of Contents**

1. [Overview](#overview)
2. [Compatibility with the 65C02](#compatibility-with-the-65c02)
3. [Registers](#)
4. [Status Flags](#)
5. [16 bit modes]
6. [Address Modes]
7. [Vectors]
8. [Instruction Tables](#instruction-tables)

## Overview

The WDC65C816 CPU is an 8/16 bit CPU and a follow-up to the 6502 processor. All
of the familiar 6502 instructions and address modes are retained, and some new
ones are added. 

The CPU now also operates in 16-bit mode when required. This allows the Accumulator
to hold 16-bit values, and the CPU reads and writes 2 bytes at a time in this mode.

The .X and .Y registers, also known as the Index registers, can also be separately
set to 16-bit mode, which allows for indexed operations up to 64KB. 

Zero Page has been renamed to Direct Page, and Direct Page can now be relocated
anywhere in the first 64K of RAM. As a result, all of the Zero Page instructions
are now "Direct" instructions and can operate anywhere in the X16's address range.

Likewise, the Stack can also be relocated, and the stack pointer is now 16 bits.
This allows for a much larger stack, and the combination of stack and DP relocation
offer interesting multitasking opportunities.

The 65C816 also extends the address bus to 24 bits, but the X16 is not equipped to
decode the bask address; as a result, the 65C816 is still limited to the same 16-bit
address space as the 65C02. 

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

The Stack Pointer (.S) is also relocatable to any 16-bit address. 

.DB and .K are the bank registers, allowing programs and data to occupy separate
64K banks on properly equipped computers.

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

The emulation mode flags are the same as the 65C02:

`nv1b dizc e`

  n = Negative  
  v = oVerflow  
  1 = this bit is always 1
  b = brk: set during a BRK instruction interrupt
  d = Decimal Mode  
  i = Interupts Disabled  
  z = Zero  
  c = Carry  
  e = Emulation Mode (0=65C02 mode, 1=65C816 mode)

**e** can only accessed via the XCE instruction, which swaps Carry and
the Emulation flag. 

The other flags can all be manipulated with SEP and REP, and the various
branch instructions (BEQ, BCS, etc) test some of the flags. The rest
can only be tested indirectly through the stack. 

## 16 bit modes

To enable 16-bit operation, the CPU must be placed in native mode. This means
clearing the **e** flag, which is a two step process. 

```
CLC  ; clear the Carry bit
XCE  ; swap the Emulation and Carry bit
```

Once **e** is cleared, the **m** and **x** flags are visible. These can be set
to 1 or 0 to control the register width. Use SEP and REP to toggle these bits.

When the **m** flag is *clear*, Accumulator operations and memory reads and writes
will be 16-bit operations. This allows for 16-bit math when **m** is 0. 

Likewise, whenn **x** is clear, the .X and .Y index registers are 16 bits wide.
INX and INY will now count up to 65535, and indexed instructions like LDA addr,X
can now cover 64K without changing the base address.

To make it easy to remember the modes, **e**, **m**, and **x** all operate 
consistently: Set to 1, they _emulate_ 65C02 behavior, and set to 0, they 
allow _native_ behavior.

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
| 16 bit relative address         | 1234      | BRL can jump by 32K bytes.                                         |
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
| RESET | FFFC  | 00FFFC |
| IRQ   | FFFE  | 00FFEE |

The 65C02 shares the same interrupt for BRK and IRQ, so the 65C816 mirrors this
behavior. The .b flag will be set when a BRK instruction is executed, allowing
the IRQ handler to decide how to handle the interrupt.

On the 65C816, BRK has its own vector (00FFE6), so the .b flag is not used.
Instead, the .b flag is swapped out for the 16-bit index register flag (.x).

Also, note that the CPU starts up in emulation mode, so after a RESET, the CPU
will always execute the FFFC vector, no matter what state the CPU was in when
RESET was asserted.

## Instruction Tables

!include Markdown/table_65C816.md

<!-- For PDF formatting -->
<div class="page-break"></div>
