import sys, os
sys.path.append("../../")
import numpy as np
from dataset.mnist import load_mnist
from PIL import Image

def img_show(img):
    pil_img = Image.fromarray(np.uint8(img))
    pil_img.show

def user_show(img):
#Simple user-defined image showing. 
#Due to limits of ssh image showing.
    for i in range(0, 28):
        for j in range(0, 28):
            if(img[i][j]>0):
                print(1, end='')
            else:
                print(0, end='')
        print()
(x_train, t_train), (x_test, t_test) = load_mnist(flatten = True, normalize = False)
# flatten = True -> 1dimensional array 

img = x_train[0]
label = t_train[0]
print(label)

img = img.reshape(28, 28) # convert it to 2 dimension array again
user_show(img)

#img_show(img)
