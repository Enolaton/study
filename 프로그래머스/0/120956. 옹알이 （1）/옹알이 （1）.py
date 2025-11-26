from itertools import permutations

def solution(babbling):
    answer = 0
    
    # 옹알이로 할 수 있는 모든 옹알이 조합(순열)을 tmp_list에 저장
    babbling_list = ["aya", "ye", "woo", "ma"]
    tmp_list = []
    for i in range(1,len(babbling_list)+1):
        for j in list(permutations(babbling_list, i)):
            tmp_str = ''
            for k in range(len(j)):
                tmp_str += j[k]
            tmp_list.append(tmp_str)
            
    for b in babbling:
        if b in tmp_list:
            answer += 1
    return answer