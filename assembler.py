class Register:
    # address is a 3 bit string
    def __init__(self, address):
        self.value = 0;
        self.address = address

    def addr(self):
        return self.address

    def val(self):
        return self.value

class Variable:
    def __init__(self, name):
        self.value = 0;
        self.name = name;

def Addition(r1, r2, r3): #Performs reg1 = reg2+ reg3. If the computation overflows, then the overflow flag is set 
    # r1 r2 and r3 are the classes
    a = r1.addr()
    b = r2.addr()
    c = r3.addr()
    return "00000" + "00" + a + b + c


    # if overflow-----flag(1,0,0,0)
    # pass
    #if not overflows----flag(0,0,0,0)
# to print the opcode

def Subtraction(r1, r2, r3):  #Performs reg1 = reg2- reg3. In case reg3> reg2, 0 is written to reg1 and overflow flag is set. 
    # r1 r2 and r3 are the classes
    a = r1.addr()
    b = r2.addr()
    c = r3.addr()
    return "00001" + "00" + a + b + c
    
    # pass

def Move_Immediate(r1, x): #Performs reg1 = $Imm where Imm is a 8 bit value.
    # x is int
    bnr = bin(x)
    bnr = bnr.replace('0b','')
    while len(bnr)<8:
        bnr = "0" + bnr

    a = r1.addr()

    return "00010" + a + bnr

def Move_Register(r1, r2):
    #r1 and r2 are the classes 
    a = r1.addr()
    b = r2.addr()
    # call flag here

    return "00011" + "00000" + a + b

def Load(r1, mem):
    a = r1.addr()
    # mem is 8 bit string

    return "00100" + a + mem

def Store(r1, mem):
    a = r1.addr()
    # mem is 8 bit string

    return "00101" + a + mem

def Multiply(r1, r2, r3):
    # r1 r2 and r3 are the classes
    a = r1.addr()
    b = r2.addr()
    c = r3.addr()
    return "00110" + "00" + a + b + c
            


def Divide(r3, r4):
    a = r3.addr()
    b = r4.addr()
    return "00111" + "00000" + a + b



def Right_Shift(r1, x):
    # x is int
    bnr = bin(x)
    bnr = bnr.replace('0b','')
    while len(bnr)<8:
        bnr = "0" + bnr

    a = r1.addr()

    return "01000" + a + bnr
   


def Left_Shift(r1, x):
    # x is int
    bnr = bin(x)
    bnr = bnr.replace('0b','')
    while len(bnr)<8:
        bnr = "0" + bnr

    a = r1.addr()

    return "01001" + a + bnr


def XOR(r1, r2, r3):
    # r1 r2 and r3 are the classes
    a = r1.addr()
    b = r2.addr()
    c = r3.addr()
    return "01010" + "00" + a + b + c
            
def OR(r1, r2, r3):
    # r1 r2 and r3 are the classes
    a = r1.addr()
    b = r2.addr()
    c = r3.addr()
    return "01011" + "00" + a + b + c
        

def AND(r1, r2, r3):
    # r1 r2 and r3 are the classes
    a = r1.addr()
    b = r2.addr()
    c = r3.addr()
    return "01100" + "00" + a + b + c 
    

def Invert(r1, r2):
    a = r1.addr()
    b = r2.addr()
    return "01101" + "00000" + a + b

def Compare(r1, r2):
    #r1 and r2 are the classes 
    a = r1.addr()
    b = r2.addr()
    # call flag here

    return "01110" + "00000" + a + b
    

def Unconditional_Jump(mem):
    # mem is a string of size 8 
    # if len(mem)!=8:
    #     error
    return "01111" + "000" + mem
    

def Jump_if_Less_Than(mem):
    # if len(mem)!=8:
    #     error
    return "10000" + "000" + mem

def Jump_if_Greater_Than(mem):
    # if len(mem)!=8:
    #     error
    return "10001" + "000" + mem

def Jump_if_Equal(mem):
    # if len(mem)!=8:
    #     error
    return "10010" + "000" + mem

def Halt():
    return "1001100000000000"
    

# def Flag(v, l, g, e):
#     pass
'''main
input 
mul r1 r2 r3
  if list[0]==Multiply:
      mul()
add r1 r2 r3 
 if list[0]== Addition:
     add()

l=[0,1,2,3,4,5,6,7,8,9......,19]
input
list=[]
split().
if list[0] not in l:
    error()


for varible:
    list of inputs:
    after last element first Variable
    variable=8 bit binary 

    x value 10
    x memory adress 7 (list last index+1)
    hlt 6 line '''

R0 = Register("000")
R1 = Register("001")
R2 = Register("010")
R3 = Register("011")
R4 = Register("100")
R5 = Register("101")
R6 = Register("110")
FLAGS = Register("111")

