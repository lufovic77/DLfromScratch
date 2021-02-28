import numpy as np
import sys, os
sys.path.append(os.pardir)
from dataset.mnist import load_mnist
from module import predict, init_network

def CEE1(y, t): # one-hot encoding이 True인 경우. 즉, 정답만 1로 표시된다. 
    if y.ndim==1: # 배치가 아니라 데이터가 하나여도 괜찮게 처리함
        t = t.reshape(1, t.size)
        y = y.reshape(1, y.size)
    batch_size = y.shape[0]
    return -np.sum(t*np.log(y+1e-7)) / batch_size
        
def CEE2(y, t): # one-hot encoding이 False인 경우. 각 레이블이 값을 유지하되, 정답이 가장 높음. 
    if y.ndim==1:
        t = t.reshape(1, t.size)
        y = y.reshape(1, y.size)
    batch_size = y.shape[0]
    return -np.sum(np.log(y[np.arange(batch_size), t]+1e-7)) / batch_size
"""
y[np.arange(batch_size), t] 이게 무엇을 의미할까?
np.arange(batch_size)는 0~batch_size-1까지의 배열을 생성. [0,1,...,batch_size-1]
t는 정답의 인덱스를 담고 있다. 
즉,[y[0, t[0]], y[1, t[1]], ...,y[batch_size-1, t[batch_size-1]]] 요런 배열을 만들어낸다. 
해석하자면, 정답 레이블을 추론한 값을 반환하는 배열이다. 
"""

network = init_network()
(x_train, t_train), (x_test, t_test) = \
        load_mnist(True, True, True)

#한번 미니배치 학습을 해보자. 그냥 데이터 중에서 무작위로 뽑아내면 된다. (np.random.choice)
train_size = x_train.shape[0] #x_train.shape: (60000,784)
batch_size = 10
batch_mask = np.random.choice(train_size, batch_size) #0~train_size-1에서 batch_size 개수 만큼의 인덱스를 뽑음
x_batch = x_train[batch_mask]
t_batch = t_train[batch_mask]
y = predict(network, x_batch)
print(CEE1(y, t_batch))

(x_train, t_train), (x_test, t_test) = \
        load_mnist(True, True, False)

train_size = x_train.shape[0] #x_train.shape: (60000,784)
batch_size = 10
batch_mask = np.random.choice(train_size, batch_size) 
x_batch = x_train[batch_mask]
t_batch = t_train[batch_mask]
y = predict(network,x_batch)
print(CEE2(y, t_batch))
