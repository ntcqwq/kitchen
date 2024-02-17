/**/ 

#include <algorithm>
#include <bits/stdc++.h>
#include <cmath>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <map>
#include <numeric>
#include <queue>
#include <ranges>
#include <set>
#include <stdio.h>
#include <string>
#include <utility>
#include <vector>

using namespace std;

#define INF 0x3f3f3f3f;
#define LINF 0x3f3f3f3f3f3f3f3f;
#define endl "\n";
#define cheat ios_base::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
 
typedef long long ll;
typedef long double db;
typedef string str;

// %d is int
// %f is float
// %s is str
// %c is char
// %ld is long int

#define scann(x) scanf("%d", &x);
#define scannn(x, y) scanf("%d%d", &x, &y);
#define scanS(x) scanf("%s", x)

#define printn(x) printf("%d\n", x);
#define printS(x) printf("%s\n", x);
#define printc(x) printf("%c\n", x);

#define size(x) int((x).size())
#define start(x) begin(x)
#define all(x) start(x), end(x)
#define rll(x) x.rbegin(), x.rend() 
#define sort(x) sort(all(x))  
#define pb push_back
#define eb emplace_back
#define ft front()
#define bk back()

#define lb lower_bound
#define ub upper_bound

#define fore(i, a, b) for (int i = (a); i < (b); ++i)
#define for0(i, a) fore(i, 0, a)
#define rof(i, a, b) for (int i = (b)-1; i >= (a); i--)
#define rof0(i, a) rof(i, 0, a)
#define rep(a) for0(_, a)
#define each(a, x) for (auto&a: x)

const ll big = 1e18; 
const db pie = acos((db)-1);

//========================end-of-my-template========================\\

const int mod = (int) 1e9+7;
const int mx = (int) 300010;

int main() {
  cheat;
#ifndef ONLINE_JUDGE
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
#endif

  int A, B;
  scannn(A, B);
  printn(B+(B-A));
}