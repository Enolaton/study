from itertools import combinations as comb

def solution(numbers):
    answer = []
    num_list = comb(numbers, 2)
    for a,b in num_list:
        answer.append(a*b)
    return max(answer)