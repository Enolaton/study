def solution(food):
    food_list = []
    # 선수 a가 왼쪽, 선수 b가 오른쪽에서 시작한다고 할때
    # 왼쪽만 다 계산하고, 0을 추가한 후 왼쪽 계산을 역으로 출력한 후, 전체 반환
    
    for i in range(1,len(food)):
        food_num = food[i]
        food_list.append(str(i)*(food_num//2))

    food_list.append('0')
    food_str = ''.join(food_list)
    food_len = len(''.join(food_list))
    for j in range(-2,-(food_len+1),-1): # 맨 마지막 인덱스부터 0까지 뒤에서부터 출력
        food_list.append(food_str[j])
    return ''.join(food_list)