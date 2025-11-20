def solution(score):
    answer = []
    score_mean = []
    # 평균 점수 리스트에 평균 점수 추가
    for i in range(len(score)):
        score_mean.append((score[i][0] + score[i][1]) / 2)
    tmp_list = score_mean
    # 평균점수 정렬
    score_mean = sorted(score_mean, reverse=True)
    print("평균점수 :", score_mean)
    # 그냥 평균 전수 리스트를 정렬하고 순위 매기면 출력에 이상이 생김
    # 따라서, 정렬 전 인덱스 번호를 주고 정렬 후 순위를 출력
    # 또한, 리스트의 키 값으로 점수를 주면, 같은 점수인 학생은 같은 순위로 출력
    ratings = {}
    rating = 0
    for j in range(len(score_mean)):
        if score_mean[j] not in ratings:
            ratings[score_mean[j]] = rating+1
            rating += 1
        else:
            rating+=1
            continue
    for k in tmp_list:
        answer.append(ratings[k])
    return answer