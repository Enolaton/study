# [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]	
# [1,5,3,5,1,2,1,4]	

def solution(board, moves):
    answer = 0
    box = []
    for n in moves:
        for i in range(len(board)):
            if board[i][n-1] != 0:
                box.append(board[i][n-1])
                board[i][n-1] = 0
                break
        if len(box) >= 2:
            if box[len(box)-1] == box[len(box)-2]:
                for j in range(2):
                    box.pop()
                    answer += 1
    return answer