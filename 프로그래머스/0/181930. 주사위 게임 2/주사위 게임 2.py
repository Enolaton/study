def solution(a, b, c):
    answer = 1
    if a == b:
        if b == c:
            # a=b=c 
            for i in range(1,4):
                answer *= (a**i + b**i + c**i)
        else:
            # a=b != c
            for i in range(1,3):
                answer *= (a**i + b**i + c**i)
    elif a == c:
        if a != b:
            for i in range(1,3):
                answer *= (a**i + b**i + c**i)
    elif a != b:
        if b == c:
            for i in range(1,3):
                answer *= (a**i + b**i + c**i)
        else:
            answer = a+b+c
    return answer