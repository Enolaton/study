# code by gemini 
# 차후에 다시 풀 예정

def solution(n):
    answer = []
    pegs = {1:[x for x in range(n,0,-1)], 2:[], 3:[]}
    move = 1
    
    if n%2==0:
        smallest = {1:2, 2:3, 3:1}
    else:
        smallest = {1:3, 2:1, 3:2}
        
    for step in range(1,2**n):
        if step%2 != 0:
            dest = smallest[move]
            pegs[move].pop()
            pegs[dest].append(1)
            answer.append([move, dest])
            move = dest
        else:
            p1, p2 = [p for p in (1,2,3) if p != move]
            
            top1 = pegs[p1][-1] if pegs[p1] else float('inf')
            top2 = pegs[p2][-1] if pegs[p2] else float('inf')
            
            if top1 < top2:
                disk = pegs[p1].pop()
                pegs[p2].append(disk)
                answer.append([p1,p2])
            else:
                disk = pegs[p2].pop()
                pegs[p1].append(disk)
                answer.append([p2,p1])
    return answer