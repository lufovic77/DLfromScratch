# 학습 
학습이란, 주어진 데이터를 이용해서 최적의 매개변수 값을 찾아가는 과정이다.  
__최적__ 의 의미는?   
Loss Function를 최소화 하는 값이다.  
이에 관해서는 아래서 알아봄.  
간단하게 이해하면, 손실이 적으면 정확도는 높을 것.  
## 데이터
앞에서 정리한 퍼셉트론의 경우 가중치 값을 사람이 직접 정함.   
지금부터는, 주어진 training data를 통해 스스로 정해간다.   
- Training Data  
- Test Data   

우선, 훈련 데이터를 이용해 가중치를 수정해 나가고,  
얼마나 잘 학습한지를 테스트 데이터를 이용해 평가한다.   
다만, 특정 훈련 데이터 셋에 너무 최적화되어 다른 데이터 셋은 못 맞추는  
현상이 발생 가능하며, 이를 오버피팅(Overfitting)이라고 한다.  
# Loss Function(Cost Function)
