def solution():
    T = int(input())
    for test_case in range(1,T+1):
        beverage = list(map(int, input().split()))
        answer = sum(beverage)//100
        print(f"#{test_case}", answer)

if __name__ == '__main__':
    solution()