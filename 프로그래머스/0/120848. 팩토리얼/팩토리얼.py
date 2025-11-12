from math import factorial


def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n < factorial(i):
            answer = i-1
            break
        else:
            answer = i
    return answer