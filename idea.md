# MAPD_A

## Modules

### Clock module
Synch of the operations. 
In our case will be something similar to a while (while !HLT) loop, printing (or saving into a .txt) the states of all components before the end of each iteration. 
It is related to the micro-instructions (fetch, exectution) and not to the instruction per se. 

### Registers
Three 8-bit registers: A, B, IR. A and B are general-purpose, IR is the instruction register (store the current instruction that's being executed). 
During the lessons, A was the accumulator and was a special register. 
-> Three numpy array of fixed size. 


### ALU
ALU can perform either A+B or A-B. 
Depending on the result, the flags might be changed. 
Does it save the result on A? Yes, just overwrite one register
Do we need a class or it's part of the "main"? Maybe in the main is better


### RAM
RAM stores both the program and the data. 16 addresses of 8 bits each. 
-> One numpy array (note that the numpy array has indices from 0 to 15 and not to 0x0 to 0xF)


### Program counter
It counts from 0000, keeping track of the current instruction. 

### Output
LEDs. In our case a string with the number. Possibility to print it in a file .txt


### CPU control logic
It tells the CPU what to do depending on the opcode (instruction). 
-> If - elif - elif - elif


## Partial schema
We can decide how to rapresent a number: array or string? (probably better strings)

class CPU{

    RAM: array 16x(8 bits: op code + RAM index)
    A: array 8 bits
    B: array 8 bits
    IR: array 8 bits
    Flags: list of two integers
    Program counter: array 4 bits (next istruction, RAM index)
    MAR: array 4 bits (current istruction, RAM index)
    Time state: array 6 bits

    function init: set all to zero 
    self.RAM = [0] * 16  # Initialize RAM with zeros
    self.A = [0] * 8
    self.B = [0] * 8
    self.IR = [0] * 8
    self.Flags = [0, 0]  # Placeholder for flags
    self.PC = [0] * 4
    self.MAR = [0] * 4
    self.TimeState = [0] * 6
    
    function load(.txt): from .txt to RAM, different line for each instruction

    function run():
        while !HLT: 
            for i in range(6):

                if time state == 000001:
                    MAR = PC
                elif time state == 000010:
                    PC = PC + 1
                elif time state == 000100:
                    IR = RAM[PC]

                elif time state == 001000:
                    if op code == "ADD": ---
                    elif op code == ----
                # add others op_code

                TO DO: execution cycle steps

            time state = time state + 1

    #That would be it if we were designing the code by scratch. Instead we need all the mini-function such as:

    load_program
        # Load program from a .txt file into RAM
    
    function execution_cycle
        if opcode == "ADD":
            self.alu_add()
        elif opcode == "SUB":
        etc...
    
    function fetch
        self.load_mar
        self.load_pc
        load_ir
        
    function update_time_state:
        time state = time state + 1
        #But time state is something like "000000" and time stata + 1 is "000010"
        (sono addormentato come cambia il time state come funziona il +1)

    function run
        while instruction !HLT
            fetch_cycle
            execution_cycle
            update_time_state

    function load_mar

    function load_PC

    function load_ir

    function decode_instruction
    #decode_instruction method, you need to extract the opcode from the instruction stored in the Instruction Register (IR)


}

Fetch Cycles (Fetching the instruction from memory):
Fetch 1: Load the instruction address from the Program Counter (PC) into the Memory Address Register (MAR).
Fetch 2: Read the instruction from memory using the address present in the MAR and load it into the Instruction Register (IR).
Fetch 3: Increment the Program Counter to point to the next address.

Execution Cycles (Executing the instruction):
Execution 1: Decode the instruction present in the IR to obtain the opcode and determine the operation to be performed.
Execution 2: Perform the desired operation, for example, add A and B in the ALU.
Execution 3: Update the registers and flags, and prepare the CPU for the next instruction.
