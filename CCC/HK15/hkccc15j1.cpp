#include <bits/stdc++.h>
using namespace std;
#define endl "\n";
#define fio cin.tie(nullptr) -> sync_with_stdio(false); 
typedef long long ll;
const int inf = INT_MAX;

string a[102], b[102];

int main() {
    fio;
    int N, aa=0, bb=0;
    cin >> N;
    for (int i = 0; i < N; ++i) {
        cin >> a[i];
    }
    for (int i = 0; i < N; ++i) {
        cin >> b[i];   
        if ((a[i] == "rock" and b[i] == "scissors") or (a[i] == "scissors" and b[i] == "paper") or (a[i] == "paper" and b[i] == "rock")) aa++;
        else if ((b[i] == "rock" and a[i] == "scissors") or (b[i] == "scissors" and a[i] == "paper") or (b[i] == "paper" and a[i] == "rock")) bb++;
    }
    cout << aa << " " << bb;
    return 0;
}