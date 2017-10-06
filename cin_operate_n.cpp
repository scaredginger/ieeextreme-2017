#include <iostream>

using namespace std;

void operate(int);

void operate(int a) {
	cout << a << '\n';
}

int main() {
	int n;
	cin >> n;
	for (int i = 0; i < n; i++) {
		int a;
		cin >> a;
		operate(a);
	}
	return 0;
}
