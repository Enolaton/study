def solution(s):
    answer = True
    check = list(s)
    check_num = 0
    if s.count('(') == s.count(')'):
        if s[-1] == '(':
            answer = False
    else:
         answer = False 
    for c in s:
        if c == '(':
            check_num += 1
        else:
            check_num -= 1
        if check_num < 0:
            answer = False
            break

    return answer