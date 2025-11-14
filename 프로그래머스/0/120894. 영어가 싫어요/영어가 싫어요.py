def solution(numbers):
    answer = ''
    number = list(numbers)
    num = { 
        'zero': 0,
        'one' : 1,
        'two' : 2,
        'three' : 3,
        'four' : 4,
        'five' : 5,
        'six' : 6,
        'seven' : 7,
        'eight' : 8,
        'nine' : 9
    }
    s=''
    for i in range(len(numbers)):
      s += number.pop(0)
      if s in num:
        answer += str(num[s])
        s=''  
    return int(answer)