from itertools import combinations as comb

def solution(nums):
    answer = []
    num_list = list(comb(nums, 3))
    sum_nums = []
    for i in num_list:
        sum_nums.append(sum(i))
    for num in sum_nums:
        is_prime = True
        for n in range(2,num//2):
            if num%n==0:
                is_prime=False
        if is_prime:
            answer.append(num)
        
    return len(answer)