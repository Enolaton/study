def solution(s):
    answer = []
    jc_list = s.split(' ')
    for word in jc_list:
        tmp = ''
        for c in range(len(word)):
            if word[c].isalpha() == True:
                if c == 0:
                    tmp += word[c].upper()
                else:
                    tmp += word[c].lower()
            else:
                tmp += word[c]
        answer.append(tmp)
    return ' '.join(answer)