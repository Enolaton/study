import math

def solution(signals):
    result = -1
    n = len(signals)
    t = 1
    cycle = []
    
    for i in range(n):
        cycle.append(sum(signals[i]))
    num = math.lcm(*cycle)
    
    while t<=num:
        is_blackout = True
        for i in range(n):
            green = signals[i][0]
            yellow = signals[i][1]
            if not (green <= (t-1)%cycle[i] < green+yellow):
                is_blackout = False
                break
        if is_blackout:
            result = t
            break
        t+=1
        
    return result
    