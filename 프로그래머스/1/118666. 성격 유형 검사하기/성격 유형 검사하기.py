def solution(survey, choices):
    result = []
    answer = {'R':0,'T':0,'C':0,'F':0,'J':0,'M':0,'A':0,'N':0}
    for i in range(len(survey)):
        match choices[i]:
            case 1:
                answer[survey[i][0]] += 3
            case 2:
                answer[survey[i][0]] += 2
            case 3:
                answer[survey[i][0]] += 1
            case 5:
                answer[survey[i][1]] += 1
            case 6:
                answer[survey[i][1]] += 2
            case 7:
                answer[survey[i][1]] += 3
                
    if answer['R'] >= answer['T']:
        result.append('R')
    else:
        result.append('T')
    if answer['C'] >= answer['F']:
        result.append('C')
    else:
        result.append('F')
    if answer['J'] >= answer['M']:
        result.append('J')
    else:
        result.append('M')
    if answer['A'] >= answer['N']:
        result.append('A')
    else:
        result.append('N')
    return ''.join(result)