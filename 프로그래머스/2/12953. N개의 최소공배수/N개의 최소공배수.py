import math

def solution(arr):
    answer = 1
    for n in arr:
        answer = (answer*n)//math.gcd(answer,n)
    return answer