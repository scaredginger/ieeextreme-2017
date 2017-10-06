#include <iostream>
#include <vector>

using namespace std;

int main() {
	int n;
	cin >> n;
	vector<int> values(n);
	for (int i = 0; i < n; i++) {
		cin >> values[i];
	}
	return 0;
}
