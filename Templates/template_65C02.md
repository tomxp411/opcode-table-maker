
# Appendix C: The 65C02 Processor

This is not meant to be a complete manual on the 65C02 processor, though is
meant to serve as a convenient quick reference. Much of this information comes
from 6502.org and pagetable.com. It is been placed here for convenience though
further information can be found at those (and other) sources.

## Overview

The WDC65C02 CPU is a modern version of the MOS6502 with a few additional
instructions and addressing modes and is capable of running at up to 14 MHz. On
the Commander X16, it is clocked at 8 MHz.

## A note about 65C816 Compatibilty

The Commander X16 may be upgraded at some point to use the WDC 65C816 CPU.
The 65C816 is mostly compatible with the 65C02, except for 4 instructions
(`BBRx`, `BBSx`, `RMBx`, and `SMBx`).

These instructions *may* be deprecated in a future release of the emulator, and
so we suggest not using these instructions. Some people are already using the
65C816 in their X16 systems, and so using these instructions will cause your
programs to malfunction on these computers.

## Instruction Tables

!include Markdown/table_65C02.md

## Status Flags

Flags are stored in the P register. PHP and PLP can be used
to directly manipulate this register. Otherwise the flags
are used to indicate certain statuses and changed by
various instructions.

P-Register:

`NV1B DIZC`

  N = Negative  
  V = oVerflow  
  1 = Always 1  
  B = Interrupt Flag  
  D = Decimal Mode  
  I = Interupts Disabled  
  Z = Zero  
  C = Carry  

## Replacement Macros for Bit Instructions

Since `BBRx`, `BBSx`, `RMBx`, and `SMBx` should not be used to support a
possible upgrade path to the 65816, here are some example macros that can be
used to help convert existing software that may have been using these
instructions:

```asm
.macro bbs bit_position, data, destination
	.if (bit_position = 7)
		bit data
		bmi destination
	.else
		.if (bit_position = 6)
			bit data
			bvs destination
		.else
			lda data
			and #1 << bit_position
			bne destination
		.endif
  .endif
.endmacro

.macro bbr bit_position, data, destination
	.if (bit_position = 7)
		bit data
		bpl destination
	.else
		.if (bit_position = 6)
			bit data
			bvc destination
		.else
			lda data
			and #1 << bit_position
			beq destination
		.endif
	.endif
.endmacro

.macro rmb bit, destination
	lda #$1 << bit
	trb destination
.endmacro

.macro smb bit, destination
	lda #$1 << bit
	tsb destination
.endmacro
```

The above is CA65 specific but the code should work similarly for other
languages. The logic can also be used to if using an assembly language tool
that does not have macro support with small changes.

## Further Reading

- <http://www.6502.org/tutorials/6502opcodes.html>
- <http://6502.org/tutorials/65c02opcodes.html>
- <https://www.pagetable.com/c64ref/6502/?cpu=65c02>
- <http://www.oxyron.de/html/opcodesc02.html>
- <https://www.nesdev.org/wiki/Status_flags>
- <https://skilldrick.github.io/easy6502/>
- <https://www.westerndesigncenter.com/wdc/documentation/w65c02s.pdf>
- <https://www.westerndesigncenter.com/wdc/documentation/w65c816s.pdf>

[^1]: Add 1 cycle if a page boundary is crossed  
[^2]: Add 1 cycle if branch is taken on the same page, or 2 if it's taken to
a different page  
[^3]: 65C02 specific addressing mode  
[^4]: 65C02 specific op-code  
[^5]: Not supported on the 65C816  

<!-- For PDF formatting -->
<div class="page-break"></div>
