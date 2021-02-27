#-*-coding:utf-8-*-
import sys, os
sys.path.append("../../")
#originally sys.path.append(os.pardir) 
from dataset.mnist import load_mnist

(x_train, t_train), (x_test, t_test) = load_mnist(flatten=True, normalize = False)

print(x_train.shape) #(60000, 784) -> 60,000 images with 28x28 pixels
print(t_train.shape)

