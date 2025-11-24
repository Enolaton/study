def solution(quiz):
    answer = []
    result = 0
    quiz_list = list(quiz)
    for i in range(len(quiz_list)):
        quiz_list[i] = quiz_list[i].split(' ')
    print(quiz_list)
    for j in range(len(quiz_list)):
        if quiz_list[j][1] == '+':
            if int(quiz_list[j][4]) == (int(quiz_list[j][0]) + int(quiz_list[j][2])):
                answer.append('O')
            else:
                answer.append('X')
        else:
            if int(quiz_list[j][4]) == (int(quiz_list[j][0]) - int(quiz_list[j][2])):
                answer.append('O')
            else:
                answer.append('X')
    return answer