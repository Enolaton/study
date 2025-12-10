def solution(n, m, section):
    answer = 0
    
    # 다시 페인트를 칠해야 하는곳 : False
    # 다시 페인트를 칠하지 않아도 되는 곳 : True
    section_list = [True] * n
    for s in section:
        section_list[s-1] = False
    
    for i in section:
        if i+m > section[-1]:
            answer+=1
            break
        if section_list[i-1] == True:
            continue
        for j in range(i-1,i+m-1):
            section_list[j] = True
        answer+=1
    return answer