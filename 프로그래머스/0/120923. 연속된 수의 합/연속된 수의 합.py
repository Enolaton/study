def solution(num, total):
    answer = []
    setup = 0
    for i in range(1,num):
        setup += i
    start = total-setup
    result = start // num
    for k in range(result, result + num, 1):
        answer.append(k)
    return answer