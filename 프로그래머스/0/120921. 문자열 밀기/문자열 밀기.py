def solution(A, B):
    answer = 0
    check_list = []
    for j in range(1,len(A)):
        check = ''
        for i in range(j-len(A),j):
            if A == B:
                answer = 1
                break
            else:
                check += A[i]
        check_list.append(check)

    if B in check_list:
        # B와 같은 인덱스가 여러 개 있는 경우 가장 큰 수 = 가장 적게 움직이는 수를 반환
        rest_list = list(filter(lambda x: check_list[x] == B, range(len(check_list))))
        answer = len(B) - (max(rest_list) + 1)
    else:
        answer += -1
    return answer