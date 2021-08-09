class Register:
    def __init__(self):
        self.value = "";

class Variable:
    def __init__(self, name):
        self.value = 0;
        self.name = name;

def Addition(r1, r2, r3):
    pass
# to print the opcode

def Subtraction(r1, r2, r3):
    pass

def Move_Immediate(r1, x):
    #x is int
    pass

def Move_Register(r1, r2):
    pass

def Load(r1, mem):
    # mem is memory address
    pass

def Store(r1, mem):
    pass

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
