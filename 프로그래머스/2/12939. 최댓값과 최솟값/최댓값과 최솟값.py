def solution(s):
    str_list = s.split(' ')
    num_list = []
    
    for c in str_list:
        num_list.append(int(c))
        
    num_list = sorted(num_list)
    
    return str(num_list[0]) + ' ' + str(num_list[-1])