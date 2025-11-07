def solution(num, k):
    answer = 0
    list_num = [] # 정수 상태에서는 문자열 인덱싱이 어렵기 때문에 리스트 형태로 전환
    for _ in str(num): # 문자열을 문자 하나씩 리스트에 저장
        list_num.append(int(_))

    if k not in list_num: # 입력값 k가 리스트에 없으면, -1 반환
        answer = answer-1
    else:
        answer = list_num.index(k)+1 # 자릿수 = 인데스 + 1
    return answer