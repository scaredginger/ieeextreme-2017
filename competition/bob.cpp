#include <iostream>
#include <vector>

using namespace std;
int main() {
	vector<vector<int>> preferences;
	for (int i = 1; i <= 10; i++) {       // Read in the preferences
		vector<int> position;
		int a, b;
		cin >> a >> b;
		position.push_back(a - 1);
		position.push_back(b - 1);
		preferences.push_back(position);
	}
	int min[2][3] = { 0,0,0,0,0,0 };
	for (int i = 0; i < 2; i++) {
		int count[3] = { 0,0,0 };
		count[preferences[0][i]] += 1;
		for (int j = 1; j < 9; j++) {
			if (preferences[j][i] != 0 && count[0] < 3) {
				min[i][0] += 1;
			}
			else {
				count[0] += 1;
			}
			if (preferences[j][i] != 1 && count[1] < 3) {
				if (i == 1) {
				}
				min[i][1] += 1;
			}
			else {
				count[1] += 1;
			}
			if (preferences[j][i] != 2 && count[2] < 3) {
				min[i][2] += 1;
			}
			else {
				count[2] += 1;
			}
		}
	}
	// Now Solving
	int best[3];
	best[2] = min[0][0];
	for (int i = 0; i < 2; i++) {
		for (int j = 0; j < 3; j++) {
			if (min[i][j] < best[2]) {
				best[0] = i;
				best[1] = j + 1;
				best[2] = min[i][j];
			}
		}
	}
	vector<vector<int>> bobMoves;
	for (int i = 0; i < 9; i++) {
		if ((i + 1) % 2 == 0) { // My Turn
			for (int j = 0; j < preferences.size(); j++) {
				if (preferences[j][best[0]] + 1 != best[1]) {
					cout << preferences[j][0] + 1 << " " << preferences[j][1] + 1 << endl;
					preferences.erase(preferences.begin() + j);
					break;
				}
			}
		}
		else {           // Bob's Turn
			bobMoves.push_back(preferences[0]);
			preferences.erase(preferences.begin());
		}
	}
	return 0;
}