import numpy as np
def SSE(y, t): #오차 제곱합(sum_square_error)
    return 0.5*np.sum((y-t)**2) #y와 t를 스칼라 값이 아니라 넘파이 배열로 쓸 수 있다는게 큰 장점
def CEE(y, t): #교차 엔트로피 오차(cross_entropy_error)
    delta = 1e-7
    return -np.sum(t*np.log(y+delta)) #로그가 0이 되는걸 막기 위해서 아주 작을 값인 delta를 더해줌. 
    #어차피 정답만 t가 1임. 즉 결국 정답에 대한 추정값(y)의 자연로그를 구하는 것.
