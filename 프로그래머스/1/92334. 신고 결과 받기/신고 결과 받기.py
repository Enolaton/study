def solution(id_list, report, k):
    answer = [ 0 for _ in range(len(id_list)) ]
    report_set = set(report)
    id_dict = {}
    report_list = {}
    ban_list = []
    
    for name in id_list:
        report_list[name] = []
    
    for i in id_list:
        id_dict[i]=0
    
    for r in report_set:
        a,b = r.split()
        id_dict[b] += 1
        report_list[a].append(b)
    for n in id_dict:
        if id_dict[n] >= k:
            for c in report_list:
                if n == c:
                    ban_list.append(n)
    for m in report_list:
        for b in report_list[m]:
            if b in ban_list:
                answer[id_list.index(m)]+=1
            
    return answer