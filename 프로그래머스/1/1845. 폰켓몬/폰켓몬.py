def solution(nums):
    answer = 0
    number = len(nums)/2
    pkm_list = []
    for i in nums:
        if i not in pkm_list:
            pkm_list.append(i)
    answer = min(len(pkm_list), number)

    return answer