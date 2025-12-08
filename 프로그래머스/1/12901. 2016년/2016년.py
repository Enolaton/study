def solution(a, b):
    answer = ''
    day_list = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
    months_list = [31,29,31,30,31,30,31,31,30,31,30,31]
    day_month = 5
    for i in range(a-1):
        day_month += months_list[i]
    day_month += b-1
    day_month = day_month%7
    answer = day_list[day_month]
    return answer