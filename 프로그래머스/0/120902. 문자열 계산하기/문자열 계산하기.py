def solution(my_string):
    check = ''
    my_string = my_string.split()
    answer = int(my_string[0])
    for _ in my_string:
        if _ == '+':
            check = '+'
            continue
        elif _ == '-':
            check = '-'
            continue
        if check == '+':
            answer += int(_)
        elif check == '-':
            answer -= int(_)
    return answer