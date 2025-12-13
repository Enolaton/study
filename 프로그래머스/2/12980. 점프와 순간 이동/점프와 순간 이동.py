def solution(n):
    answer = 0
    while n > 0:
        # 순간이동은 배터리 사용X
        if n%2  == 0:
            n /= 2
        else:
            # 점프 사용시 배터리 사용O
            n-=1
            answer += 1
    return answer