#include <cstdio>

using namespace std;

void operate(int);

void operate(int a) {
	printf("%d\n", a);
}

int main() {
	int n;
	scanf("%d\n", &n);
	for (int i = 0; i < n; i++) {
		int a;
		scanf("%d\n", &a);
		operate(a);
	}
	return 0;
}
