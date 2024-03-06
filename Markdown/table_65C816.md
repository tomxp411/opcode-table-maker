## Instructions By Opcode

|           |x0         |x1         |x2         |x3         |x4         |x5         |x6         |x7         |x8         |x9         |xA         |xB         |xC         |xD         |xE         |xF         |
|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|
|        0x |[BRK](#BRK)|[ORA](#ORA)|[COP](#COP)|[ORA](#ORA)|[TSB](#TSB)|[ORA](#ORA)|[ASL](#ASL)|[ORA](#ORA)|[PHP](#PHP)|[ORA](#ORA)|[ASL](#ASL)|[PHD](#PHD)|[TSB](#TSB)|[ORA](#ORA)|[ASL](#ASL)|[ORA](#ORA)|
|        1x |[BPL](#BPL)|[ORA](#ORA)|[ORA](#ORA)|[ORA](#ORA)|[TRB](#TRB)|[ORA](#ORA)|[ASL](#ASL)|[ORA](#ORA)|[CLC](#CLC)|[ORA](#ORA)|[INC](#INC)|[TCS](#TCS)|[TRB](#TRB)|[ORA](#ORA)|[ASL](#ASL)|[ORA](#ORA)|
|        2x |[JSR](#JSR)|[AND](#AND)|[JSL](#JSL)|[AND](#AND)|[BIT](#BIT)|[AND](#AND)|[ROL](#ROL)|[AND](#AND)|[PLP](#PLP)|[AND](#AND)|[ROL](#ROL)|[PLD](#PLD)|[BIT](#BIT)|[AND](#AND)|[ROL](#ROL)|[AND](#AND)|
|        3x |[BMI](#BMI)|[AND](#AND)|[AND](#AND)|[AND](#AND)|[BIT](#BIT)|[AND](#AND)|[ROL](#ROL)|[AND](#AND)|[SEC](#SEC)|[AND](#AND)|[DEC](#DEC)|[TSC](#TSC)|[BIT](#BIT)|[AND](#AND)|[ROL](#ROL)|[AND](#AND)|
|        4x |[RTI](#RTI)|[EOR](#EOR)|[WDM](#WDM)|[EOR](#EOR)|[MVP](#MVP)|[EOR](#EOR)|[LSR](#LSR)|[EOR](#EOR)|[PHA](#PHA)|[EOR](#EOR)|[LSR](#LSR)|[PHK](#PHK)|[JMP](#JMP)|[EOR](#EOR)|[LSR](#LSR)|[EOR](#EOR)|
|        5x |[BVC](#BVC)|[EOR](#EOR)|[EOR](#EOR)|[EOR](#EOR)|[MVN](#MVN)|[EOR](#EOR)|[LSR](#LSR)|[EOR](#EOR)|[CLI](#CLI)|[EOR](#EOR)|[PHY](#PHY)|[TCD](#TCD)|[JMP](#JMP)|[EOR](#EOR)|[LSR](#LSR)|[EOR](#EOR)|
|        6x |[RTS](#RTS)|[ADC](#ADC)|[PER](#PER)|[ADC](#ADC)|[STZ](#STZ)|[ADC](#ADC)|[ROR](#ROR)|[ADC](#ADC)|[PLA](#PLA)|[ADC](#ADC)|[ROR](#ROR)|[RTL](#RTL)|[JMP](#JMP)|[ADC](#ADC)|[ROR](#ROR)|[ADC](#ADC)|
|        7x |[BVS](#BVS)|[ADC](#ADC)|[ADC](#ADC)|[ADC](#ADC)|[STZ](#STZ)|[ADC](#ADC)|[ROR](#ROR)|[ADC](#ADC)|[SEI](#SEI)|[ADC](#ADC)|[PLY](#PLY)|[TDC](#TDC)|[JMP](#JMP)|[ADC](#ADC)|[ROR](#ROR)|[ADC](#ADC)|
|        8x |[BRA](#BRA)|[STA](#STA)|[BRL](#BRL)|[STA](#STA)|[STY](#STY)|[STA](#STA)|[STX](#STX)|[STA](#STA)|[DEY](#DEY)|[BIT](#BIT)|[TXA](#TXA)|[PHB](#PHB)|[STY](#STY)|[STA](#STA)|[STX](#STX)|[STA](#STA)|
|        9x |[BCC](#BCC)|[STA](#STA)|[STA](#STA)|[STA](#STA)|[STY](#STY)|[STA](#STA)|[STX](#STX)|[STA](#STA)|[TYA](#TYA)|[STA](#STA)|[TXS](#TXS)|[TXY](#TXY)|[STZ](#STZ)|[STA](#STA)|[STZ](#STZ)|[STA](#STA)|
|        Ax |[LDY](#LDY)|[LDA](#LDA)|[LDX](#LDX)|[LDA](#LDA)|[LDY](#LDY)|[LDA](#LDA)|[LDX](#LDX)|[LDA](#LDA)|[TAY](#TAY)|[LDA](#LDA)|[TAX](#TAX)|[PLB](#PLB)|[LDY](#LDY)|[LDA](#LDA)|[LDX](#LDX)|[LDA](#LDA)|
|        Bx |[BCS](#BCS)|[LDA](#LDA)|[LDA](#LDA)|[LDA](#LDA)|[LDY](#LDY)|[LDA](#LDA)|[LDX](#LDX)|[LDA](#LDA)|[CLV](#CLV)|[LDA](#LDA)|[TSX](#TSX)|[TYX](#TYX)|[LDY](#LDY)|[LDA](#LDA)|[LDX](#LDX)|[LDA](#LDA)|
|        Cx |[CPY](#CPY)|[CMP](#CMP)|[REP](#REP)|[CMP](#CMP)|[CPY](#CPY)|[CMP](#CMP)|[DEC](#DEC)|[CMP](#CMP)|[INY](#INY)|[CMP](#CMP)|[DEX](#DEX)|[WAI](#WAI)|[CPY](#CPY)|[CMP](#CMP)|[DEC](#DEC)|[CMP](#CMP)|
|        Dx |[BNE](#BNE)|[CMP](#CMP)|[CMP](#CMP)|[CMP](#CMP)|[PEI](#PEI)|[CMP](#CMP)|[DEC](#DEC)|[CMP](#CMP)|[CLD](#CLD)|[CMP](#CMP)|[PHX](#PHX)|[STP](#STP)|[JMP](#JMP)|[CMP](#CMP)|[DEC](#DEC)|[CMP](#CMP)|
|        Ex |[CPX](#CPX)|[SBC](#SBC)|[SEP](#SEP)|[SBC](#SBC)|[CPX](#CPX)|[SBC](#SBC)|[INC](#INC)|[SBC](#SBC)|[INX](#INX)|[SBC](#SBC)|[NOP](#NOP)|[XBA](#XBA)|[CPX](#CPX)|[SBC](#SBC)|[INC](#INC)|[SBC](#SBC)|
|        Fx |[BEQ](#BEQ)|[SBC](#SBC)|[SBC](#SBC)|[SBC](#SBC)|[PEA](#PEA)|[SBC](#SBC)|[INC](#INC)|[SBC](#SBC)|[SED](#SED)|[SBC](#SBC)|[PLX](#PLX)|[XCE](#XCE)|[JSR](#JSR)|[SBC](#SBC)|[INC](#INC)|[SBC](#SBC)|

## Instructions By Category

|Category       |Instructions   |
|---------------|---------------|
| Arithmetic    | [ADC](#ADC) , [SBC](#SBC) |
| Boolean       | [AND](#AND) , [EOR](#EOR) , [ORA](#ORA) |
| Shift         | [ASL](#ASL) , [LSR](#LSR) , [ROL](#ROL) , [ROR](#ROR) |
| Branch        | [BCC](#BCC) , [BCS](#BCS) , [BEQ](#BEQ) , [BMI](#BMI) , [BNE](#BNE) , [BPL](#BPL) , [BRA](#BRA) , [BRK](#BRK) , [BRL](#BRL) , [BVC](#BVC) , [BVS](#BVS) |
| Test          | [BIT](#BIT) , [TRB](#TRB) , [TSB](#TSB) |
| Flags         | [CLC](#CLC) , [CLD](#CLD) , [CLI](#CLI) , [CLV](#CLV) , [REP](#REP) , [SEC](#SEC) , [SED](#SED) , [SEI](#SEI) , [SEP](#SEP) |
| Compare       | [CMP](#CMP) , [CPX](#CPX) , [CPY](#CPY) |
| Interrupt     | [COP](#COP) , [WAI](#WAI) |
| Inc/Dec       | [DEC](#DEC) , [DEX](#DEX) , [DEY](#DEY) , [INC](#INC) , [INX](#INX) , [INY](#INY) |
| Flow          | [JMP](#JMP) , [JSL](#JSL) , [JSR](#JSR) , [NOP](#NOP) , [RTI](#RTI) , [RTL](#RTL) , [RTS](#RTS) , [WDM](#WDM) |
| Load          | [LDA](#LDA) , [LDX](#LDX) , [LDY](#LDY) |
| Block Move    | [MVN](#MVN) , [MVP](#MVP) |
| Stack         | [PEA](#PEA) , [PEI](#PEI) , [PER](#PER) , [PHA](#PHA) , [PHB](#PHB) , [PHD](#PHD) , [PHK](#PHK) , [PHP](#PHP) , [PHX](#PHX) , [PHY](#PHY) , [PLA](#PLA) , [PLB](#PLB) , [PLD](#PLD) , [PLP](#PLP) , [PLX](#PLX) , [PLY](#PLY) |
| Store         | [STA](#STA) , [STP](#STP) , [STX](#STX) , [STY](#STY) , [STZ](#STZ) |
| Register Swap | [TAX](#TAX) , [TAY](#TAY) , [TCD](#TCD) , [TCS](#TCS) , [TDC](#TDC) , [TSC](#TSC) , [TSX](#TSX) , [TXA](#TXA) , [TXS](#TXS) , [TXY](#TXY) , [TYA](#TYA) , [TYX](#TYX) , [XBA](#XBA) , [XCE](#XCE) |

