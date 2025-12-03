def solution(n):
    answer = 0
    cal = []
    cnt = 0
    for i in range(18):
        if 3 ** i > n:
            cnt = i
            break
    for j in range(cnt-1,-1,-1):
        cal.append(n//(3**j))
        n = n%(3**j)

    for k in range(len(cal)-1,-1,-1):
        answer += cal[k]*(3**k)
    return answer