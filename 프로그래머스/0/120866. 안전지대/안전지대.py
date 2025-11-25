def solution(board):
    answer = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 1:
                try:
                    for m in range(i-1, i+2):
                        if m>=0:
                            for n in range(j-1, j+1):
                                if n>= 0:
                                    if board[m][n] != 1:
                                        board[m][n] = 'is_danger'
                except:
                    pass
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 1:
                try:
                    for m in range(i-1, i+2):
                        if m>=0:
                            for n in range(j, j+2):
                                if board[m][n] != 1:
                                    board[m][n] = 'is_danger'
                except:
                    pass
    # 열이 하나인 리스트
    if len(board[0]) == 1:
        try:
            for l in range(len(board)):
                if board[l][0] == 1:
                    if board[l + 1][0] != 1:
                        if l-1>=0:
                            board[l - 1][0] = 'is_danger'
                        board[l + 1][0] = 'is_danger'
        except:
            pass
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                answer += 1
    return answer