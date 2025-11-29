def solution(sizes):
    answer = 0
    w_list = []
    h_list = []
    
    for size in sizes:
        size.sort()
    
    for i in range(len(sizes)):
      w,h = sizes[i]
      w_list.append(w)
      h_list.append(h)
      
    answer = max(w_list) * max(h_list)
    return answer