#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int* solution(int n) {
    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
    int* answer = (int*)malloc(n*sizeof(int));
    int cnt = 0;
    for(int i=1; i<n+1; i++) {
        if (i%2!=0) {
            answer[cnt] = i;
            cnt++;
        }
    }
    for(int j=0; j<cnt; j++) {
        printf("%d", answer[j]);
    }
    return answer;
}