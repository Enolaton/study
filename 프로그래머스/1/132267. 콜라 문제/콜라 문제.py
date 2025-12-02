def solution(a, b, n):
    answer = 0
    return_cola = 0
    q = 0 # 몫(quotient)
    r = 0 # 나머지(remainder)

    while n >= a:
        r = n % a
        q = n // a
        return_cola = q*b
        n = return_cola + r
        n = return_cola + r
        answer += return_cola
    answer += (r+return_cola)//a
    return answer