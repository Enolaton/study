def solution(cards1, cards2, goal):
    answer = 'Yes'
    for _ in range(len(goal)):
        if cards1 == []:
            if goal[0] == cards2[0]:
                goal.remove(goal[0])
                cards2.remove(cards2[0])
            else:
                answer = 'No'
        elif cards2 == []:
            if goal[0] == cards1[0]:
                goal.remove(goal[0])
                cards1.remove(cards1[0])
            else:
                answer = 'No'
        else:
            if goal[0] == cards1[0]:
                goal.remove(goal[0])
                cards1.remove(cards1[0])
            elif goal[0] == cards2[0]:
                goal.remove(goal[0])
                cards2.remove(cards2[0])
            else:
                answer = 'No'
                break
    return answer