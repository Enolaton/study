def solution(n, m, section):
    answer = 0
    
    # 다시 페인트를 칠해야 하는곳 : False
    # 다시 페인트를 칠하지 않아도 되는 곳 : True
    section_list = [True] * n
    for s in section:
        section_list[s-1] = False
    
    for i in section:
        # 인덱스한 값이 맨 마지막 빈 페이트 영역인 경우 
        if i+m > section[-1]:
            answer+=1
            break
        # 인덱스한 값이 이미 페인트 칠된 경우
        if section_list[i-1] == True:
            continue
        # 페인트 칠 실행
        for j in range(i-1,i+m-1):
            section_list[j] = True
        # 횟수 +1
        answer+=1
    return answer