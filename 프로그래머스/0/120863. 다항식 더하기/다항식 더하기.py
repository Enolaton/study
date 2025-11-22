def solution(polynomial):
    answer = ''
    polynomial = polynomial.split(' ') # 공백 제거 후 리스트로 반환
    p_list = []
    # 리스트 안에 공백(' ') 과 더하기('+') 제거 후, 'x' 를 '1x'로 반환
    for c in polynomial:
        if c != '+':
            if c == 'x':
                p_list.append('1x')
                continue
            p_list.append(c)
    print(p_list)
    ct_count = 0 # constant term  상수항
    lt_count = 0 # linear term 선형항 / 1차항
    for i in p_list:
        if 'x' not in i:
            ct_count += int(i) # 상수항 더하기
        else:
            lt_count += int(i[:len(i)-1]) # 선형항 더하기
    if ct_count != 0:
        if lt_count != 0:
            # 1차항, 상수항 모두 있는 경우
            answer = f'{lt_count}x + {ct_count}'
        else:
            # 상수항만 있는 경우
            answer = f'{ct_count}'
    else:
        # 1차항만 있는 경우
        answer = f'{lt_count}x'
    # '1x' 를 'x' 로 변환
    if lt_count == 1:
        if '1x' in answer:
            answer = answer.replace('1x', 'x')
    return answer