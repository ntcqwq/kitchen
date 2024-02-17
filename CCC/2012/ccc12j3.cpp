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
	for (int r = 0; r < K; ++r) {
		for (int c = 0; c < K; ++c) {
			cout << "*";
		}
		for (int c = 0; c < K; ++c) {
			cout << "x";
		}
		for (int c = 0; c < K; ++c) {
			cout << "*";
		}
		cout << endl;
	}
	for (int r = 0; r < K; ++r) {
		for (int c = 0; c < K; ++c) {
			cout << " ";
		}
		for (int c = 0; c < K; ++c) {
			cout << "x";
		}
		for (int c = 0; c < K; ++c) {
			cout << "x";
		}
		cout << endl;
	}
	for (int r = 0; r < K; ++r) {
		for (int c = 0; c < K; ++c) {
			cout << "*";
		}
		for (int c = 0; c < K; ++c) {
			cout << " ";
		}
		for (int c = 0; c < K; ++c) {
			cout << "*";
		}
		cout << endl;
	}
}