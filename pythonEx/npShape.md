# numpy.shape() function
개인적으로 이 함수가 작동하는 방식을 이해하는데 애를 먹음.  
키 포인트는 다음 두 가지다.  
- 행렬처럼 이해하면 혼동을 준다.  
- 해당 함수는 '__튜플 수__'를 반환함에 유의하자.  

## 오해
처음 내가 한 오해는, 
```python
x = np.array([[1,2],[2,3]])
```
위 행렬의 모양이 (2,2)인건 당연히 알지.  2x2 행렬이므로.  
근데 왜 
```python
y = np.array([1,2])
```
요놈은 왜 모양이 (1,2)가 아니라 (2,) 인거냐? 1x2행렬 아님?   

이런 오해는numpy.shape() 함수에 대한 내 생각을  
(row, column)을 뱉는다고 confining한데서 나온것.  
물론, 2차원에서는 (row, column)을 적용해도 무리가 없지만,  
3차원, 4차원에서는 너무 협소한 생각이고 1차원에서는 너무 넓은 생각이다. 

## 동작 방식
그럼 작동 방식이 뭔가?  
numpy.shape()함수를 사용하려면, '__차원 수__'를 고려해야한다.  
원소의 개수는 차원 수를 의미라며, 각 원소의 값은 튜플의 개수를 의미한다.  
- 원소의 개수: 차원 수
- 각 원소 값: 튜플의 개수
그럼 위의 상황을 다시 보자.  

```python
x = np.array([[1,2],[2,3]])
y = np.array([1,2])
```
x는 2차원이므로 괄호안의 원소 개수는 2개.  
튜플 수는 2개이므로, 형상은 (2,2).   
y는 1차원이므로 괄호안의 원소 개수는 1개.   
튜플수는 2개이므로, 형상은 (2,).  
그럼 다른 여러 보기를 살펴보자.  

## 다양한 보기 
```python
# 1-dimensional
np.array([1, 2, 3]).shape #(3,)

# 2-dimensional
np.array([[1, 2, 3]]).shape #(1, 3)
np.array([[1], [2], [3]]).shape #(3, 1) 바로 위와의 차이점을 잘 보자! 튜플 수!!

# 3-dimensional
np.array([[[1, 2, 3]]]).shape #(1, 1, 3)
np.array([[[1,2],[3,4]],[[5, 6], [7, 8]]]).shape #(2, 2, 2)
```
## Reference
[Stack Overflow](https://stackoverflow.com/questions/63245509/understanding-the-shape-of-a-numpy-array, "my_question")
