def solution(arr, l, r):
    # brr을 만들어서 풀면 테스트케이스 4~6에서 timeout 발생
    # brr을 만들지 않고, 계산해서 풀어야 함
    
    k = 0
    c = 0
    l -= 1      # 5번째 원소의 위치는 인덱스4번
    size = r-l  # 부분배열brr의 원소의 개수
    win = size
    
    for n in arr:
        if l < 0:
            if size <= 0:
                break
            elif size-n <= 0:
                k += n*size
                size -= n
            elif size-n > 0:
                k += n*n
                size -= n
        elif l-n <= 0:
            if n-l > size:    # 숫자n묶음에서 size만큼을 빼고도 숫자가 남을경우
                k += n*size
                size = 0
                l -= n
            else:
                k += n*(n-l)
                size -= (n-l)
                l -= n
        elif l-n > 0:
            l -= n
            
    ans_k = k  
    i = 0
    j = 0 
    size = 0  
    rem = win
    r_cnt = 0
    
    for idx, n in enumerate(arr):
        if rem > n:
            size += n * n
            rem -= n
        else:
            size += rem * n
            j = idx
            r_cnt = n - rem  
            break
            
    k -= size  
    l_cnt = arr[0] 
    
    if k == 0:
        c = 1
    
    while j < len(arr):
        step = min(l_cnt, r_cnt)
        
        diff = arr[j] - arr[i]
        
        if diff == 0:
            if k == 0:
                c += step
        else:
            if k % diff == 0 and 0 <= k // diff < step:
                c += 1
                
        k -= diff * step
        l_cnt -= step
        r_cnt -= step
        
        if l_cnt <= 0:
            i += 1
            if i < len(arr):
                l_cnt = arr[i]
                
        if r_cnt <= 0:
            j += 1
            if j < len(arr):
                r_cnt = arr[j]
                
    return [ans_k, c]