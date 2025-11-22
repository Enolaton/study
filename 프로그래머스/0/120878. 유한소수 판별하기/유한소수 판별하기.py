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
    tmp_list = [1]
    for k in range(len(cnt_list)):
        if cnt_list[k] % 2 == 0 or cnt_list[k] % 5 == 0:
            tmp_list.append(cnt_list[k])
    if tmp_list != cnt_list:
        answer=2
    else:
        answer=1
    return answer