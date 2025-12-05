def solution(numbers):
    answer = [-1] * len(numbers)
    temp = []
    # numbers 뒤에서부터 인덱싱
    for i in range(-1,-(len(numbers)+1),-1):
        while temp and temp[-1] <= numbers[i]:
            temp.pop()
        if temp:
            answer[i] = temp[-1]
        temp.append(numbers[i])
    return answer