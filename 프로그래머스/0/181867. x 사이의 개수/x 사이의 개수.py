def solution(myString):
    answer = []
    cnt = 0
    for _ in myString:
        if _ == 'x':
            answer.append(cnt)
            cnt = 0
        else:
            cnt += 1
    answer.append(cnt)
    return answer