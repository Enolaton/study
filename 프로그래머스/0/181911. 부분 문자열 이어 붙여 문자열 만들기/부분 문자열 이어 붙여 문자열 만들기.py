def solution(my_strings, parts):
    word_list = []
    for i in range(len(my_strings)):
        word_list.append(my_strings[i][parts[i][0]:parts[i][1]+1])
    answer = ''.join(word_list)
    return answer
