# 다시풀어야 할 문제

def solution(arr):
    def solve(x, y, size):
        first = arr[x][y]
        
        is_same = all(arr[i][j] == first for i in range(x, x + size) for j in range(y, y + size))
        
        if is_same:
            if first == 0:
                return [1, 0]  
            else:
                return [0, 1]

        half = size // 2
        ul = solve(x, y, half)               
        ur = solve(x, y + half, half)        
        dl = solve(x + half, y, half)        
        dr = solve(x + half, y + half, half) 

        return [
            ul[0] + ur[0] + dl[0] + dr[0],
            ul[1] + ur[1] + dl[1] + dr[1]
        ]

    return solve(0, 0, len(arr))