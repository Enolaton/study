def solution(array, n):
    answer = 0
    close = [0 for _ in range(len(array))]
    x = 0
    tmp = []
    for i in range(len(array)):
        close[i] += abs(array[i]-n)
    x = min(close)
    print('가장 차이 값',x)
    if close.count(x) == 1: # 가장 작은 차이 값을 가지는 값이 리스트 안에 1개인 경우
        answer = array[close.index(x)]
    else:
        for j in range(len(close)):
            if close[j] == x:
                tmp.append(array[j])
        answer = min(tmp)
    return answer