def solution(n, wires):
    answer = -1
    result = []
    for i in range(n-1):
        network = wires[:i] + wires[i+1:]
        left = [wires[i][0]]
        right = [wires[i][1]]
        while network:
            temp=[]
            if len(temp) == len(network):
                break
            for j in range(len(network)):
                wire = network[j]
                if wire[0] in left:
                    left.append(wire[1])
                elif wire[1] in left:
                    left.append(wire[0])
                elif wire[0] in right:
                    right.append(wire[1])
                elif wire[1] in right:
                    right.append(wire[0])
                else:
                    temp.append(wire)
            network = temp
        result.append(abs(len(left)-len(right)))
    answer = min(result)
    return answer