def solution(n):
    answer = 0
    f_list = [0,1,1]
    for _ in range(n - 2):
        f_list.append(f_list[-1]+f_list[-2])
    answer = f_list[-1]
    return answer%1234567