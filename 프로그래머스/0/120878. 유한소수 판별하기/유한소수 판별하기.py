def solution(a, b):
    answer = 1
    cnt_list = [] # 분모의 약수를 담을 리스트
    if a>b:
        for i in range(b,1,-1):
            # 최소공배수가 있는 경우
            if a%i == 0 and b%i ==0:
                # 최소공배수로 나눈 수를 반환
                a = a//i
                b = b//i
        for j in range(1,b+1):
            if b%j  == 0:
                cnt_list.append(j)
    else:
        for i in range(a,1,-1):
            # 최소공배수가 있는 경우
            if a%i == 0 and b%i ==0:
                # 최소공배수로 나눈 수를 반환
                a = a//i
                b = b//i
        for j in range(1,b+1):
            if b%j  == 0:
                cnt_list.append(j)
    # 분모의 약수 리스트 중 2와 5의 배수만 모을 리스트  
    tmp_list = [1]
    # 약수 리스트 안에 2와 5를 제외한 약수가 포함된 경우 -> 무한소수 
    for k in range(len(cnt_list)):
        if cnt_list[k] % 2 == 0 or cnt_list[k] % 5 == 0:
            tmp_list.append(cnt_list[k])
    # 분모의 약수 리스트 중에서 2와 5의 배수만 모은 것과 모든 약수 리스트 두개가 다르다면 무한소수
    if tmp_list != cnt_list:
        answer=2
    else: # 같은 경우 분모가 2와 5로만 이루어진 경우 -> 유한소수
        answer=1
    return answer