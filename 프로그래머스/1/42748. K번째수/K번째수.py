def solution(array, commands):
   answer = [0 for i in range(len(commands))]
   for i in range(len(commands)):
      for j in commands[i]:
         list1 = array[commands[i][0]-1:commands[i][1]]
         list1.sort()
         answer[i] = list1[commands[i][2]-1]
   return answer