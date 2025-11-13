def solution(s):
    answer = 0
    num_list = s.split(' ') # 문자열 s를 공백을 기준으로 나눔
    new_list = []
    for i in range(len(num_list)):
        if num_list[i] == 'Z':
            new_list.pop(-1)
        else:
            new_list.append(int(num_list[i]))
    for _ in new_list:
        answer += _
    return answer