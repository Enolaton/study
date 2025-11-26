def solution(dots):
    answer = 0
    x_list, y_list  = [], []
    a_list=[0,0,0,0,0,0]
    for i in range(len(dots)):
        for j in range(i+1, len(dots)):
            x_list.append(dots[j][0] - dots[i][0])
            y_list.append(dots[j][1] - dots[i][1])
    for k in range(len(x_list)):
        a_list[k] = y_list[k]/x_list[k]
    if  a_list[0] == a_list[4] or a_list[0] == a_list[5]:
        answer = 1
    elif a_list[4] == a_list[2] or a_list[4] == a_list[1]:
        answer = 1
    return answer