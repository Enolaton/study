def solution(keyinput, board):
    cnt_LR = 0
    cnt_UD = 0
    if len(keyinput)==0: # 테스트 케이스 2번 : keyinput의 길이가 0인 경우
        return [0,0]
    else: 
        for x in keyinput:
            if x == 'left':
                cnt_LR -= 1
                if cnt_LR < -((board[0]-1)//2):
                    cnt_LR = -((board[0]-1)//2)
            elif x == 'right':
                cnt_LR += 1
                if cnt_LR > (board[0]-1)//2:
                    cnt_LR = (board[0]-1)//2
            elif x == 'up':
                cnt_UD += 1
                if cnt_UD > (board[1]-1)//2:
                    cnt_UD = (board[1]-1)//2
            elif x == 'down':
                cnt_UD -= 1
                if cnt_UD < -((board[1]-1)//2):
                    cnt_UD = -((board[1]-1)//2)
        answer = [cnt_LR,cnt_UD]
    return answer