import numpy as np
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
