#include<iostream>
#include <stdio.h>

using namespace std;

int main(int argc, char** argv)
{
	int T;
	scanf("%d", &T);
	for(int test_case = 1; test_case <= T; ++test_case)
	{
        double result = 0.0;
        int arr[11];
        for(int i=0;i<10;i++)
        {
            double num;
            scanf("%d", &num);
            result+=num;
        }
        
        printf("#%d %d\n", test_case, result/10);
	}
	return 0;
}