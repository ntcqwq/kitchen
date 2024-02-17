#include <bits/stdc++.h>

using namespace std;

#define endl "\n";
#define cheat ios_base::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);

int main() {
	cheat;
	while (true) {
		int N;
		cin >> N;
		if (N == 0) {
			break;
		}
		int x = sqrt(N);

		while (N % x != 0) {
			x++;
		}
		int y = N/x;
		cout << "Minimum perimeter is " << 2*(x+y) << " with dimensions " << x << " x " << y << endl;
	}
}