def solution(array):
    answer = 0
    for _ in array:
        answer += str(_).count('7')
    return answer