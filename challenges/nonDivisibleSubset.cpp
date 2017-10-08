//https://www.hackerrank.com/challenges/non-divisible-subset/problem

#include <iostream>
#include <vector>

using namespace std;

int main() {
	int count;
	int divisor;
        cin >> count >> divisor;
    	vector<int> remainders(divisor, 0);
	int newNumber;
	for(int i = 0; i < count; i++) {
		cin >> newNumber;
		remainders[newNumber%divisor] += 1;
	}
	//now find the best group from each remainder pair that adds to divisor
        //add the larger of the pair to the total group which can be formed.
	int compliment;
	int current;
	int sum = 0;
	int end = (divisor/2);
        sum += remainders[0];
	for (int i = 1; i <= end; i++) {
		current = remainders[i];
		compliment = remainders[divisor-i];
        	if(current == compliment) {
                	sum += 0; //if there is a halve it musn't be counted.
            	}
		else if(current > compliment) {
			sum += current;
		} else {
			sum += compliment;
		}
	}
	cout << sum;
	return 0;
}