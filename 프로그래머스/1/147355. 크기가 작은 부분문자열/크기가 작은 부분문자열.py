def solution(t, p):
    answer = 0
    for i in range(len(t)):
        print()
        if int(t[i:i+len(p)]) <= int(p):
            answer += 1
        if i + len(p) >= len(t):
            break
    return answer
