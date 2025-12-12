import math

def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    head = 0
    tail = len(people)-1
    
    while head <= tail:
        if people[head] <= limit/2:
            answer += math.ceil((tail-head+1)/2)
            break
        if people[head] + people[tail] <= limit:
            if people:
                answer += 1
                head += 1
                tail -= 1
        else:
            answer += 1
            head += 1
    return answer