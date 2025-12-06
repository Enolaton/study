def solution(n, w, num):
    boxes = [[] for _ in range(w)]

    number = 1
    direction = 1

    while number <= n:
        if direction == 1:
            for col in range(w):
                boxes[col].append(number)
                number += 1

                if number > n:
                    break
        else:
            for col in range(w-1,-1,-1):
                boxes[col].append(number)
                number += 1

                if number > n:
                    break
        direction *= -1
        
    for col in boxes:
        if num in col:
            return len(col)-col.index(num)
        
    return 0