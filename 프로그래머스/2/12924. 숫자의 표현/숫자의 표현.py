def solution(n):
    answer = 0
    num_list = []
    
    for i in range(1, n+1):
        if n%i == 0:
            num_list.append(i)
    for num in num_list:
        if num%2 != 0:
            answer+=1
    return answer