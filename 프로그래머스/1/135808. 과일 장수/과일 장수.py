def solution(k, m, score):
    answer = 0
    tmp = 0
    score_list =[]
    while k > 0:
        if (score.count(k)+tmp)//m == 0:
            tmp += score.count(k)%m
        else:
            answer += ((score.count(k)+tmp)//m)*m*k
            tmp = (score.count(k)+tmp)%m
        k -= 1
    return answer