def solution(array):
    answer = 0
    num_count = [0 for _ in range(1000)] # 0부터 999까지의 리스트
    for _ in array:
        num_count[_] += 1 # 1이 들어오면 인덱스 번호가 1인 요소를 +1함
    if num_count.count(max(num_count)) != 1: # 최빈값의 수가 1이 아닌 경우
        answer = -1
    else: # 최빈값의 수가 하나인 경우
        answer = num_count.index(max(num_count))
    return answer