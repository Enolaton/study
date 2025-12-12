def solution(n):
    answer = 0
    one_counter = bin(n)[2:].count('1')
    num = n # 다음 큰 숫자 체크를 위한 변수
    
    while True: # 반복을 중단할 조건을 미리 지정하지 않음
        n += 1
        n_one_counter = bin(n)[2:].count('1')   # bin(n)[2:] -> str
        if n_one_counter == one_counter: # 1의 개수가 동일한 경우
            # if int(bin(n)[2:]) > num
            answer = n
            break
    
    return answer