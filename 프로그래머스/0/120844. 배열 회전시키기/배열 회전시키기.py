def solution(numbers, direction):
    answer = [0 for i in range(len(numbers))] # numbers 와 같은 크기의 리스트 반한 리스트 생성
    if direction == 'right': # 오른쪽으로 밀기
        answer[0] = numbers[-1] # numbers[-1]을 따로 처리
        for i in range(len(numbers)-1): 
            answer[i + 1] = numbers[i]
    else: # 왼쪽으로 밀기
        answer[-1] = numbers[0] # numbers[0]를 따로 처리
        for i in range(1,len(numbers)):
            answer[i - 1] = numbers[i]

    return answer