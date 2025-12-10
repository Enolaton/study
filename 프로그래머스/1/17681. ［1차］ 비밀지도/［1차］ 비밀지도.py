def solution(n, arr1, arr2):
    answer = []
    arr1_binary = []
    arr2_binary = []
    
    # 10진수 배열을 2진수 리스트로 변환
    for num in range(n):
        arr1_binary.append(bin(arr1[num])[2:])
        arr2_binary.append(bin(arr2[num])[2:])
        
    for a1,a2 in zip(arr1_binary,arr2_binary):
        # 원소 X의 길이가 n보다 작을 경우, '100'인 경우 '00100'반환 
        if len(a1) < n: 
                arr1_binary[arr1_binary.index(a1)] = '0'*(n-len(a1))+a1
        if len(a2) < n:
                arr2_binary[arr2_binary.index(a2)] = '0'*(n-len(a2))+a2
                
    # 기본으로 '#'을 n만큼 두고, 두 배열의 원소 중 0이 있으면 (공백)을 변환
    for row in range(n):
        result = '#'*n
        for column in range(n):
            if arr1_binary[row][column] == '0' and arr2_binary[row][column] == '0':
                # 슬라이싱을 이용해서 바뀐 문자열 변환
                result = result[:column]+' '+result[column+1:] 
        answer.append(result)
    return answer