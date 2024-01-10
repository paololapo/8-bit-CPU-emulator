# 8-bit CPU emulator
### The context
The final project for the 'Management and Analysis of Physics Dataset (MOD. A)' course in the 'Physics of Data' master program, University of Padua. <br>
Group 7: <a href=https://github.com/paololapo> Paolo Lapo Cerni </a>, <a href=https://github.com/emanuele-quaglio> Emanuele Quaglio </a>, <a href=https://github.com/LorenzoVigorelli> Lorenzo Vigorelli </a>
### The project
A Python object-oriented high-level emulator for a simple 8-bit CPU, inspired by the <a href=https://eater.net/8bit/> project of Ben Eater </a>. <br>
The code is organized into three different files:
* <code> utils.py </code>: the definition of the classes of the components (registers, clock, ...) and some helper functions
* <code> CPU.py </code>: the main class with all the logic functions to handle every microinstruction flexibly and scalably. Inside the class, there are also the functions <code> load() </code> (the RAM) to read an ASSEMBLY code from a .txt file, and <code> run() </code>. By default, the state of the CPU after every micro-instruction will be saved into a log file.
* <code> main.py </code>: to load the RAM and start the emulator.
  
At the moment, our instruction set is composed of *LDA*, *ADD*, *SUB*, *STA*, *LDI*, *JMP*, *JC*, *JZ*, *OUT*, *HLT*. Thus, this CPU is slightly more complicated than a SAP 1. <br>
As a reference, here are the high-level schematics of the Ben Eater CPU:
<p align="center">
<img src="https://eater.net/schematics/high-level.png" alt="schematics" width="70%" height="70%">
</p>
