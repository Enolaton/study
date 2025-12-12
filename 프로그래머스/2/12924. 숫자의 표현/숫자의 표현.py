def solution(n):
    answer = 0
    # 1부터 n까지 리스트로 생성 
    num_list = [x for x in range(1,n+1)]
    
    # i는 얼마나 많은 수를 짝지을 것인가에 대한 변수
    # 예를 들어, i가 1이면 [1], [2], [3] 이고
    # i가 2이면 [1,2], [2,3], [3,4]
    for i in range(1,n+1):
        # j는 이동에 관한 변수
        # j가 1이면 [1], 2이면 [2]
        for j in range(1,n+1):
            tmp = num_list[i-1:i+j-1]
            # 효율성 테스트 통과를 위해,
            # 리스트의 합이 n을 초과하는 경우 중단
            if sum(tmp) > n:
                break
            # 리스트의 합이 n과 동일한 경우 +1
            if ((tmp[0]+tmp[-1])*(tmp[-1]-tmp[0]+1))/2 == n:
                answer += 1
                break
    return answer