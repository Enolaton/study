def solution():
    T = int(input())
    for test_case in range(1,1+T):
        N = int(input())
        distance = 0
        speed = 0
        for _ in range(N):
            cmd = list(map(int, input().split()))
            if len(cmd) != 1:
                if cmd[0] == 1:
                    speed += cmd[1]
                else:
                    speed -= cmd[1]
                    if speed<0:
                        speed = 0
            distance += speed
        print(f"#{test_case}", distance)
        
    
if __name__=="__main__":
    solution()