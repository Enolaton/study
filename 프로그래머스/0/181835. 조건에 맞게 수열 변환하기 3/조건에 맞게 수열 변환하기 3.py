def solution(arr, k):
    if k%2 == 0:
        for i in range(len(arr)):
            arr[i] = arr[i]+k
    else:
         for j in range(len(arr)):
            arr[j] = arr[j]*k
    return arr