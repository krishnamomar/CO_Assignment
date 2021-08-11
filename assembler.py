class Register:
    def __init__(self):
        self.value = "";

class Variable:
    def __init__(self, name):
        self.value = 0;
        self.name = name;

def Addition(r1, r2, r3): #Performs reg1 = reg2+ reg3. If the computation overflows, then the overflow flag is set 
    a="00000"
    b="00"
    c="001"
    d="010"
    e="011"
    f=a+b+c+d+e
    return f


    # if overflow-----flag(1,0,0,0)
    # pass
    #if not overflows----flag(0,0,0,0)
# to print the opcode

def Subtraction(r1, r2, r3):  #Performs reg1 = reg2- reg3. In case reg3> reg2, 0 is written to reg1 and overflow flag is set. 
    # if r3>r2:
        # r1=0
        #overflow----flag(1,0,0,0)
    # r1=r2-r3
    a="00001"
    b="00"
    c="001"
    d="010"
    e="011"
    f=a+b+c+d+e
    return f
    
    # pass

def Move_Immediate(r1, x): #Performs reg1 = $Imm where Imm is a 8 bit value.
    # r1=x
    #x is int
    a="00010"
    # b="00"
    b="001"
    # d="010"
    # e="011"
    c=x
    # f=a+b+c+d+e
    f=a+b
    return f

    # pass

def Move_Register(r1, r2):
    # r1=r2
    a="00011"
    b="00000"
    c="001"
    d="010"
    # e="011"
    f=a+b+c+d
    return f
    # pass

def Load(r1, mem):
    # mem is memory address
    #load value at address mem to r1
    a="00100"
    # b="00"
    b="001"
    # d="010"
    # e="011"
    c=mem
    f=a+b+c
    return f
    # pass

def Store(r1, mem):
    #Stores data from reg1 to mem_addr.
    a="00101"
    # b="00"
    b="001"
    # d="010"
    # e="011"
    c=mem
    f=a+b+c
    return f
    # pass

def Multiply(r1, r2, r3):
    pass

def Divide(r3, r4):
    # quotent in r0 
    # remainder in r1
    pass

def Right_Shift(r1, x):
    #x is int
    pass

def Left_Shift(r1, x):
    pass

def XOR(r1, r2, r3):
    pass

def OR(r1, r2, r3):
    pass

def AND(r1, r2, r3):
    pass

def Invert(r1, r2):
    pass

def Compare(r1, r2):
    pass

def Unconditional_Jump(mem):
    pass

def Jump_if_Less_Than(mem):
    pass

def Jump_if_Greater_Than(mem):
    pass

def Jump_if_Equal(mem):
    pass

def Halt():
    pass

# def Flag(v, l, g, e):
#     pass
