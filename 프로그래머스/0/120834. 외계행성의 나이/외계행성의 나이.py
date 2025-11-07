def solution(age):
    answer = ''
    name_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    name = str(age) # 입력값 age가 정수이므로, 먼저 str로 타입변경
    for _ in name: # 문자열 타입으로 반복문에서 문자 하나씩 접근하고, 문자를 다시 정수로 변경
        answer += name_list[int(_)] # 정수로 변경한 것을 인덱싱을 통해서 answer에 값 저장
    return answer