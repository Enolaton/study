def solution(id_pw, db):
    answer = ''
    result = []
    for _ in db:
        if id_pw[0] == _[0]:
                if id_pw[1] == _[1]:
                    result.append('login')
                else:
                    result.append('wrong pw')

        else:
            result.append('fail')

    if 'login' in result:
        answer = 'login'
    elif 'wrong pw' in result:
        answer = 'wrong pw'
    else:
        answer = 'fail'

    return answer