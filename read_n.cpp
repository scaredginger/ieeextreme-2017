#include <stdio.h>
#include <vector>

using namespace std;

int main() {
	int n;
	scanf("%d", &n);
	vector<int> values(n);
	for (int i = 0; i < n; i++) {
		scanf("%d", &values[i]);
	}
	return 0;
}
