def solution(sides):
    answer = 0
    for i in range(abs(sides[0]-sides[1])+1,sides[0]+sides[1]):
        answer+=1
    return answer