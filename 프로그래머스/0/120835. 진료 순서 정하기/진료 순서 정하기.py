def solution(emergency):
    answer = []
    em = [[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0],[8,0],[9,0],[10,0]] # 응급도와 인덱스를 연결할 2차원 리스트 생성
    emer_sort = sorted(emergency, reverse=True) # 응급도 순으로 배열 정렬
    for j in range(len(emer_sort)): # 응급도와 진료순서를 연결
        em[j][1] += emer_sort[j] 
    for _ in emergency: 
        for i in range(len(emergency)): 
            if _ == em[i][1]:
                answer.append(em[i][0])
    return answer