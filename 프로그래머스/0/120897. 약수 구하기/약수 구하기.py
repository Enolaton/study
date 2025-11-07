def solution(n):
    answer = []
    # 1부터 n까지
    for i in range(1,n+1):
        if n%i == 0: # 입력값 n을 반복값i로 나누었을 때 나머지가 없으면, i는 n의 약수
            answer.append(i) # 리스트에 i 추가
    return answer # 리스트 반환