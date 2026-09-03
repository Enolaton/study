#include<iostream>
#include <vector>
#include <numeric>

using namespace std;

int main(int argc, char** argv)
{
	int test_case;
	int T;
	cin>>T;
    
	for(test_case = 1; test_case <= T; ++test_case)
	{
        vector<int> numbers;
        int n;
        for (int i=0; i<10;i++) {
            cin >> n;
            if (n%2==1) {
            	numbers.push_back(n);
            }
        }
        cout << "#" << test_case << " " << accumulate(numbers.begin(),numbers.end(),0) << "\n";
	}
	return 0;
}