def solution(numlist, n):
    n_list = []
    for i in range(len(numlist)):
        n_list.append([abs(numlist[i]-n),numlist[i]])
    n_list.sort()
    answer = [n_list[0][1]]
    for j in range(1,len(n_list)):
        for k in range(j+1, len(n_list)):
            if n_list[j][0] == n_list[k][0]:
                answer.append(n_list[k][1])
        answer.append(n_list[j][1])
    result = []
    for num in answer:
        if num not in result:
            result.append(num) # 중복값 제거
    return result