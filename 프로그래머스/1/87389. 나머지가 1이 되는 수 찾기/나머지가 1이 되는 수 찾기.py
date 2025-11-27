def solution(n):
    answer = 0
    a = []
    for i in range(2,n):
        if (n-1)%i == 0:
            a.append(i)
    answer = min(a)
    return answer