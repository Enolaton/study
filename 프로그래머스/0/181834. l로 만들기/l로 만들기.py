def solution(myString):
    answer = ''
    l = len(myString)
    my_string_list = []
    for _ in myString:
        if ord(_) < 108:
            my_string_list.append('l')
        else:
            my_string_list.append(_)
    answer = ''.join(my_string_list)
    return answer