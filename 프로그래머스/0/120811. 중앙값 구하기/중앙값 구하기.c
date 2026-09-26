#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// array_len은 배열 array의 길이입니다.
int solution(int array[], size_t array_len) {
    int answer = 0;
    int temp;
    for(int i=0; i<array_len; i++) {
        int min_index=i;
        for(int j=i+1; j<array_len; j++) {
            if (array[j]<array[min_index]){
                min_index = j;
            }
        }
        temp = array[i];
        array[i] = array[min_index];
        array[min_index] = temp;
    }
    answer = array[array_len/2];
    return answer;
}