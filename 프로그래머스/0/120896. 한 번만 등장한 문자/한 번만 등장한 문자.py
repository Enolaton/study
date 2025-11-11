def solution(s):
    answer = ''
    s_list = list(s)
    d_list = []
    for _ in s_list:
        if s_list.count(_) == 1:
            d_list.append(_)
    d_list = sorted(d_list)
    return ''.join(d_list)