def solution(n):
    answer = 0
    num_str = str(n)
    for _ in num_str:
        answer += int(_)

    return answer