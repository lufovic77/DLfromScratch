# coding: utf-8
import sys, os
import pickle
sys.path.append("../CH3_neuralNetwork")
sys.path.append("../")
import numpy as np
from dataset.mnist import load_mnist
from activeFunc import sigmoid, softmax
def get_data(f, n, o):
    (x_train, t_train), (x_test, t_test) = \
            load_mnist(flatten = f, normalize = n, one_hot_label = o)
    #train: literally training data
    #x: image info. pixel value
    #t: label. answer. 
    return x_train, t_train, x_test, t_test
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
