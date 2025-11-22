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
        rest_list = list(filter(lambda x: check_list[x] == B, range(len(check_list))))
        # print(max(rest_list))
        answer = len(B) - (max(rest_list) + 1)
        # if check_list.index(B)+1 <= len(B)-(check_list.index(B)+1):
        #     answer = check_list.index(B)+1
        # else:
        #     answer = len(B) - (check_list.index(B)+1)
    else:
        answer += -1
    return answer