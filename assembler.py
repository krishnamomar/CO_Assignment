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
   def dtb(num): 
        num=int(num)
        bnr = bin(num)
        bnr=bnr.replace('0b','')
        x = bnr[::-1] #this reverses an array
        while len(x) < 8:
            x += '0'
        bnr = x[::-1]
        #print((bnr))
        return(bnr)

    #print(dtb(5))
    lst=['rs R2 $25']

    for a in range(0,len(lst)):
        line=lst[a].split(' ')
        if line[0]=='rs':
            ele1='01000'
            printflag=1
            for i in range(0,8):
                if line[1]=='R'+'0' or line[1]=='R'+'1' or line[1]=='R'+'2' or line[1]=='R'+'3' or line[1]=='R'+'4' or line[1]=='R'+'5' or line[1]=='R'+'6':   #checking value of 1st registor
                    if i==0:
                        ele2='000'
                    elif i==1:
                        ele2='001'
                    if i==2:
                        ele2='010'
                    if i==3:
                        ele2='011'
                    if i==4:
                        ele2='100'
                    if i==5:
                        ele2='101'
                    if i==6:
                        ele2='110'
                    
                else:
                    
                    print('Error')
                    printflag-=1
                    break
            if (line[2][1:]).isdigit():
                ele3=dtb(line[2][1:])    #binary conversion of 25
            else:
                print('error')
                printflag-=1
                break
            
            if printflag==1:
                return(ele1+ele2+ele3)
    
    


def Left_Shift(r1, x):
    def dtb(num): 
        num=int(num)
        bnr = bin(num)
        bnr=bnr.replace('0b','')
        x = bnr[::-1] #this reverses an array
        while len(x) < 8:
            x += '0'
        bnr = x[::-1]
        #print((bnr))
        return(bnr)

    #print(dtb(5))
    lst=['ls R2 $25']

    for a in range(0,len(lst)):
        line=lst[a].split(' ')
        if line[0]=='ls':
            ele1='01001'
            printflag=1
            for i in range(0,8):
                if line[1]=='R'+'0' or line[1]=='R'+'1' or line[1]=='R'+'2' or line[1]=='R'+'3' or line[1]=='R'+'4' or line[1]=='R'+'5' or line[1]=='R'+'6':   #checking value of 1st registor
                    if i==0:
                        ele2='000'
                    elif i==1:
                        ele2='001'
                    if i==2:
                        ele2='010'
                    if i==3:
                        ele2='011'
                    if i==4:
                        ele2='100'
                    if i==5:
                        ele2='101'
                    if i==6:
                        ele2='110'
                    
                else:
                    
                    print('Error')
                    printflag-=1
                    break
            if (line[2][1:]).isdigit():
                ele3=dtb(line[2][1:])    #binary conversion of 25
            else:
                print('error')
                printflag-=1
                break
            
            if printflag==1:
                return(ele1+ele2+ele3)


def XOR(r1, r2, r3):
    lst=['xor R3 R1 R2']

    for a in range(0,len(lst)):
        line=list(lst[a].split(' '))
        if line[0]=='xor':
            ele1='01010'+'00'
            printflag=1
            for i in range(0,7):
                if line[1]=='R'+'0' or line[1]=='R'+'1' or line[1]=='R'+'2' or line[1]=='R'+'3' or line[1]=='R'+'4' or line[1]=='R'+'5' or line[1]=='R'+'6':   #checking value of 1st registor
                    if i==0:
                        ele2='000'
                    elif i==1:
                        ele2='001'
                    elif i==2:
                        ele2='010'
                    elif i==3:
                        ele2='011'
                    if i==4:
                        ele2='100'
                    if i==5:
                        ele2='101'
                    if i==6:
                        ele2='110'
                else:
                    print('Error')
                    printflag-=1
                    break
                    
                    
                
                if line[2]=='R'+'0' or line[2]=='R'+'1' or line[2]=='R'+'2' or line[2]=='R'+'3' or line[2]=='R'+'4' or line[2]=='R'+'5' or line[2]=='R'+'6':    #checking the value of 2nd registor
                    if i==0:
                        ele3='000'
                    if i==1:
                        ele3='001'
                    if i==2:
                        ele3='010'
                    if i==3:
                        ele3='011'
                    if i==4:
                        ele3='100'
                    if i==5:
                        ele3='101'
                    if i==6:
                        ele3='110'
                else:
                    print('Error')
                    printflag-=1
                    break
                    
                        
                if line[3]=='R'+'0' or line[3]=='R'+'1' or line[3]=='R'+'2' or line[3]=='R'+'3' or line[3]=='R'+'4' or line[3]=='R'+'5' or line[3]=='R'+'6':    #checking the value of 3rd registor
                    if i==0:
                        ele4='000'
                    if i==1:
                        ele4='001'
                    if i==2:
                        ele4='010'
                    if i==3:
                        ele4='011'
                    if i==4:
                        ele4='100'
                    if i==5:
                        ele4='101'
                    if i==6:
                        ele4='110'
                else:
                        print('Error')
                        printflag-=1
                        break
                        
            #print(printflag)            
            if printflag==1 :               
                return(ele1+ele2+ele3+ele4)
            


def OR(r1, r2, r3):
    lst=['or R3 R1 R2']

    for a in range(0,len(lst)):
        line=lst[a].split(' ')
        if line[0]=='or':
            ele1='01011'+'00'
            printflag=1
            for i in range(0,7):
                if line[1]=='R'+'0' or line[1]=='R'+'1' or line[1]=='R'+'2' or line[1]=='R'+'3' or line[1]=='R'+'4' or line[1]=='R'+'5' or line[1]=='R'+'6':   #checking value of 1st registor
                    if i==0:
                        ele2='000'
                    elif i==1:
                        ele2='001'
                    elif i==2:
                        ele2='010'
                    elif i==3:
                        ele2='011'
                    if i==4:
                        ele2='100'
                    if i==5:
                        ele2='101'
                    if i==6:
                        ele2='110'
                else:
                    print('Error')
                    printflag-=1
                    break
                    
                    
                
                if line[2]=='R'+'0' or line[2]=='R'+'1' or line[2]=='R'+'2' or line[2]=='R'+'3' or line[2]=='R'+'4' or line[2]=='R'+'5' or line[2]=='R'+'6':    #checking the value of 2nd registor
                    if i==0:
                        ele3='000'
                    if i==1:
                        ele3='001'
                    if i==2:
                        ele3='010'
                    if i==3:
                        ele3='011'
                    if i==4:
                        ele3='100'
                    if i==5:
                        ele3='101'
                    if i==6:
                        ele3='110'
                else:
                    print('Error')
                    printflag-=1
                    break
                    
                        
                if line[3]=='R'+'0' or line[3]=='R'+'1' or line[3]=='R'+'2' or line[3]=='R'+'3' or line[3]=='R'+'4' or line[3]=='R'+'5' or line[3]=='R'+'6':    #checking the value of 3rd registor
                    if i==0:
                        ele4='000'
                    if i==1:
                        ele4='001'
                    if i==2:
                        ele4='010'
                    if i==3:
                        ele4='011'
                    if i==4:
                        ele4='100'
                    if i==5:
                        ele4='101'
                    if i==6:
                        ele4='110'
                else:
                        print('Error')
                        printflag-=1
                        break
                        
            #print(printflag)            
            if printflag==1 :               
                return(ele1+ele2+ele3+ele4)
        


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
