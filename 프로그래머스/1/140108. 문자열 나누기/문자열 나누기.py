def solution(s):
    answer = 0
    text = s[0]
    s = list(s)
    s_list = [text]
    
    while s:
        c, not_c = 1, 0
        for i in s[1:]:
            if c == not_c:
                break
            elif i == s[0]:
                c+=1
            else:
                not_c += 1
        s_list.append(s[:c+not_c])
        s = s[c+not_c:]
    answer = len(s_list)-1
    return answer