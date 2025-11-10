def solution(n):
    answer = 0
    for i in range(2,n+1):
        for j in range(2,i):
            if i%j == 0: # 2부터 i까지 약수가 있다면 -> 합성수
                answer+=1
                break
    return answer