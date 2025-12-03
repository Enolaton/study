def solution(k, score):
    answer = []
    score_list = []
    for day in range(1,len(score)+1):
        score_list.append(score[day-1])
        score_list = sorted(score_list)
        if day <= k:
            answer.append(score_list[0])
            continue
        answer.append(score_list[day-k])
    return answer