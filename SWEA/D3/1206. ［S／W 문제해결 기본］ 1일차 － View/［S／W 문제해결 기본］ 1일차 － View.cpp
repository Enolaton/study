#include <stdio.h>

int main(int argc, char** argv)
{
	int test_case;
	int T=10;
    
	for(test_case = 1; test_case <= T; ++test_case) {
        int view = 0;
        // 가로길이(N) : 건물의 수 + 4
        int N;
        scanf("%d",&N);
        
        // 건물의 높이 배열
        int building[N];
        for(int i=0; i<N; i++) {
             scanf("%d",&building[i]);
        }
        
        // 조망권 계산
        for(int i=2; i<N-2; i++) {
            int max_left = (building[i-2]>=building[i-1]) ? building[i-2] :building[i-1];      // 왼쪽 건물 두 개 중 큰 건물
            int max_right = (building[i+2]>=building[i+1]) ? building[i+2] : building[i+1];   // 오른쪽 건물 두 개 중 큰 건물
            int max_building = (max_left>=max_right) ? max_left : max_right;      // 좌, 우 건물 중 큰 건물의 높이 
            
            // 기준 건물이 조망권이 확보 될때만 전체 결과에 더 함
            if (building[i] > max_building){
                view += (building[i]-max_building);
            }
        }
        printf("#%d %d\n",test_case, view);
    }
	
	return 0;
}