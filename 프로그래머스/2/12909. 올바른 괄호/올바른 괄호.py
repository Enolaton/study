def solution(s):
    answer = True
    check = list(s)
    check_num = 0
    
    # 왼쪽 괄호의 수와 오른쪽 괄호의 수의 개수를 비교
    if s.count('(') == s.count(')'):
        # 여는 괄호로 끝날 경우 false
        if s[-1] == '(':
            answer = False
    else:
        # 여는 괄호와 닫는 괄호의 개수가 다를 경우
         answer = False 
            
    # 여는 괄호와 닫는 괄호의 수가 같아도 위치에 따라서 다를 수 있음
    # -1, 0, +1 을 사용해서 위치가 제대로 인지 판별함
    # 디지털신호 인코딩, 디코딩에서 아이디어 받음
    
    for c in s:
        if c == '(':
            check_num += 1
        else:
            check_num -= 1
        if check_num < 0:
            answer = False
            break

    return answer