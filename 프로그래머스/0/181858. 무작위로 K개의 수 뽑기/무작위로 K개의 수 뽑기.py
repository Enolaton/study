def solution(arr, k):
    temp = []
    for n in arr:
        if n not in temp:
            temp.append(n)
    temp=temp[:k]
    for i in range(k-len(temp)):
        temp.append(-1)
    return temp