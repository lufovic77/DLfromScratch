import numpy as np
network = {}
network['W1'] = np.array([[0.1,0.3,0.5], [0.2,0.4,0.6]])
W1 = network['W1']
x = np.array([1.0,0.5])
print(np.shape(network['W1'])) #(2,3)
print(np.shape(x)) #(2,)

a1 = np.dot(x, W1)
print(np.shape(a1)) #(3,)

network['W2'] = np.array([[0.1,0.4], [0.2, 0.5], [0.3, 0.6]])
W2 = network['W2']
print(np.shape(W2)) #(3,2)
