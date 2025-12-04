def solution(s):
    answer = ''
    word_list = list(s.split(" "))
    for word in word_list:
        for c in range(len(word)):
            if c%2 == 0:
                answer += word[c].upper()
            else:
                answer += word[c].lower()
        answer += ' ' 
    return answer[:len(answer)-1]