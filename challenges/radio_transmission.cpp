//https://www.hackerrank.com/challenges/hackerland-radio-transmitters/problem

#include <iostream>
#include <vector>

using namespace std;

int main() {
	int n;
	int k;
	cin >> n >> k;
	vector<int> x(n);
	for(int x_i = 0; x_i < n; x_i++) {
		cin >> x[x_i];
	}
	std::sort(x.begin(), x.end());
	int totalTransmitters = 0;
	int doneIndex = 0;
	int coverage = 0;
	int current;
	int last;
	int counter;
	while(doneIndex < x.size()) {
		current = x[doneIndex];
		last = current;
		counter = doneIndex + 1;
		while(x[counter] <= current + k && counter < x.size()) {
			last = x[counter];
			counter++;
		}
		totalTransmitters++;
		coverage = last + k;
		while(x[doneIndex] <= coverage && doneIndex < x.size()) {
			doneIndex++;
		}
	}
	cout << totalTransmitters;
	return 0;
}

