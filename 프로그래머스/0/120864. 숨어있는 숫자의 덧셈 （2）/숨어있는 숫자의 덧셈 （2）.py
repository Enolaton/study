def solution(my_string):
    answer = 0
    cnt = 0

    for i in range(1,len(my_string)+1):
        if ord(my_string[-i]) < 65:
            answer += int(my_string[-i])*10**cnt
            cnt += 1
        else:
            cnt = 0
    return answer