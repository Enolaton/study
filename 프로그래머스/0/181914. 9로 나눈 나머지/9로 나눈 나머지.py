def solution(number):
    num_list = list(number)
    num = 0
    for n in num_list:
        num+=int(n)
    return num%9