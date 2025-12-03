def solution(d, budget):
    answer = 0
    office = 0
    d = sorted(d)

    while office < budget:
        # 부서 요청 금액의 합 <= 예산액
        if sum(d) <= budget:
            answer = len(d)
            break
        # 각 부서 요청 금액 접근
        for _ in d:
            office += _
            # 요청 금액을 처리했을 때, 예산을 초과하는 경우
            if office > budget:
                break
            answer += 1
        break
    return answer