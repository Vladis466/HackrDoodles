#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

int main() {
	int t;
	int _r = 0;                             //Used to keep track of pattern row/col positon
	int _c = 0;
	cin >> t;                               //Number of test cases
	for (int a0 = 0; a0 < t; a0++) {          //For each test case
		int sw = 0;
		int R;                              //Number of rows and columns
		int C;
		cin >> R >> C;
		vector<string> G(R);                //An array of R strings where each string has C letters (columns)
		for (int G_i = 0; G_i < R; G_i++) {
			cin >> G[G_i];
		}
		int r;
		int c;
		cin >> r >> c;
		vector<string> P(r);
		for (int P_i = 0; P_i < r; P_i++) {
			cin >> P[P_i];
		}






		int x;
		int _i;
		int _j;

		for (int i = 0; i < R; i++) {                     //For the amt of rows in the grid
			if (r > R - i) { break; }                 //If not enough rows left to check, break
			for (int j = 0; j < C; j++) {                  //For the amt of cols in the grid
				if (c> C - j + _c) { break; }       //If not enough columns left to check, break out
				_r = 0;
				_c = 0;
				x = 0;
				if (P[_r][_c] == G[i][j]) {               //If first entry in pattern matches an entry, increment and check 
					_i = i;
					_j = j;
					while (P[_r][_c] == G[_i][_j]) {        //Loop through all both maps comparing the values
						_c += 1;
						_j += 1;
						x += 1;								//Var used for checking because column gets reset
						if (_c == c) { _c = 0; _r += 1; _i += 1; _j = j; }   //If we reach end of line, move to the next on both.  
						if (_r == r && x == c * r) { 
							cout << "YES" << endl; sw = 1; goto endloop; }
					}
				}
			}
		}
		endloop:
		if (sw != 1)
			cout << "NO" << endl;

	}
	return 0;
}