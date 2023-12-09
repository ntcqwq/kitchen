#include <bits/stdc++.h>

using namespace std;

#define endl "\n";
#define cheat ios_base::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);

int a, b, c, d, s;

int main() {
	cheat;
	cin >> a >> b >> c >> d >> s;
	int ns= s/(a+b);
	int bs = s/(c+d);
	int nr = s-(a+b)*ns;
	int br = s-(c+d)*bs;
	int np = (a-b)*ns;
	int bp = (c-d)*bs;
	if (nr > a) {
		np = np + a - (nr-a);
	} else {
		np = np + nr;
	}
	if (br > c) {
		bp = bp + c - (br-c);
	} else {
		bp = bp + br;
	}
	if (np > bp) {
		cout << "Nikky" << endl;	
	} else if (np<bp) {
		cout << "Byron" << endl;
	} else {
		cout << "Tied" << endl;
	}
	return 0;
}