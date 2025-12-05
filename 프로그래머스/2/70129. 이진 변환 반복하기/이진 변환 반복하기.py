def solution(s):
    answer = []
    zero_cnt = 0
    binary_cnt = 0
    
    while len(s) > 1:
        new_s = []
        for check in s:
            if check == '0':
                zero_cnt += 1
            else:
                new_s.append(check)
        s = bin(len(new_s))[2:]
        binary_cnt += 1
    return [binary_cnt,zero_cnt]