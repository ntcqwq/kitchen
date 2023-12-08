#include <bits/stdc++.h>

using namespace std;

#define endl "\n"
#define fastio ios_base::sync_with_stdio(false); cin.tie(nullptr)

typedef string str;
typedef long long ll;

const float inf = numeric_limits<float>::infinity();

int main() {
	fastio;
	map<str, str> t;
	t["CU"] = "see you";
	t[":-)"] = "I'm happy";
	t[":-("] = "I'm unhappy";
	t[";-)"] = "wink";
	t[":-P"] = "stick out my tongue";
	t["(~.~)"] = "sleepy";
	t["TA"]	= "totally awesome";
	t["CCC"] = "Canadian Computing Competition";
	t["CUZ"] = "because";
	t["TY"]	= "thank-you";
	t["YW"]	= "you're welcome";
	t["TTYL"] = "talk to you later";
	while (true) {
		str N;
		cin >> N;
		if (t.find(N) != t.end()) {
			cout << t[N] << endl;	
		} else {
			cout << N << endl;
		}
		if (N == "TTYL") {
			break;		
		}
	}
	return 0;
}