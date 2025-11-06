def hour2min(num):
    hour = num // 100
    min = num % 100
    return hour * 60 + min

def solution(schedules, timelogs, startday):
    answer = 0
    for i in range(len(schedules)):
        employ = 0
        timelogs[i] = timelogs[i][7-startday+1:] + timelogs[i][:7-startday+1]
        for j in range(5):
            timelogs[i][j] = hour2min(timelogs[i][j])
            if timelogs[i][j] > hour2min(schedules[i]) + 10:
                break
            else:
                employ += 1
        if employ == 5:
            answer += 1
            
        
    return answer