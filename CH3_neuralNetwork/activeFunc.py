import numpy as np
class activation:
    def __init__(self):
        print("initialized")
    def stepVer1(self, x):#Only with scalar 
        if(x>0):
            return 1
        else:
            return 0
    def stepVer2(self, x):
        y = x>0#bool numpy array
        return y.astype(np.int)#Convert to int array
    def sigmoid(self, x):
        return 1 / (1+np.exp(-x))
    def ReLu(self, x):
        return np.maximum(0, x)
class Softmax:
    def __init__(self):
        print("init")
    def noSoftmax(self, arr):
        exp = np.exp(arr)
        exp_sum = np.sum(exp)
        return exp/exp_sum
    def softmax(self, arr):
        arr_max = np.max(arr) #overflow
        arr -= arr_max
        exp = np.exp(arr)
        exp_sum = np.sum(exp)
        return exp/exp_sum
soft = Softmax()
tmp = np.arange(1, 2, 0.1)
print(tmp)
print(soft.softmax(tmp))
print(np.sum(soft.softmax(tmp)))

A = activation()
x = np.arange(-3.0, 3.0, 0.5)
print("step func: ")
print(A.stepVer2(x))
print("sigmoid: " )
print(A.sigmoid(x))
