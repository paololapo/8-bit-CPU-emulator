""" CPU """
class CPU:
    
    """ CLASSES """

    class Register:
        """
        General purpouse regis
        """    

        def __init__(self):
            self.state = ''

        # Return the state of the register
        def read(self):
            return self.state

        # Overwrite the state of the register
        def write(self, data):
            self.state = data

        #TO DO 
        # print: similar to read but in a .txt convention
        def print(self):
            return self.state


    class ByteRegister(Register):
        def __init__(self):
            self.state = '0'*8


    class NibbleRegister(Register):
        def __init__(self):
            self.state = '0'*4
    
        
    class RAM(Register):
        """
        RAM stores both the program and the data. 16 addresses of 8 bits each
        """

        def __init__(self):
            # List of 8-bits registers
            self.state = [ByteRegister() for _ in range(16)]

        # Write on the address of the RAM
        def write(self, data, address):
            # Data validation
            assert type(data) is str, 'data type error'
            assert len(data) == 8, 'size error'

            self.state[address].write(data)
        
        # Read the address of the RAM
        def read(self, address):
            return self.state[address].read()
        
        # TO DO
        # def print()


    class InstructionRegister(ByteRegister):
        """
        Register where you can access the first and the second nibbles 
        """

        def readOpCode(self):
            return self.read()[:4]
        
        def readOperand(self):
            return self.read()[4:]


    class ProgramCounter(NibbleRegister):
        """
        4-bits program counter
        """

        # Update the counter
        def advance(self):       
            # Get the decimal value
            value = int(self.state, 2)
            # Update the counter mod 2**4
            value = (value + 1)%2**4
            # Convert the new value into a 4-bits string
            string = bin(value)[2:].zfill(4)

            self.state = string

    class Flag(Register):
        def __init__(self):
            self.state = 0
        

    class ALU(ByteRegister):
        """
        The logic of the CPU
        """
        def __init__(self, aRegister, bRegister):
            self.a = aRegister
            self.b = bRegister
            
        #def read(mode):
			#if(mode=='add'):
				
			#elif(mode=='sub')
    
    """ FUNCTIONS """
	
    def __init__():
        clock=Clock()
        ringCounter=RingCounter()
        programCounter=ProgramCounter()
        ram=RAM()
        memoryAddressRegister=ByteRegister()
        aRegister=ByteRegister()
        bRegister=ByteRegister()
        instructionRegister=InstructionRegister()
        alu=ALU(aRegister,bRegister)
        flagA=Flag(a)	

    def load_ram(self, input_path):#parser, loads to ram the code
        pass
    def run(): #esegue il programma in ram
        clock.on=True 
        while(clock.on):
            fetch(self)
            advance_clock(3)
            while(clock.on):

                macro_instructions[mnemo_op_code[self.instructionRegister.readOpCode()]][self.ringCounter.read()](self)

                #questo esegue la micro-operazione dell'istruzione presente sull'ir,
                #corrispondente al time-state indicato sul microclock.

                advance_clock()

        def advance_clock(how_much=1):
            self.clock().advance(how_much)
            self.ringCounter().advance(how_much)