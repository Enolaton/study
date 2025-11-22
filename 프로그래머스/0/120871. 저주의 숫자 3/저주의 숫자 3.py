def solution(n):
    answer = 0
    three_cnt_list = list(range(1,n**2))
    result_list = []
    if len(three_cnt_list) == 0:
        result_list.append(n)
    for i in range(len(three_cnt_list)):
        # 3의 배수거나 숫자3을 사용하는 경우 결과 제외
        if three_cnt_list[i] % 3 != 0:
            if '3' not in str(three_cnt_list[i]):
                result_list.append(three_cnt_list[i])
    return result_list[n-1]