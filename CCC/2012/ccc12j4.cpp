#include <bits/stdc++.h>

using namespace std;

#define endl "\n"
#define fastio ios_base::sync_with_stdio(false); cin.tie(nullptr)

typedef string str;
typedef long long ll;

const float inf = numeric_limits<float>::infinity();

int main() {
	fastio;
	int K;
	cin >> K;
	str w;
	cin >> w;
	for (int i = 0; i < w.size(); ++i) {
		int a = w[i];
		a -= 65;
		a -= (3*(i+1) + K);
		a += 26;
		a %= 26;
		a += 65;
		cout << (char)a;
	}
}