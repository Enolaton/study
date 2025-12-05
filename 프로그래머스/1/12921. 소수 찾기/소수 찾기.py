def solution(n):
    answer = 0
    prime_number_list =  [ x for x in range(2,n+1)]
    for i in range(2,n+1):
        for j in range(2, int(i**(1/2))+1):
            if i%j == 0:
                answer += 1
                break
    return n - answer - 1