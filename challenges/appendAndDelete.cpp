//https://www.hackerrank.com/challenges/append-and-delete/problem

#include <iostream>
#include <string>

using namespace std;

int main(){
    string s;
    cin >> s;
    string t;
    cin >> t;
    int k;
    cin >> k;

    int match = 0;
    bool done = false;
    while(done == false && match < s.length() && match < t.length()) {
        if(s[match] == t[match]) {
            match++;
        } else {
            done = true;
        }
    }

    if(s.length() + t.length() - 2*match > k) {
        cout << "No";
    } 
    
    else if((s.length() + t.length() - 2*match)%2 == k%2) {
        cout << "Yes";
    } 
    
    else if(s.length() + t.length() <= k) {
        cout << "Yes";
    } 
    
    else {
        cout << "No";
    }

    return 0;
}
