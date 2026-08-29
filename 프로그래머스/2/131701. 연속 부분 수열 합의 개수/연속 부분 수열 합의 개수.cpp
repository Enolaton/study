#include <string>
#include <vector>
#include <unordered_set>

using namespace std;

int solution(vector<int> elements) {
    int n = elements.size(); // elements 배열의 길이
    vector<int> extended_elements = elements; // 확장 배열 선언
    for (int i=0;i<n;i++) {
        extended_elements.push_back(elements[i]);
    }
    // 중복을 제거하여 담을 sum_set
    unordered_set<int> sum_set;
    // 길이 0 ~ n까지 부분수열 
    for (int len=1; len<=n; len++) {
        // 시작위치: 0 ~ (n-1)
        for (int start=0; start<n; start++) {
            int current_sum = 0;
            // start부터 len개 만큼 더함
            for (int k=0; k<len; k++) {
                current_sum += extended_elements[start+k];
            }
            sum_set.insert(current_sum);
        }
    }
    return sum_set.size();
}