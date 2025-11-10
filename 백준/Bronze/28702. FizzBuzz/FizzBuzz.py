fb_list = []

for i in range(3):
    x = input()
    if x != "Fizz" and x != "Buzz" and x != "FizzBuzz":
        fb_list.append([3-i,int(x)])
for j in fb_list:
    if (sum(j))%3==0 and (sum(j))%5==0:
        print("FizzBuzz")
    elif (sum(j))%3==0:
        print("Fizz")
    elif (sum(j))%5==0:
        print("Buzz")
    else:
        print(str(sum(j)))
    break