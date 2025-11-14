def solution(balls, share):
    answer = 0
    a = 1
    b = 1 
    c = 1
    for i in range(balls,1,-1):
        a *= i
    print(a)
    for j in range(share,1,-1):
        b *= j
    for k in range(balls-share,1,-1):
        c *= k
    print(b)
    answer =  a//(b*c)
    return answer