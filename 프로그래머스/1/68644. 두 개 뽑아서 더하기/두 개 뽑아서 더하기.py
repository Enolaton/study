from itertools import combinations as c

def solution(numbers):
    answer = []
    number_list = []
    for a,b in c(numbers,2):
        number_list.append(a+b)
    for i in number_list:
        if i not in answer:
            answer.append(i)
    answer.sort()
    return answer