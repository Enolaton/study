from itertools import permutations

def solution(spell, dic):
    answer = 0
    new_spell = []
    result = []

    # spell 안 문자열 조합 만들기
    for _ in permutations(spell, len(spell)):
        new_spell.append(_)

    for _ in new_spell:
        result.append(''.join(_))
    for _ in result:
        if _ in dic:
            answer = 1
            break
        else:
            answer = 2
    return answer