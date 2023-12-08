#include <bits/stdc++.h>

using namespace std;

#define endl "\n";
#define cheat ios_base::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);

int N;
int main() {
	cheat;
	cin >> N;
    switch(N) {
        case 0:
            cout <<" * * *\n*     *\n*     *\n*     *\n\n*     *\n*     *\n*     *\n * * *\n";
        break;
        case 1:
            cout <<"\n      *\n      *\n      *\n\n      *\n      *\n      *\n\n";
        break;
        case 2:
            cout <<" * * *\n      *\n      *\n      *\n * * *\n*\n*\n*\n * * *\n";
        break;
        case 3:
            cout <<" * * *\n      *\n      *\n      *\n * * *\n      *\n      *\n      *\n * * *\n";
        break;
        case 4:
            cout <<"\n*     *\n*     *\n*     *\n * * *\n      *\n      *\n      *\n\n";
        break;
        case 5:
            cout <<" * * *\n*\n*\n*\n * * *\n      *\n      *\n      *\n * * *\n";
        break;
        case 6:
            cout <<" * * *\n*\n*\n*\n * * *\n*     *\n*     *\n*     *\n * * *\n";
        break;
        case 7:
            cout <<" * * *\n      *\n      *\n      *\n\n      *\n      *\n      *\n\n";
        break;
        case 8:
            cout <<" * * *\n*     *\n*     *\n*     *\n * * *\n*     *\n*     *\n*     *\n * * *\n";
        break;
        case 9:
            cout <<" * * *\n*     *\n*     *\n*     *\n * * *\n      *\n      *\n      *\n * * *\n";
		break;
	}
	return 0;
}