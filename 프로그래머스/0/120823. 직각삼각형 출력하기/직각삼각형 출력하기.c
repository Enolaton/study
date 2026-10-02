#include <stdio.h>

int main(void) {
    int n;
    scanf("%d", &n);
    int cnt=1;
    for(int i=0; i<n; i++) {
        for(int j=0; j<cnt; j++) printf("*");
        printf("\n");
        cnt++;
    }
    return 0;
}