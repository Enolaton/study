def solution(k, tangerine):
    answer = 0
    tangerines = {}
    
    # 자연어처리에서 배운 사용된 토큰의 수를 튜플 형식으로 지정한 내용 응용
    for t in tangerine:
        tangerines[t] = tangerines.get(t, 0) + 1
    # 딕셔너리의 value 기준으로 내림차순 정렬
    sorted_tangerines = sorted(tangerines.items(), key=lambda item: item[1], reverse=True)
    
    # (한 상자에 담으려는 귤의 개수) - (개수가 많은 귤)
    for st in sorted_tangerines:
        if k <= 0:
            break
        k-=st[1]
        answer += 1
    return answer