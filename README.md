# 8-bit CPU emulator
A Python object-oriented high-level emulator for a simple 8-bit CPU, inspired by the <a href=https://eater.net/8bit/> project of Ben Eater </a>. <br>
The code is organized into three different files:
* <code> utils.py </code>: the definition of the classes of the components (registers, clock, ...) and some helper functions
* <code> CPU.py </code>: the main class with all the logic functions to handle every microinstruction flexibly and scalable. Inside the class, there are also the functions <code> load() </code> (the RAM) to read an ASSEMBLY code from a .txt file, and <code> run() </code>. By default, the state of the CPU after every micro-instruction will be saved into a log file.
* <code> main.py </code>: to load the run and start the emulator. <br>
At the moment, our instruction set is composed of *LDA*, *ADD*, *SUB*, *STA*, *LDI*, *JMP*, *JC*, *JZ*, *OUT*, *HLT*. This CPU is slightly more complicated than a SAP 1. <br>
As a reference, here are the high-level schematics of the Ben Eater CPU:
<p align="center">
<img src="https://eater.net/schematics/high-level.png" alt="schematics" width="50%" height="50%">
</p>
