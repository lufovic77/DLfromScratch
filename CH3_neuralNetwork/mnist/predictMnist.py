# coding: utf-8
import sys, os
import pickle
sys.path.append("../../")
sys.path.append("../")
import numpy as np
from dataset.mnist import load_mnist
from activeFunc import sigmoid, softmax
def get_data():
    (x_train, t_train), (x_test, t_test) = \
            load_mnist(flatten = True, normalize = True, one_hot_label = False)
    #train: literally training data
    #x: image info. pixel value
    #t: label. answer. 
    return x_test, t_test
def init_network():
    with open("sample_weight.pkl", 'rb') as f: #contains the weigth and bias
        network = pickle.load(f)
    return network

def predict(network, x):
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3'] 
    # 3 Layers
    #784 -> sigmoid -> 50 -> sigmoid -> 100 -> softmax -> 10 (10 figures)
    #X      W1      W2      W3      Y
    #784 ->784X50->50X100->100X10->10(10 figures)
    #X means the input. Just one image. The other code below shows the input with batch. 
    a1 = np.dot(x, W1) + b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2, W3) + b3
    z3 = softmax(a3)

    return z3

x, t = get_data()
network = init_network()

accuracy_cnt = 0
for i in range(len(x)): #each image, predice the accuracy
    y = predict(network, x[i])
    p = np.argmax(y) #pick highest index
    if p == t[i]: #if it's correct
        accuracy_cnt +=1
print("Accuracy:" + str(float(accuracy_cnt)/len(x)))
"""
TILL HERE FOR JUST ONE IMAGE. BELOW SHOWS THE BATCH INPUT. 
"""

batch_size = 100
accuracy_cnt = 0

for i in range(0, len(x), batch_size): #increasing interval: batch size. range(start, end, step): start~end-1, increasing step
    x_batch = x[i:i+batch_size]
    y_batch = predict(network, x_batch) #y_batch는 100x10 형상임. 
    p = np.argmax(y_batch, axis=1) #axis=1은 1차원, 즉 100x10중 10에서 최대값의 인덱스를 반환. 어떤 레이블이 가장 답과 가까운지를 뽑아낸다고 생각하면 된다. (어떤 숫자)
    accuracy_cnt += np.sum(p == t[i:i+batch_size]) #t는 정답이고 p는 신경망이 추론한 결과 
print("Accuracy:" + str(float(accuracy_cnt)/len(x)))

