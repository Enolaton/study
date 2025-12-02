def solution(food):
    food_list = []

    for i in range(1,len(food)):
        food_num = food[i]
        food_list.append(str(i)*(food_num//2))

    food_list.append('0')
    food_str = ''.join(food_list)
    food_len = len(''.join(food_list))
    for j in range(-2,-(food_len+1),-1): # 맨 마지막 인덱스부터 0까지 뒤에서부터 출력
        food_list.append(food_str[j])
    return ''.join(food_list)