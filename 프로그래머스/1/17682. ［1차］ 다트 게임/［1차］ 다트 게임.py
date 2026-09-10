def solution(dartResult):
    answer = 0
    dart = []
    dartResult = dartResult.replace('10','X')
    
    for i in dartResult:
        if i.isdigit():
            dart.append(int(i))
        elif i=='X':
            dart.append(10)
        else:
            dart.append(i)
    print(dart)
    score = dart[0]
    score_list = []
    for c in dart[1:]:
        if c=='S':
            score_list.append(score)
        elif c=='D':
            score_list.append(score**2)
        elif c=='T':
            score_list.append(score**3)
        elif c=='*':
            if len(score_list)>1:
                score1 = score_list.pop()   # score_list 마지막 요소
                score2 = score_list.pop()   # score_list 뒤에서 두번째 요소
                score_list.append(2*score2)
                score_list.append(2*score1)
            else:
                score1 = score_list.pop()
                score_list.append(2*score1)
        elif c=='#':
            score1 = score_list.pop()
            score_list.append((-1)*score1)
        else:
            score = c
        print(score_list)
    answer = sum(score_list)
    return answer