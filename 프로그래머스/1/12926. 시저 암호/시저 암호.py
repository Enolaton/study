def solution(s, n):
    answer = ''
    for c in s:
        # 공백 배제
        if c == ' ':
            answer += ' '
            
        # 아스키코드
        elif c.islower():
            if ord(c)+n > 122:
                answer += chr(ord(c)+n-26)
            else:
                answer += chr(ord(c)+n)
        elif c.isupper():
            if ord(c)+n > 90:
                answer += chr(ord(c)+n-26)
            else:
                answer += chr(ord(c)+n)
    return answer