# Neural Network
## 신경망이란?
Input layer, Hidden layer 그리고 Output layer를 가진다.  
중간의 hidden layer이 추가된 것이 퍼셉트론과의 차이점.  

# Activation function
말그래도 입력 신호들에 가중치를 곱해 더한 값이 활성화를 일으키는지 여부를 결정한다.  
사실 퍼셉트론에서도 존재하며, 두 단계로 분리한다 생각하면 된다.  
예를 들어, 퍼셉트론에서는 주로 아래와 같은 식을 사용했다. 
```
	0 (w1x1+w2x2+b <= 0)
y =
	1 (w1x1+w2x2+b > 0)
```
이를 두개로 분리하면, 
```
a = w1x1+w2x2+b,
y = h(a),
		1 (x<=0)
h(x) = 
		0 (x>0)
```
위와 같이 나눌 수 있다.   
여기서, h(x)가 바로 활성화 함수, activation function이다.  
다른 활성화 함수를 퍼셉트론에서 사용하면 바로 신경망으로 나아갈 수 있다. 

## Sigmoid function
가장 자주 사용하는 활성화 함수인 시그모이드 함수이다.  
파이썬으로 구현하면, 
```python
def sigmoid(x):
	y = 1 / (1 + np.exp(-x))
```
위의 함수는 파라미터가 넘파이 배열이여도 문제없이 돌아간다(브로드캐스팅).  
시그모이드 함수를 실제로 그려보면 0에서 1사이의 값을 가지는 S자 모양의 함수가 나온다.  

## Step function 
단층 퍼셉트론에서 사용한 함수로, 임계값을 기준으로 출력이 바뀌는 함수.  

# Reference
밑바닥부터 시작하는 딥러닝(Deep Learning from Scratch)
