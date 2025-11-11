def solution(i, j, k):
    tmp = '' # 모든 문자를 합칠 문자열
    for x in range(i, j + 1): 
        tmp = tmp + str(x) # i 부터 j까지 모든 숫자를 문자로 변환해서 tmp에 합침
    answer = tmp.count(str(k)) # 문자열에서 k가 얼마나 들어가 있는 지 계산
    return answer