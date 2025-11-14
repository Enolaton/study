numCount = int(input())

numList = list(map(int, input().split()))
numMax = max(numList)
sum = 0
for i in range(0, numCount):
    sum = sum + numList[i]

# num1, num2, num3 = map(int, input().split())
# numMax = max(num1, num2, num3)
# sum = num1 + num2 + num3

everage = sum*100/numMax/numCount
print(everage)
