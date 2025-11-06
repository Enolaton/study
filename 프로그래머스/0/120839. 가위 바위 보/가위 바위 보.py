def solution(rsp):
    answer = ''
    rsp_dict = {'2':'0','0':'5','5':'2'}
    for i in range(len(rsp)):
        answer+=rsp_dict[rsp[i]]
    return answer