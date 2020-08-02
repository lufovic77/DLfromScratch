# Numpy array
1차원 배열을 vector로 지칭한다.
```python
x = np.array([1.0, 2.0, 3.0])
print(x)
```
## Numpy array arithmetic
같은 수의 원소를 가진 배열은 element-wise 연산을 수행한다. 
```python
x = np.array([1, 2, 3])
y = np.array([2, 4, 6]) 
print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x/2) #Broadcast
```

## Numpy N-dimensional array
```python
A = np.array([[1,2],[3,4]]) #matrix
print(A)
print(A.shape)
B = np.array([[3,0], [0,6]])
print(A+B) #Also element-wise. Only between identical shape
print(A*10) #Array with scalar(broadcasting)
```
그렇다면, 원소의 개수를 안맞춰도 되나? 
```python
np.array([[1,2], [1,2,3,4]]) 
```
이런식의 선언은 되긴 하지만, 우리가 원하는 2x2 행렬같은 타입이 아니라,  
그냥 리스트를 두개 담은 오브젝트가 선언된다. 

## Broadcasting
브로드캐스팅이란 아주 좋은 연산 방법이 존재한다.  
주로 스칼라 값을 행렬에 대해 연산하는 경우 자동으로 적용.  
자동적으로 둘의 형상(shape)를 동일하게 만든다.  
```python
A = np.array([[1,2], [3,4]])
A = A * 10
```
위의 경우, 10이라는 스칼라 값은 2x2 행렬로 자동으로 확장됨.  
아래와 같은 경우도 마찬가지고, 2x1을 2x2로 자동으로 확장.
```python
A = np.array([[1,2], [3,4]])
B = np.array([10,20])
print(A*B) 
# array([[10, 30],
		[30, 80]])
```
