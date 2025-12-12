def solution(s):
    answer = 0
    s_list = list(s)
    new_s_list = []
    
    for c in s_list:
        if new_s_list and new_s_list[-1] == c:
            new_s_list.pop()
        else:
            new_s_list.append(c)
            
    if not new_s_list:
        answer = 1 
    return answer