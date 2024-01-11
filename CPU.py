from utils import *	


class CPU:

    # Initialize the components of the CPU
    def __init__(self):
        self.clock=Clock(self)
        self.ringCounter=RingCounter(6)
        self.programCounter=ProgramCounter()
        self.memoryAddressRegister=NibbleRegister()
        self.ram=RAM()
        self.aRegister=ByteRegister()
        self.bRegister=ByteRegister()
        self.instructionRegister=InstructionRegister()
        self.alu=ALU(self.aRegister,self.bRegister)
        self.flagZero=FlagZero(self.aRegister)	
        self.flagCarry=FlagCarry(self.alu)


    # Functions: the core of the CPU
    def bus(self, reg1, reg2):
        # Copy the content of the register reg1 into reg2
        self.advance_clock()
        reg2.write(reg1.read())

    def pc_to_mar(self):
        # Copy the content of the program counter into the MAR
        data = self.programCounter.read()
        self.memoryAddressRegister.write(data)
        
    def ram_to_a(self):
        # Copy the content of the RAM into the register A
        address = binary_to_decimal(self.memoryAddressRegister.read())
        self.aRegister.write(self.ram.read(address))

    def ram_to_b(self):
        # Copy the content of the RAM into the register B
        address = binary_to_decimal(self.memoryAddressRegister.read())
        self.bRegister.write(self.ram.read(address))

    def ram_to_ir(self):
        # Copy the content of the RAM into the Instruction Register
        address = binary_to_decimal(self.memoryAddressRegister.read())
        self.instructionRegister.write(self.ram.read(address))

    def a_to_ram(self):
        # Copy the content of the register A into the RAM
        address = binary_to_decimal(self.memoryAddressRegister.read())
        self.ram.write(self.aRegister.read(), address)

    def a_to_terminal(self):
        # Print the state of the register A
        print(f'OUTPUT: {self.aRegister}')

    def ir_to_mar(self):
        # Copy the content of the Instruction Register into the MAR
        self.memoryAddressRegister.write(self.instructionRegister.readOperand())

    def ir_to_a(self):
        # Copy the content of the IR into the register A
        self.aRegister.write('0000' + self.instructionRegister.readOperand())

    def ir_to_pc(self):
        # Copy the content of the Instruction Register into the program counter
        self.programCounter.write(self.instructionRegister.readOperand())

    def ir_to_pc_c(self):
        # Copy the content of the IR into the PC, given the Carry Flag
        if self.flagCarry.read() == 1:
            self.programCounter.write(self.instructionRegister.readOperand())

    def ir_to_pc_z(self):
        # Copy the content of the IR into the PC, given the Zero Flag
        if self.flagZero.read() == 1:
            self.programCounter.write(self.instructionRegister.readOperand())

    def alu_to_a_add(self):
        # Copy the content of the ALU into A, in case of a sum
        self.flagCarry.update()
        self.aRegister.write(self.alu.read('add'))

    def alu_to_a_sub(self):
        # Copy the content of the ALU into A, in case of a difference
        self.aRegister.write(self.alu.read('sub'))

    def no_op(self):
        # No operation
        pass

    def clock_off(self):
        # Turn off the clock, abort the run
        self.clock.on = False


    # Define the microinstructions set of every instruction
    macro_instructions={ 
        'LDA':[ir_to_mar, ram_to_a, no_op],
        'ADD':[ir_to_mar, ram_to_b, alu_to_a_add],
        'SUB':[ir_to_mar, ram_to_b, alu_to_a_sub],
        'STA':[ir_to_mar, a_to_ram, no_op],
        'LDI':[ir_to_a, no_op, no_op],
        'JMP':[ir_to_pc, no_op, no_op],
        'JC':[ir_to_pc_c, no_op, no_op],
        'JZ':[ir_to_pc_z, no_op, no_op],
        'OUT':[a_to_terminal, no_op, no_op],
        'HLT':[clock_off, no_op, no_op]
    }


    # Dictionaries to convert op-code in mnemonics and viceversa
    mnemo_op_code = {
        "LDA": "0000",
        "ADD": "0001",
        "SUB": "0010",
        "OUT": "1110",
        "HLT": "1111",
        "STA": "1010",
        "LDI": "1011",
        "JMP": "0101",
        "JC" : "0111",
        "JZ" : "1001"
    }

    op_code_mnemo = {
        '0000' : 'LDA', 
        '0001' : 'ADD',
        '0010' : 'SUB',
        '1110' : 'OUT',
        '1111' : 'HLT',
        "1010" : "STA",
        "1011" : "LDI",
        "0101" : "JMP" ,
        "0111" : "JC" ,
        "1001" : "JZ"
    }

    # Helper function to get the op-code of a mnemonics
    def convert_mnemo_op_code(self, instruction):
        op_code = self.mnemo_op_code.get(instruction, "N/A")
        return op_code


    # Function to load the ram from a .txt ASSEMBLY script
    def load(self, file_path):

        # Open the file in reading
        with open(file_path, "r") as file:
            # Read each line
            for line_number, line in enumerate(file):
                # Delete blanks
                line = line.strip()

                if line[0].isalpha():
                    # Split the line into instruction and hexadecimal number
                    parts = line.split()
                    
                    if len(parts) == 1:
                        # Convert instruction to op code
                        op_code = self.convert_mnemo_op_code(line)
                        combined_data = op_code + "0000"
                        
                    
                    if len(parts) == 2:
                        instruction = parts[0]
                        hex_number = parts[1]
                        # Convert instruction to op code
                        op_code = self.convert_mnemo_op_code(instruction)
                        if hex_number == "0x0":
                            binary_number = "0000"
                        else:
                            # Extract the hexadecimal number from the target line
                            binary_number = hex_to_binary(hex_number, 4)
                        # Combine op code and binary number
                        combined_data = op_code + binary_number
                        
                    
                elif not line[0].isalpha():
                    # Split the line into instruction and hexadecimal number
                    if line == "0x0" or line == "0x00":
                            combined_data = "00000000"
                    else:
                        combined_data = hex_to_binary(line, 8)
                else:
                    continue
                # Append combined data to RAM using line number as address
                self.ram.write(combined_data, line_number)


    # Function to make both the clock and the ringcounter click
    def advance_clock(self, how_much=1):
        for i in range(how_much):
            self.clock.advance(self)
            self.ringCounter.advance()


    # Function to execute the program 
    def run(self, threshold=1000):
        # Turn on the clock
        self.clock.on = True

        # Start executing the program 
        while self.clock.on:
            
            # Fetch cycle
            self.pc_to_mar()
            self.advance_clock()
            self.ram_to_ir()
            self.advance_clock()
            self.programCounter.advance()
            self.advance_clock()

            # Execution cycle
            while self.clock.on:

                # Read the op-code from the IR
                op_code = self.instructionRegister.readOpCode()    
                # Read the ring counter to understand what microinstruction is needed
                time_state = self.ringCounter.read()                
                # Execute the correspondent micro-instruction 
                self.macro_instructions[self.op_code_mnemo[op_code]][time_state - 3](self)

                # Make the clock click
                self.advance_clock()

                # Exit execution if cycle ended
                # This allows to implement also instructions with more than 6 time states
                if self.ringCounter.read()==0:
                    break

                # Abort the run after some iteration (mainly for debugging purpouses)
                if self.clock.state > threshold:
                    self.clock.on = False
                    break

    # Define the printable state of the CPU
    def __str__(self):
        if self.clock.state == 0:
            snapshot = f"Clock: {self.clock.__str__()}\nRing Counter: {self.ringCounter.__str__()}\nProgram Counter: {self.programCounter.__str__()}\n" \
                    f"Memory Address Register: {self.memoryAddressRegister.__str__()}\nA Register: {self.aRegister.__str__()}\n" \
                    f"B Register: {self.bRegister.__str__()}\nInstruction Register: {self.instructionRegister.__str__()}\n" \
                    f"Flag Z: {self.flagZero.__str__()}\nFlag C: {self.flagCarry.__str__()}\nRAM:\n{self.ram.__str__()}\n"
            global previous_ram_str
            previous_ram_str=self.ram.__str__()
        
        else:
            snapshot = f"Clock: {self.clock.__str__()}\nRing Counter: {self.ringCounter.__str__()}\nProgram Counter: {self.programCounter.__str__()}\n" \
                    f"Memory Address Register: {self.memoryAddressRegister.__str__()}\nA Register: {self.aRegister.__str__()}\n" \
                    f"B Register: {self.bRegister.__str__()}\nInstruction Register: {self.instructionRegister.__str__()}\n" \
                    f"Flag Z: {self.flagZero.__str__()}\nFlag C: {self.flagCarry.__str__()}\n"
            if previous_ram_str!= self.ram.__str__():
                previous_ram_str=self.ram.__str__()
                snapshot = f"Clock: {self.clock.__str__()}\nRing Counter: {self.ringCounter.__str__()}\nProgram Counter: {self.programCounter.__str__()}\n" \
                    f"Memory Address Register: {self.memoryAddressRegister.__str__()}\nA Register: {self.aRegister.__str__()}\n" \
                    f"B Register: {self.bRegister.__str__()}\nInstruction Register: {self.instructionRegister.__str__()}\n" \
                    f"Flag Z: {self.flagZero.__str__()}\nFlag C: {self.flagCarry.__str__()}\nRAM:\n{self.ram.__str__()}\n"
            
        return snapshot

		
