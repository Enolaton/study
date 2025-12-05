def solution(number, limit, power):
    answer = 0
    for n in range(1,number+1):
        div_list = []
        for i in range(1,int(n**(1/2))+1):
            if n%i == 0:
                div_list.append(i)
                if (i**2) != n:
                    div_list.append(n//i)
        if len(div_list) > limit:
             answer += power
        else:
             answer += len(div_list)   
    return answer