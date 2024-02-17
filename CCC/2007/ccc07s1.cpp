#include <bits/stdc++.h>

using namespace std;

#define endl "\n"
#define fastio ios_base::sync_with_stdio(false); cin.tie(nullptr)

typedef string str;
typedef long long ll;

const float inf = numeric_limits<float>::infinity();

int main() {
	fastio;
	int N;
	cin >> N;
	while (N--) {
		int y, m, d;
		cin >> y >> m >> d;
		if (y < 1989) {
			cout << "Yes" << endl;
		} else if (y > 1989) {
			cout << "No" << endl;
		} else if (m > 2) {
			cout << "No" << endl;
		} else if (m == 1) {
			cout << "Yes" << endl;
		} else if (m == 2 and d > 27) {
			cout << "No" << endl;
		} else {
			cout << "Yes" << endl;
		}
	}
	return 0;
}