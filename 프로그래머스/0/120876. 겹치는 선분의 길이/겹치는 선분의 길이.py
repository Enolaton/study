def solution(lines):
    d = {}
    for i in range(len(lines)):
        r = lines[i]
        for k in range(r[0], r[1], 1):
            if k in d:
                d[k] += 1
            else:
                d[k] = 1
    count = 0
    for i in d.values():
        if i >= 2:
            count += 1
    return count