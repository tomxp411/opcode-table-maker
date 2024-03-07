
# Appendix E: The 65C816 Processor

[Click here for the opcode listing](#instruction-tables)

This is not meant to be a complete manual on the 65C816 processor. This is a
reference. Much of this information comes from 6502.org, undisbeliever.net, and
[Programming the 65816: Including the 6502, 65C02, and
65802](https://www.amazon.com/Programming-65816-Including-65C02-65802/dp/0893037893)
by David Eyes and Ron Lichty.

## Overviewv

The WDC65C816 CPU is an 8/16 bit CPU and a follow-up to the 6502 processor. It
uses the same basic instructions, with additional 16-bit instructions and
several new address modes. It also includes two block move instructions, which
are handy for copying large amounts of memory around the system.

The CPU has 16-bit wide registers. In addition, Zero Page has been renamed to
Direct Page and, along with the Stack, can be moved anywhere in the first 64K of
RAM.

## Compatibility with the 65C02

The 65C916 CPU is generally compatible with the 65C02 instruction set, with the
exception  of the `BBRx`, `BBSx`, `RMBx`, and `SMBx` instructions.

## Registers

The 65C816 has some additional registers, mostly dealing with banking. The .A,
.X, and .Y registers are also upgrade to 16 bits when in native mode and the .m
and .x flags are clear.

| Notation   | Name             | Description     |
|------------|------------------|-----------------|
| A         | Accumulator      | The accumulator. It stores the result of moth math and logical operations.  |
| X         | X Index          | .X is mostly used as a counter and to offset addresses with X indexed modes |
| Y         | Y Index          | .Y is mostly used as a counter and to offset addresses with Y indexed modes |
| S         | Stack Pointer    | SP points to the next open position on the stack.                           |
| DB or DBR | Data Bank        | Data bank is the default bank for operations that use a 16 bit address.     |
| K or  PBR | Program Bank     | The default address for 16 bit JMP and JSR oprerations. Can only be set with a 24 bit JMP or JSR. |
| P         | Processor Status | The flags. |
| PC        | Program Counter  | The address of the current CPU instruction |

## Status Flags

Flags are stored as the P register. PHP, PLP, SEP, and REP instructions can
modify the flags. They can be tested with the various Branch instructions

The e flag can only be set with the XCE instruction, which swaps the Carry flag
and the Emulation flag.

Depending on the CPU mode, there are two configurations. (Note that on the
65C816, the flag names are written in *lower case*, to avoid confusion with
overlapping CPU register names.)

In Emulation mode, the flags follow the 65C02 convention. In Native mode (e=1),
the flags are as follows:

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
