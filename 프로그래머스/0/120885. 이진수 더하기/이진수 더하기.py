def solution(bin1, bin2):
    # 둘 다 0일 경우, 무한루프 -> 강제 0 리턴
  if bin1 == '0' and bin2 == '0':
    return '0'

  answer = ''
  n1 = 0 # 10진수로 변환한 bin1 값
  n2 = 0 # 10진수로 변환한 bin2 값

  # bin1을 10진수 n1으로
  for i in range(len(bin1)):
      if bin1[i] == "1":
        n1 += 2**(len(bin1)-i-1)
  print(n1)

  # bin2를 10진수 n1로
  for i in range(len(bin2)):
      if bin2[i] == "1":
        n2 += 2**(len(bin2)-i-1)
  print(n2)
  
  n3 = n1+n2

  # bin1+bin2의 값을 2진수로 변환
  while n3 != 1:
      answer += str(n3%2)
      n3 = n3//2 

  # 인덱싱이 앞에서부터라 정답이 거꾸로 나옴
  answer += str(n3%2)
  # 문자열을 뒤집어 줌
  reverse_answer = ''.join(reversed(answer))

  return reverse_answer