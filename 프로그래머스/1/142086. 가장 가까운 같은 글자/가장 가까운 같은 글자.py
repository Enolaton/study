def solution(s):
    answer = []
    s_list = list(s)
    for i in range(len(s)):
        if i == s_list.index(s[i]):
            answer.append(-1)
        else:
            answer.append(i - s_list.index(s[i]))
            s_list[s_list.index(s[i])] = ''
    return answer