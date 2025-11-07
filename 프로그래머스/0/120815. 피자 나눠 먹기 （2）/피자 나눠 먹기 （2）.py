def solution(n): # 6과 n의 최소공배수 찾기
    answer = 0
    for i in range(6,6*(n+1),6): # 피자 한판이 6조각이므로, 6조각씩 증가
        if i % n ==0: # 모두 같은 수의 피자 조각을 먹는 경우
            answer = i//6 # 피자수(n) = 피자조각수/한판당조각수
            break
        else:
            answer = i*6
    return answer