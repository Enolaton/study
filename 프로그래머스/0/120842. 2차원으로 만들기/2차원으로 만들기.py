def solution(num_list, n):
    l = len(num_list)//n
    answer = [ [ 0 for _ in range(n)] for _ in range(l) ]
    for i in range(l):
        for j in range(n):
            answer[i][j] += num_list.pop(0)
    return answer