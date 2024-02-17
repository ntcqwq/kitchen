#include <bits/stdc++.h>

using namespace std;

#define endl "\n"
#define fastio ios_base::sync_with_stdio(false); cin.tie(nullptr)

typedef string str;
typedef long long ll;

const float inf = numeric_limits<float>::infinity();

int main() {
    fastio;
    int a, b, total = 0;
	cin >> a;
	cin >> b;

	for (int i = 1; i <= a; i++) {
		for (int j = 1; j <= b; j++) {
			if ((i + j) == 10) 
				total++;
		}
	}

	if (total == 1)
		cout << "There is 1 way to get the sum 10." << endl;
	else
		cout << "There are " << total << " ways to get the sum 10." << endl;

    return 0;
}