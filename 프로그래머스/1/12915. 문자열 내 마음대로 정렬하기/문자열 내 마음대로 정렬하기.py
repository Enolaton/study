def solution(strings, n):
    answer = []
    c_list = [] # 인덱스 문자를 담을 리스트
    s_list = [] # 인덱스 문자로 비교한 순서를 strings와 매칭하여 담을 리스트
    
    for s in strings:
        c_list.append(s[n])
    for s_out in zip(c_list, strings):
        s_list.append(s_out)
    s_list = sorted(s_list)
    for i in range(len(s_list)):
        answer.append(s_list[i][1])
    return answer