def solution(brown, yellow):
    answer = []
    total = brown+yellow
    for i in range(3,total):
        # 총 격자의 개수의 약수 경우의 수 중, 조건을 만족하는 경우
        if total%i == 0 and total//i >= i:
            # 이 조건이 없다면 조건을 만족하는 격자 중, yellow 보다 더 많은 값을 가지는 yellow를 출력할수있음
            if (total//i-2)*(i-2) == yellow:
                answer=[total//i, i]
            
    return answer