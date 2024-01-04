# MAPD_A

### Clock module
Synch of the operations. 
In our case will be something similar to a while (while !HLT) loop, printing (or saving into a .txt) the states of all components before the end of each iteration. 

### Registers
Three 8-bit registers: A, B, IR. A and B are general-purpose, IR is the instruction register (store the current instruction that's being executed). 
During the lessons, A was the accumulator and was a special register. 
-> Three numpy array of fixed size. 


### ALU
ALU can perform either A+B or A-B. 
Depending on the result, the flags might be changed. 
Does it save the result on A? Do we need a class or it's part of the "main"?


### RAM
RAM stores both the program and the data. 16 addresses of 8 bit each. 
-> One numpy array (note that the numpy array has indices from 0 to 15 and not to 0x0 to 0xF)


### Program counter
It counts from 0000, keeping track of the current instruction. 

### Output
LEDs. In our case a string with the number. 


### CPU control logic
It tells the CPU what to do depending on the opcode (instruction). 
-> If - elif - elif - elif