from itertools import combinations

def solution(number):
    answer = 0
    number_list = combinations(number, 3)
    for n in number_list:
        if sum(n) == 0:
            answer += 1
    return answer