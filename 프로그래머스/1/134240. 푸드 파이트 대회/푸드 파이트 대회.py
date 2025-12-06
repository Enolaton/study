"""
선수 a가 왼쪽, 선수 b가 오른쪽에서 시작한다고 할때
왼쪽만 다 계산하고, 0을 추가한 후 왼쪽 계산을 역으로 출력한 후, 전체 반환

예시) [우리가 계산한 리스트] + '0' + [계산한 리스트를 역으로 출력한 리스트]
"""

def solution(food):
    food_list = []
    
    # 왼쪽 선수가 먹은 음식을 food_list에 추가
    for i in range(1,len(food)):
        food_num = food[i]
        food_list.append(str(i)*(food_num//2))

    # '0'(물) 추가 
    food_list.append('0')
    food_str = ''.join(food_list)
    food_len = len(''.join(food_list))

    # 맨 마지막 인덱스부터 0까지 뒤에서부터 역출력
    for j in range(-2,-(food_len+1),-1): 
        food_list.append(food_str[j])
        
    # 리스트를 문자열로 반환하는 방법 -> ''.join(바꾸려고 하는 리스트 이름)
    return ''.join(food_list)