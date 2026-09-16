def calc_pos(nums, n):
    for row in range(len(nums)):
        for col in range(len(nums[row])):
            if str(n) == nums[row][col]:
                return [row,col]

def solution(numbers, hand):
    answer = []
    position = [['1','2','3'],['4','5','6'],['7','8','9'], ['*','0','#']]
    l_pos = [3,0]
    r_pos = [3,2]
    for n in numbers:
        if str(n) in ['1','4','7']:
            answer.append('L')
            l_pos = calc_pos(position, n)
        elif str(n) in ['3','6','9']:
            answer.append('R')
            r_pos = calc_pos(position, n)
        else:
            num_pos = calc_pos(position, n)
            l_dist = abs(num_pos[0]-l_pos[0]) + abs(num_pos[1]-l_pos[1])
            r_dist = abs(num_pos[0]-r_pos[0]) + abs(num_pos[1]-r_pos[1])
            if l_dist<r_dist:
                answer.append('L')
                l_pos = calc_pos(position, n)
            elif l_dist>r_dist:
                answer.append('R')
                r_pos = calc_pos(position, n)
            else:
                if hand == "left":
                    answer.append('L')
                    l_pos = calc_pos(position, n)
                else:
                    answer.append('R')
                    r_pos = calc_pos(position, n)
    return ''.join(answer)