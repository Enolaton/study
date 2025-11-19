def solution(dots):
    answer = 0
    dots_list = [[0 for _ in range(2)] for _ in range(3)]
    for i in range(1,4):
        dots_list[i-1] = dots[i][0]-dots[0][0],dots[i][1]-dots[0][1]

    for j in dots_list:
        answer += abs(j[0]*j[1])
    return answer