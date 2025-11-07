def solution(my_string):
    answer = ''
    my_string_list = [] # sort 함수 사용을 위한 리스트 선언
    my_string = my_string.lower() # my_string -> 소문자로 변환
    
    for _ in my_string:
        my_string_list.append(_)
    my_string_list.sort()
    
    for _ in my_string_list:
        answer += _
    
    return answer