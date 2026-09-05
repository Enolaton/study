def solution():
    T = int(input())
    for test_case in range(1, T + 1):
        n = int(input())
        A = [1, 1] 
        
        for i in range(2, n + 1):
            num = 1 
            
            while True:
                check = True
                
                for k in range(1, (i // 2) + 1):
                    if num == 2 * A[i-k] - A[i-2*k]:
                        check = False
                        break 
                        
                if check:
                    A.append(num) 
                    break
                    
                num += 1
                
        print(A[n])

if __name__ == "__main__":
    solution()