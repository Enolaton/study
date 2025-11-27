def solution(x):
    answer = True
    h = 0
    for _ in str(x):
        h += int(_)
    if x%h != 0:
        answer = False
    return answer