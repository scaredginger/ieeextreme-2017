#include <stdio.h>
#include <vector>

using namespace std;

struct item {
	int weight;
	int value;
	bool taken;
};

int max_weight;
int n;
vector<item> items;

int knapsack(int value, int weight);

int knapsack(int value, int weight) {
	int max_value = value;
	for (int i = 0; i < items.size(); i++) {
		if (!items[i].taken && items[i].weight + weight <= max_weight) {
			items[i].taken = true;
			int current_value = knapsack(value + items[i].value, weight + items[i].weight);
			if (current_value > max_value) {
				max_value = current_value;
			}
			items[i].taken = false;
		}
	}
	return max_value;
}

int main() {
	scanf("%d", &max_weight);
	scanf("%d", &n);
	items = vector<item>(n);
	for (int i = 0; i < n; i++) {
		int w, v;
		scanf("%d%d", &w, &v);
		items[i].weight = w;
		items[i].value = v;
		items[i].taken = false;
	}
	printf("%d", knapsack(0, 0));
	return 0;
}
