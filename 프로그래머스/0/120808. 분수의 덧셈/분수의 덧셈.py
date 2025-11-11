def solution(numer1, denom1, numer2, denom2):
    answer = []
    answer.append(numer1*denom2+denom1*numer2) # 새로운 분수의 분자
    answer.append(denom1*denom2) # 새로운 분수의 분모
    print(answer)
    for i in range(1,1000000):
        if answer[0] % i == 0 and answer[1] % i == 0: # 분자와 분모가 약분이 된다면,
            max = i # 최대 공약수
    answer[0] = answer[0]/max
    answer[1] = answer[1]/max
    return answer
