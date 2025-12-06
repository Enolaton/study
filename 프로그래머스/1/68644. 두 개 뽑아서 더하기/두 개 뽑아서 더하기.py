"""
numbers의 첫 번째 원소에 접근
            ↓
numbers의 두 번째 원소부터 마지막까지 접근하며 첫번째 원소와 더하기
(단, 더한 값이 출력리스트 answer에 없어야 함)
            ↓
answer를 sort함수를 사용하여 오름차순 정렬
"""

# itertools-combinations 를 사용하지 않고 푸는 방법
def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i]+numbers[j] not in answer:
                answer.append(numbers[i]+numbers[j])
    answer.sort()
    return answer