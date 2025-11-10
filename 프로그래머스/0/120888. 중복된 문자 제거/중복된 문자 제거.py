def solution(my_string):
    answer = ''
    for _ in my_string:
        if _ not in answer:
            answer+=_
    return answer