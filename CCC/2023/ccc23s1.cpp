#include <bits/stdc++.h>

using namespace std;

#define endl "\n"
#define fastio ios_base::sync_with_stdio(false); cin.tie(nullptr)

typedef string str;
typedef long long ll;
typedef pair<int, int> pint;
typedef vector<int> vint;

const float inf = numeric_limits<float>::infinity();

int main() {
	fastio;
	int C;
	cin >> C;

	vector<vector<int>> cols(2, vector<int>(C));
	for (int row = 0; row < 2; row++) {
		for (int col = 0; col < C; col++) {
			cin >> cols[row][col];
		}
	}

	int total = 0;
	for (int row = 0; row < 2; row++) {
		for (int col = 0; col < C; col++) {
			if (cols[row][col] == 1) {
				int count = 3;
				if (col % 2 == 0) {
					if (row == 0) {
						if (cols[row + 1][col] == 1) {
							count -= 1;
						}
					} else {
						if (cols[row - 1][col] == 1) {
							count -= 1;
						}
					}
				}
				if (col < C - 1) {
					if (cols[row][col + 1] == 1) {
						count -= 1;
					}
				}
				if (col > 0) {
					if (cols[row][col - 1] == 1) {
						count -= 1;
					}
				}
				total += count;
			}
		}
	}

	cout << total << endl;
	return 0;
}