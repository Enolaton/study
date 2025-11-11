def solution(before, after):
    answer = 0
    # 문자열은 정리하기 어려우니, 리스트로 변환
    before_list = list(before)
    after_list = list(after)
    
    # before 리스트의 값이 after에 있으면, 두 리스트에서 삭제
    for _ in before_list:
        if _ in after_list:
            before_list.remove(_)
            after_list.remove(_)
            
    # 정렬되지 않으면, 같은 리스트라고 인식하지 못함
    # 정렬 된 값이 같으면, answer=1
    if  sorted(before_list) == sorted(after_list):
        answer=1
    return answer