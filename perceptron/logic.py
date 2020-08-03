import numpy as np
class logic:
    def __init__(self):
        print("initialized")
    def AND(self,x1,x2):
        x = np.array([x1, x2])
        w = np.array([0.5, 0.5])
        b = -0.7
        tmp = np.sum(x*w)+b
        if(tmp<=0):
            return 0
        else:
            return 1
    def OR(self,x1,x2):
        x = np.array([x1, x2])
        w = np.array([1.0, 1.0])
        b = -0.1
        tmp = np.sum(x*w)+b
        if(tmp<=0):
            return 0
        else:
            return 1
    def NAND(self, x1, x2):
        x = np.array([x1, x2])
        w = np.array([-0.5, -0.5]) #Difference is the weight with AND gate
        b = 0.7 
        tmp = np.sum(x*w)+b
        if(tmp<=0):
            return 0
        else:
            return 1
def XOR(l,x1, x2):
    s1 = l.NAND(x1, x2)
    s2 = l.OR(x1, x2)
    return l.AND(s1, s2)
l = logic()
print("AND 0,1: " + str(l.AND(0,1)))
print("AND 1,1: " + str(l.AND(1,1)))
print("OR 0,0: " + str(l.OR(0,0)))
print("OR 1,0: " + str(l.OR(1,0)))
print("NAND 0,0: " + str(l.NAND(0,0)))
print("NAND 0,1: " + str(l.NAND(0,1)))
print("XOR 0,0: " + str(XOR(l,0,0)))#Even passing instance available?
print("XOR 1,0: " + str(XOR(l,1,0)))
