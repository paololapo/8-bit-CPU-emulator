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
Does it save the result on A? Do we need a class or it's part of the "main"?


### RAM
RAM stores both the program and the data. 16 addresses of 8 bits each. 
-> One numpy array (note that the numpy array has indices from 0 to 15 and not to 0x0 to 0xF)


### Program counter
It counts from 0000, keeping track of the current instruction. 

### Output
LEDs. In our case a string with the number. 


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
    
    function load(.txt): from .txt to RAM

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

                TO DO: execution cycle steps

            time state = time state + 1

    #That would be it if we were designing the code by scratch. Instead we need all the mini-function such as:

    function update_time_state: 
        time state = time state + 1
        #But time state is something like "000000" and time stata + 1 is "000010"

    function load_mar

    function load_PC

    #And so on...



}