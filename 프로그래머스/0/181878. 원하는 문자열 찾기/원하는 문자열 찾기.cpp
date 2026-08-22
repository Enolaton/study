#include <string>
#include <vector>
#include <cctype>

using namespace std;

int solution(string myString, string pat) {
    int answer = 0;
    
    int strLen = myString.length();
    int patLen = pat.length();
    
    // myString 소문자 변환
    for (char &c : myString) {
        c=tolower(c);
    }
    
    // pat 소문자 변환
    for (char &c : pat) {
        c=tolower(c);
    }
    
    // 문자열 비교
    for (int i=0; i<=strLen-patLen; i++) {
        if (i+patLen <= strLen) {
            // substr(시작인덱스,길이)
            if (myString.substr(i,patLen) == pat){
                answer=1;
                break;
            }
        }
    }
    
    return answer;
}