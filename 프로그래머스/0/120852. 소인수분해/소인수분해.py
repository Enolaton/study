def solution(n):
    answer = []
    tmp = []
    temp = []
    for i in range(2,n+1):
        if n % i == 0:
            for j in range(0,14): # 2^13 < 10000 < 2^14
                if n % (i**j) == 0:
                    n = n / (i**j)
                    print(n)
            tmp.append(i)
    answer.append(tmp[0])
    
    for _ in tmp: # 리스트 안에 배수가 포함된 경우 제거
        for j in answer:
            if _%j != 0:
                answer.append(_)

    for _ in answer: # 위 반복문에서 같은 약수가 추가된 경우 제거
        if _ not in temp:
            temp.append(_)
    return temp